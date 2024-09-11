
from typing import * 
from dataclasses import dataclass, field, MISSING
import uuid 
from uuid import UUID 


NodeTypes = Literal["Aisle", "Lane"]


@dataclass
class Coords: 
    x: int = field(default=MISSING)
    y: int = field(default=MISSING)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Coords): 
            raise NotImplemented
        return self.x == value.x and self.y == value.y 


@dataclass
class Node:
    coords: Coords
    node_type: NodeTypes = field(default=MISSING, compare=False)
    id: str = field(default=MISSING, compare=True)
    uuid: str = field(default=MISSING, compare=False)

    def __init__(
        self, 
        id: str, 
        node_type: NodeTypes, 
        coords: Coords,
    ) -> None: 
        uuid_conversion = UUID(id)
        object.__setattr__(self, 'id', uuid_conversion.int)
        object.__setattr__(self, 'node_type', node_type)
        object.__setattr__(self, 'coords', coords)
        object.__setattr__(self, 'uuid', id)

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Node): 
            raise NotImplemented
        return self.id == value.id 
    
    def __lt__(self, other: "Node") -> bool: 
        return self.coords.x < other.coords.x or self.coords.y < other.coords.y 

        




@dataclass(frozen=True)
class Map: 
    lanes_nums: int 
    aisle_nums: int 
    map_id: str
    coordinates: Dict[str, Node] = field(default_factory=dict)

    def get_node_by_coords(
        self, 
        x: int, 
        y: int
    ) -> Union[Node, None]: 
        for value in self.coordinates.values(): 
            if value.coords.x == x and value.coords.y == y: 
                return value 
            
    def get_node_by_id(
        self, 
        node_id: str 
    ) -> Union[Node, None]: 
        node = self.coordinates.get(node_id)
        if not node: 
            raise KeyError(f"Node doesn't exist in Map with Id: {node_id}")
        return node 
    
    def get_map_length(self) -> int: 
        return len(self.coordinates)

