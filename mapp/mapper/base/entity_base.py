
from typing import * 
from abc import ABC, abstractmethod

class MapperBase(ABC): 

    @abstractmethod
    def create_entity(self) -> None: 
        ...
        
    @abstractmethod
    def cleanup_context(self) -> None: 
        ...


class AsyncMapperBase(ABC): 
    @abstractmethod
    async def create_entity(self) -> None: 
        ...
        
    @abstractmethod
    async def cleanup_context(self) -> None: 
        ...
