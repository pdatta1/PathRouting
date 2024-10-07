
from typing import Dict, Union 

from mapp.mapper.base.entity_base import MapperBase
from mapp.mapper.map_types.mapper_types import Entity 

from mapp.algo.base.routing_base import PathRoutingBase


class ReservationMapperV1(MapperBase): 

    def __init__(self, entity: Entity) -> None:
        self.entity = entity 
        self.__algorithms_registry: Dict[str, PathRoutingBase] = {} 

    def create_entity(self) -> None:
        return super().create_entity()
    
    def cleanup_context(self) -> None:
        return super().cleanup_context()
    
    def register_algorithm(
        self, 
        algorithm_identifier: str, 
        algorithm: PathRoutingBase
    ) -> None: 
        self.__algorithms_registry[algorithm_identifier] = algorithm

    def remove_algorithm(
        self, 
        algorithm_identifier: str 
    ) -> None: 
        self.__algorithms_registry.pop(algorithm_identifier)

    def get_algorithm(
        self, 
        algorithm_identifier: str 
    ) -> Union[PathRoutingBase, None]: 
        return self.__algorithms_registry.get(algorithm_identifier, None)