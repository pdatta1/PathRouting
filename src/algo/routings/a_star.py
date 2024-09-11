
from typing import List
from base.routing_base import *
from base.direction_base import * 

from algo.directions import * 
from algo_types.map_types import List, Node 
from algo_exceptions.route_exceptions import PathNotFoundException

import heapq


class AstarRouting(PathRoutingBase): 

    def __init__(
        self, 
        map: Map, 
    ) -> None: 
        self._map = map 
        self._direction_registry_factory = RouteDirectionFactory()

        self.initialize_direction_registry()


    def initialize_direction_registry(self) -> None: 
        self._direction_registry_factory.register_direction_protocol('Aisle', AisleDirections())
        self._direction_registry_factory.register_direction_protocol('Lane', LaneDirections())


    def heuristic(
        self, 
        current_node: Node, 
        target_node: Node
    ) -> int:
        """
            calculate the heuristic of the current node to the target node 
            current_node: current sitting node
            target_node: goal node to reach
        """
        return abs(current_node.coords.x - target_node.coords.x) + abs(current_node.coords.y - target_node.coords.y)
    

    def get_neighbors(
        self, 
        node: Node
    ) -> List[Node]:
        """
            get the neigbors of a node.
            travel can only to left and right for aisles
        """
        neighbors: List[Node] = [] 

        direction_protocol = self._direction_registry_factory.get_direction_protocol(node.node_type)
        directions = direction_protocol.get_directions()

        for direction in directions: 
            neighbor_coords: Tuple[int, int] = (node.coords.x  + direction[0], node.coords.y + direction[1])
            if 0 <= neighbor_coords[0] < self._map.lanes_nums and 0 <= neighbor_coords[1] < self._map.aisle_nums:
                neighbor: Node = self._map.get_node_by_coords(neighbor_coords[0], neighbor_coords[1])
                neighbors.append(neighbor)
        return neighbors
    

    def find_path(
        self, 
        current_node: Node, 
        target_node: Node
    ) -> List[Node]:
        
        open_list: List[Tuple[int, Node]] = []  
        closed_list = set() 

        node_relations: Dict[str, Node] = {} 
        g_score: Dict[str, int] = {current_node.id: 0}

        heapq.heappush(open_list, (0, current_node))


        while open_list: 
            _, current_node = heapq.heappop(open_list)


            if current_node.id == target_node.id: 
                return self.reconstruct_path(node_relations, current_node)
            
            closed_list.add(current_node.id)

            for neighbor in self.get_neighbors(current_node): 
                if neighbor.id in closed_list: 
                    continue

                tentative_g_score = g_score[current_node.id] + 1
                
                if neighbor.id not in g_score or tentative_g_score < g_score[neighbor.id]: 
                    node_relations[neighbor.id] = current_node
                    g_score[neighbor.id] = tentative_g_score
                    f_score: int = tentative_g_score + self.heuristic(neighbor, target_node)
                    heapq.heappush(open_list, (f_score, neighbor))
        
        return PathNotFoundException(f"Path from {current_node.coords} to {target_node.coords} is not possible")
            

            

    def reconstruct_path(
        self, 
        node_relations: Dict[Node, Node],
        current_node: Node 
    ) -> List[Node]:
        
        total_path: List[Node] = [current_node]
        while current_node.id in node_relations.keys(): 
            current_node = node_relations[current_node.id]
            total_path.append(current_node)
        return total_path[::-1]

