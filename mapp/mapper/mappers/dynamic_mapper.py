
from typing import Dict, List, Union

from mapper.base.entity_base import MapperBase
from mapper.map_types.mapper_types import Entity 

from algo.base.routing_base import PathRoutingBase


class DynamicMapper(MapperBase): 

    def __init__(self, entity: Entity) -> None:

        self.entity = entity 

        self.__algorithms_registry: Dict[str, PathRoutingBase] = {} 


    def create_entity(self) -> Entity:
        return super().create_entity()
    
    def cleanup_context(self) -> None:
        return super().cleanup_context()

    async def __aenter__(self) -> None: 
        self.create_entity()

    async def __aexit__(self, exc_type, exc_value, traceback) -> None: 
        self.cleanup_context()

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
        return self.__algorithms_registry.get(algorithm_identifier)

    