from abc import ABC, abstractmethod
from typing import List, Tuple
from algo.algo_types.map_types import Node

class DirectionProtocol(ABC):
    """
    The DirectionProtocol abstract base class defines an interface for direction 
    protocols that specify valid movement directions for a node type on a map.
    Classes that inherit from DirectionProtocol must implement the `get_directions` 
    method to provide direction vectors.
    """

    @abstractmethod
    def get_directions(self) -> List[Tuple[int, int, int]]:
        """
        Abstract method to retrieve the movement directions allowed for a node.

        Returns:
            List[Tuple[int, int]]: A list of tuples, where each tuple represents 
            the change in x and y coordinates for a valid direction of movement.
        """
        pass
