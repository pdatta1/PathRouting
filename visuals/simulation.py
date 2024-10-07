from mapp.mapper.mappers.dynamic_mapper import DynamicMapper
from mapp.algo.routings.a_star import AstarRouting
from mapp.mapper.map_types.mapper_types import Entity, Node, MapEntity
from mapp.algo.algo_types.map_types import Path, Coords
from mapp.algo.base.routing_base import PathRoutingBase

from typing import List, Dict, Union
from dataclasses import dataclass, field, MISSING

@dataclass 
class SimulatedEntity: 
    entity: MapEntity 
    path: Path 
    path_progress: int = field(default=0)

    def increase_progress(self, new_progress: int) -> None: 
        self.path_progress += new_progress

class SimulationManager:
    def __init__(self, mapper: DynamicMapper):
        self.mapper = mapper
        self.simulations: List[SimulatedEntity] = [] 

    def add_simulation(
        self, 
        entity_id: str, 
        entity_type: str, 
        algorithm: str,
        coords: Coords 
    ) -> None: 
        entity: Union[MapEntity, None] = self.mapper.entity.get_entity(entity_id, entity_type)
        if not entity: 
            raise Exception(f"cannot find entity by id [{entity_id}] and type [{entity_type}]")
        
        destinated_node: Union[Node, None] = self.mapper.entity.map.get_node_by_coords(coords.x, coords.y, coords.z)
        if not destinated_node: 
            raise Exception(f"cannot find node by coords [{coords}]")
        
        routing: Union[PathRoutingBase, None] = self.mapper.get_algorithm(algorithm)
        if not routing: 
            raise Exception(f"cannot find routing [{algorithm}]")
        
        path: Path = routing.find_path(entity.entity_loc, destinated_node)
        if path and path.nodes: 
            self.simulations.append(SimulatedEntity(entity=entity, path=path))
        

    def run_simulation(
        self, 
    ) -> None: 
        for simulation in self.simulations: 
            # print(f"Computation Time: [{simulation.entity.entity_id}] ---> {simulation.path.computation_time}")
            if simulation.path_progress < len(simulation.path.nodes): 
                next_node = simulation.path.nodes[simulation.path_progress]
                simulation.entity.entity_loc = next_node 
                simulation.increase_progress(1)
                


        
