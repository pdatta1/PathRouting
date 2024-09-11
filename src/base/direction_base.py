
from abc import ABC, abstractmethod
from typing import List, Tuple

from algo_types.map_types import Node 

class DirectionProtocol(ABC): 

    @abstractmethod
    def get_directions(self) -> List[Tuple[int, int]]: 
        ...