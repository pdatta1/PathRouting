
from typing import * 
from abc import ABC, abstractmethod

from mapper.map_types.mapper_types import Entity 

from algo.base.routing_base import PathRoutingBase


class MapperBase(ABC): 

    @abstractmethod
    def create_entity(self) -> None: 
        ...
        
    @abstractmethod
    def cleanup_context(self) -> None: 
        ...