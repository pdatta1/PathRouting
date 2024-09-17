
from typing import * 
from abc import ABC, abstractmethod

from algo.base.routing_base import PathRoutingBase


class MapperBase(ABC): 

    def __init__(self) -> None: 
        self._algorithms: Dict[str, PathRoutingBase] = {} 

    @abstractmethod
    def __load_map_components(
        self, 
        map_id: str
    ) -> None: 
        ...
        
    @abstractmethod
    def register_algorithm(
        self, 
        algorithm_identifier: str, 
        algorithm: PathRoutingBase
    ) -> None: 
        ...

    @abstractmethod
    def remove_algorithm(
        self, 
        algorithm_identifier: str
    ) -> None: 
        ...
       
    @abstractmethod
    def get_suitable_algorithm_for_route(
        self
    ) -> PathRoutingBase: 
        ...