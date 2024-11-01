
import heapq
import time 
from collections import deque
from typing import List, Tuple, Dict 

from mapp.algo.algo_types.map_types import List
from mapp.algo.base.routing_base import (
    PathRoutingBase, 
    Entity,
    Node,
)
from mapp.algo.reservations.reservation_v1 import ReservationTableV1
from mapp.algo.algo_types.route_types import Path, PathState
from mapp.algo.algo_exceptions.route_exceptions import PathNotFoundException

class MappAstar(PathRoutingBase): 

    def __init__(
        self, 
        entity: Entity
    ) -> None: 
        self.entity = entity 
        self.reservation = ReservationTableV1()

    def get_occupied_nodes_by_level(
        self,
        static: bool, 
        level: int,
    ) -> List[Node]: 
        
        return [
            map_entity.entity_loc
            for map_entities in self.entity.map_entities.values()
            for map_entity in map_entities
            if map_entity.entity_loc.coords.z == level and map_entity.static == static 
        ]


    def heuristic(self, current_node: Node, target_node: Node) -> int:
        return abs(current_node.coords.x - target_node.coords.x) + abs(current_node.coords.y - target_node.coords.y) + abs(current_node.coords.z - target_node.coords.z)
    

    def find_path(self, current_node: Node, target_node: Node) -> List[Node]:
        
        open_list: List[PathState] = [] 
        open_set = set() 
        closed_list = set() 

        obstacles: List[Node] = self.get_occupied_nodes_by_level(static=True, level=current_node.coords.z)
        path_state = PathState(
            x=current_node.coords.x, 
            y=current_node.coords.y, 
            z=current_node.coords.z, 
            id=current_node.id,
            f_score=0,
            time=0
        )

        node_relations: Dict[str, Node] = {} 
        g_score: Dict[str, int] = {current_node.id: 0}

        total_compute_time: float = 0.0 

        heapq.heappush(open_list, path_state)
        open_set.add(path_state.id)

        start_time_compute: float = time.perf_counter() 

        while open_list: 
            current_state = heapq.heappop(open_list)

            open_set.remove(current_state.id)

            if current_state.id == target_node.id: 
                end_time_compute: float = time.perf_counter() 
                total_compute_time = end_time_compute - start_time_compute

                constructed_path: List[Node] = self.reconstruct_path(node_relations, current_node)
                return Path(
                    nodes=constructed_path,
                    computation_time=total_compute_time,
                    obstacles=obstacles
                )
            
            closed_list.add(current_node.id)

            for neighbor in current_node.connections: 
                if neighbor.id in closed_list: 
                    continue

                if neighbor in obstacles: 
                    continue

                tentative_g_score = g_score[current_node.id] + 1
                if neighbor.id not in g_score or tentative_g_score < g_score[neighbor.id]:
                    node_relations[neighbor.id] = current_node
                    g_score[neighbor.id] = tentative_g_score
                    f_score: int = tentative_g_score + self.heuristic(neighbor, target_node)

                    new_state = PathState(
                        x=neighbor.coords.x,
                        y=neighbor.coords.y, 
                        z=neighbor.coords.z, 
                        id=neighbor.id,
                        time=current_state.time + 1,
                        f_score=f_score
                    )

                    if self.reservation.is_reserved(
                        time=new_state.time,
                        x=new_state.x, 
                        y=new_state.y,
                        z=new_state.z 
                    ): 
                        continue

                    if new_state.id not in open_set: 
                        heapq.heappush(open_list, path_state)
                        open_set.add(new_state.id)

        raise PathNotFoundException(f"Path from {current_node.coords} to {target_node.coords} is not possible")
    
    
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