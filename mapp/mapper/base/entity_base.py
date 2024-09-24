
from typing import * 
from abc import ABC, abstractmethod

from mapp.mapper.map_types.mapper_types import Entity 

from mapp.algo.base.routing_base import PathRoutingBase


class MapperBase(ABC): 

    @abstractmethod
    def create_entity(self) -> None: 
        ...
        
    @abstractmethod
    def cleanup_context(self) -> None: 
        ...