
from typing import Dict, Tuple, Set 
from abc import abstractmethod, ABC 


class ReservationBase(ABC): 

    def __init__(
        self,
    ) -> None: 
        self.reservation_table: Dict[str, Set] = {} 

    @abstractmethod
    def is_reserved(
        self, 
        time: float, 
        x: int, 
        y: int, 
        z: int
    ) -> bool: 
        ... 

    @abstractmethod
    def reserve(
        self, 
        time: float, 
        x: int, 
        y: int, 
        z: int
    ) -> None: 
        ...
