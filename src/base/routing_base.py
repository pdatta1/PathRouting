

from typing import * 
from abc import abstractmethod, ABC 

from algo_types.map_types import * 


class PathRoutingBase(ABC): 

    def __init__(
        self, 
        map: Map,
    ) -> None: 
        ...


    @abstractmethod
    def heuristic(
        self, 
        current_node: Node,
        target_node: Node 
    ) -> int: 
        ...
    

    @abstractmethod
    def get_neighbors(
        self, 
        node: Node 
    ) -> List[Node]: 
        ...


    @abstractmethod
    def find_path(
        self, 
        current_node: Node,
        target_node: Node
    ) -> List[Node]: 
        ... 
    
