from typing import List, Tuple, Dict
from mapp.algo.base.routing_base import PathRoutingBase
from mapp.algo.directions import RouteDirectionFactory
from mapp.algo.directions import (
    AisleDirections, 
    LaneDirections,
    ElevationDirections
)
from mapp.algo.algo_types.map_types import Map, Node, Path, Coords
from mapp.algo.algo_exceptions.route_exceptions import (
    PathNotFoundException, 
    VTUNotFound,
    NotSameLevelRoutingException
)

from mapp.mapper.map_types.mapper_interfaces import MapNodeTypes
from mapp.mapper.map_types.mapper_types  import MapEntity
from mapp.mapper.base.entity_base import Entity


import heapq
import time 
from collections import deque

class AstarRouting(PathRoutingBase):
    """
    AstarRouting is an implementation of the A* pathfinding algorithm.
    It calculates the optimal path from a start node to a target node on a map.
    The class utilizes different direction protocols for aisles and lanes,
    and computes the shortest path based on a heuristic function.
    """

    def __init__(self, entity: Entity) -> None:
        """
        Initializes the AstarRouting class with a provided map and sets up the
        direction registry using the factory pattern.

        Args:
            map (Map): The map on which the routing will be performed.
        """
        self.entity = entity
        self._direction_registry_factory = RouteDirectionFactory()
        self.initialize_direction_registry()

    def initialize_direction_registry(self) -> None:
        """
        Initializes the direction registry by registering protocols for Aisle
        and Lane navigation. This allows the class to handle different movement
        behaviors based on node types.
        """
        self._direction_registry_factory.register_direction_protocol(MapNodeTypes.Aisle.value, AisleDirections())
        self._direction_registry_factory.register_direction_protocol(MapNodeTypes.Lane.value, LaneDirections())
        self._direction_registry_factory.register_direction_protocol(MapNodeTypes.VTU.value, ElevationDirections())

    def heuristic(self, current_node: Node, target_node: Node) -> int:
        """
        Computes the heuristic value for the A* algorithm. The heuristic is the 
        Manhattan distance between the current node and the target node.

        Args:
            current_node (Node): The node being evaluated.
            target_node (Node): The goal node to reach.

        Returns:
            int: The heuristic distance from the current node to the target node.
        """
        return abs(current_node.coords.x - target_node.coords.x) + abs(current_node.coords.y - target_node.coords.y) + abs(current_node.coords.z - target_node.coords.z)

    def get_neighbors(self, node: Node) -> List[Node]:
        """
        Retrieves the neighboring nodes of a given node based on the registered
        direction protocol. The direction can vary depending on the node type 
        (Aisle or Lane).

        Args:
            node (Node): The node for which to find neighbors.

        Returns:
            List[Node]: A list of neighboring nodes.
        """
        neighbors: List[Node] = []

        direction_protocol = self._direction_registry_factory.get_direction_protocol(node.node_type)
        directions = direction_protocol.get_directions()

        # Calculate neighbors based on valid movement directions
        for direction in directions:

            neighbor_coords: Tuple[int, int] = (node.coords.x + direction[0], node.coords.y + direction[1], node.coords.z + direction[2])
            if 0 <= neighbor_coords[0] < self.entity.map.lanes_nums and 0 <= neighbor_coords[1] < self.entity.map.aisle_nums and neighbor_coords[2] < self.entity.map.level_nums :
                neighbor: Node = self.entity.map.get_node_by_coords(neighbor_coords[0], neighbor_coords[1], neighbor_coords[2])
                if neighbor:
                    neighbors.append(neighbor)
        return neighbors + node.connections

    def get_occupied_node_by_level(
        self,
        static: bool, 
        level: int,
    ) -> List[Node]: 
        
        occupied_coords: List[Coords] = [] 
        for map_entities in self.entity.map_entities.values(): 
            for map_entity in map_entities: 
                if map_entity.static == static and map_entity.entity_loc.coords.z == level: 
                    occupied_coords.append(map_entity.entity_loc)
        return occupied_coords


    def find_path_on_same_level(self, current_node: Node, target_node: Node) -> Path:
        """
        Implements the A* pathfinding algorithm to find the optimal path from 
        the current node to the target node.

        Args:
            current_node (Node): The starting node.
            target_node (Node): The goal node.

        Returns:
            List[Node]: The optimal path from the current node to the target node.
        
        Raises:
            PathNotFoundException: If no path exists between the start and target nodes.
        """
        open_list: List[Tuple[int, Node]] = []  # Priority queue (min-heap) to track nodes to evaluate
        closed_list = set()  # Set of nodes that have already been evaluated

        occupied_locations: List[Coords] = self.get_occupied_node_by_level(static=True, level=current_node.coords.z)

        node_relations: Dict[str, Node] = {}  # Dictionary to store node relationships (for path reconstruction)
        g_score: Dict[str, int] = {current_node.id: 0}  # Cost from start node to each node

        total_compute_time: float = 0.0

        if current_node.coords.z != target_node.coords.z: 
            raise NotSameLevelRoutingException("you are using a method that restricts routing on the same level.")

        heapq.heappush(open_list, (0, current_node))  # Push starting node to open list
        
        start_time_compute: float = time.perf_counter()
        while open_list:
            _, current_node = heapq.heappop(open_list)  # Pop node with lowest f-score

            # Check if we have reached the target node
            if current_node.id == target_node.id:
                end_time_compute: float = time.perf_counter()
                total_compute_time = end_time_compute - start_time_compute
                constructed_path: List[Node] = self.reconstruct_path(node_relations, current_node)
                return Path(
                    nodes=constructed_path,
                    computation_time=total_compute_time
                )

            closed_list.add(current_node.id)  # Mark current node as evaluated

            # Explore neighbors
            for neighbor in current_node.connections:
                if neighbor.id in closed_list:
                    continue  # Skip already evaluated nodes

                if neighbor in occupied_locations: 
                    continue

                

                tentative_g_score = g_score[current_node.id] + 1  # Cost to reach neighbor

                # Update g-score if this path is better or not explored
                if  neighbor.id not in g_score or tentative_g_score < g_score[neighbor.id]:
                    node_relations[neighbor.id] = current_node
                    g_score[neighbor.id] = tentative_g_score
                    f_score: int = tentative_g_score + self.heuristic(neighbor, target_node)
                    heapq.heappush(open_list, (f_score, neighbor))  # Add neighbor to open list

        # If no path found, raise an exception
        raise PathNotFoundException(f"Path from {current_node.coords} to {target_node.coords} is not possible")
    
    def find_path(self, current_node: Node, target_node: Node) -> List[Node]:
        return self.find_path_on_same_level(current_node, target_node)

    def find_closest_vtu(self, start_node: Node) -> Node: 
        visited = set() 
        queue = deque([start_node])

        while queue: 
            current_node = queue.popleft()
            if current_node.node_type == MapNodeTypes.VTU.value: 
                return current_node
            
            visited.add(current_node.id)

            neighbors = self.get_neighbors(current_node)
            for neighbor in neighbors: 
                if neighbor.id not in visited and neighbor not in queue: 
                    queue.append(neighbor)
        
        return VTUNotFound(f"No VTU found near the current node")

    def reconstruct_path(self, node_relations: Dict[Node, Node], current_node: Node) -> List[Node]:
        """
        Reconstructs the path from the target node to the start node by backtracking
        using the node_relations dictionary.

        Args:
            node_relations (Dict[Node, Node]): The dictionary containing node relationships.
            current_node (Node): The node to backtrack from (typically the target node).

        Returns:
            List[Node]: The reconstructed path in the correct order, from start to target.
        """
        total_path: List[Node] = [current_node]  # Start with the current node (goal node)
        
        # Backtrack using node_relations
        while current_node.id in node_relations.keys():
            current_node = node_relations[current_node.id]
            total_path.append(current_node)
        
        return total_path[::-1]  # Reverse the path to return it from start to goal
