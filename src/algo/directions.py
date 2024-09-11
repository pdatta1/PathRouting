
from typing import List, Tuple, Dict, Union
from algo_types.map_types import Node
from base.direction_base import DirectionProtocol


class AisleDirections(DirectionProtocol): 
    def get_directions(self) -> List[Tuple[int, int]]:
        return [(0, 1), (0, -1)]

class LaneDirections(DirectionProtocol): 
    def get_directions(self) -> List[Tuple[int, int]]:
        return [(1, 0), (-1, 0)]
    

class RouteDirectionFactory: 
    def __init__(self) -> None: 
        self.__direction_registry: Dict[str, DirectionProtocol] = {} 

    def register_direction_protocol(
        self, 
        direction_protocol_tag: str,
        direction_protocol: DirectionProtocol
    ) -> None: 
        self.__direction_registry[direction_protocol_tag] = direction_protocol

    def get_direction_protocol(
        self, 
        direction_protocol_tag: str 
    ) -> DirectionProtocol: 
        direction_protocol: Union[DirectionProtocol, None] = self.__direction_registry.get(direction_protocol_tag)
        return direction_protocol
    
    def get_direction_registry(
        self,
    ) -> Dict[str, DirectionProtocol]: 
        return self.__direction_registry