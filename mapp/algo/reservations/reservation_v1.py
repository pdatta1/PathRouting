
from typing import Tuple
from mapp.algo.base.reservation_base import ReservationBase

class ReservationTableV1(ReservationBase): 
    def __init__(self) -> None:
        super().__init__()

    def is_reserved(
        self, 
        time: float, 
        x: int, 
        y: int, 
        z: int
    ) -> bool:
        return (x, y, z) in self.reservation_table.get(time, set())
    
    def reserve(
        self,         
        time: float,
        x: int, 
        y: int, 
        z: int
    ) -> None:
        if time not in self.reservation_table: 
            self.reservation_table[time] = set() 
        self.reservation_table[time].add((x, y, z)) 
    