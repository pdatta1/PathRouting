
from dataclasses import dataclass, field
from typing import List 

from mapp.algo.algo_types.map_types import Node 


@dataclass
class Path: 
    nodes: List[Node]
    computation_time: float 
    obstacles: List[Node]  = field(default_factory=list)


@dataclass
class PathState: 
    x: int 
    y: int 
    z: int 
    id: str
    time: float = field(default=0)

    def __eq__(self, value: 'PathState') -> bool:
        return value.x == self.x and value.y == self.y and value.z == self.z and value.time == self.time
