
from dataclasses import dataclass, field
from typing import List 
from functools import total_ordering

from mapp.algo.algo_types.map_types import Node 


@dataclass
class Path: 
    nodes: List[Node]
    computation_time: float 
    obstacles: List[Node]  = field(default_factory=list)


@dataclass
@total_ordering
class PathState: 
    x: int 
    y: int 
    z: int 
    id: str 
    f_score: float = field(default=0)
    time: float = field(default=0)

    def __eq__(self, value: 'PathState') -> bool:
        return value.x == self.x and value.y == self.y and value.z == self.z and value.time == self.time and value.id == self.id 

    def __lt__(self, value: 'PathState') -> bool: 
        return self.time < value.time and self.f_score < value.f_score
    
