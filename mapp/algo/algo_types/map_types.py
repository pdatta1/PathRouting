from typing import Literal, Dict, Union, List 
from dataclasses import dataclass, field, MISSING
import uuid
from uuid import UUID

# Define the allowed node types
NodeTypes = Literal["Aisle", "Lane", "VTU"]

@dataclass
class Coords:
    """
    Represents the coordinates of a node on the map.
    
    Attributes:
        x (int): The x-coordinate.
        y (int): The y-coordinate.
    """
    x: int = field(default=MISSING)
    y: int = field(default=MISSING)
    z: int = field(default=MISSING)

    def __eq__(self, value: object) -> bool:
        """
        Checks equality between two Coords objects.

        Args:
            value (object): The object to compare against.

        Returns:
            bool: True if both objects have the same coordinates, otherwise False.
        """
        if not isinstance(value, Coords):
            raise NotImplemented
        return self.x == value.x and self.y == value.y and self.z == value.z

@dataclass
class Node:
    """
    Represents a node on the map. Each node is identified by its unique id (UUID) 
    and has a specific type (either 'Aisle' or 'Lane').

    Attributes:
        coords (Coords): The coordinates of the node.
        node_type (NodeTypes): The type of the node ('Aisle' or 'Lane').
        id (str): The string UUID of the node, converted to an integer.
        uuid (str): The original string UUID.
    """
    coords: Coords
    node_type: NodeTypes = field(default=MISSING, compare=False)
    id: str = field(default=MISSING, compare=True)
    uuid: str = field(default=MISSING, compare=False)

    def __init__(self, id: str, node_type: NodeTypes, coords: Coords) -> None:
        """
        Initializes the Node with an id, node_type, and coordinates.
        
        Args:
            id (str): The UUID of the node.
            node_type (NodeTypes): The type of the node ('Aisle' or 'Lane').
            coords (Coords): The coordinates of the node.
        """
        uuid_conversion = UUID(id)
        object.__setattr__(self, 'id', uuid_conversion.int)
        object.__setattr__(self, 'node_type', node_type)
        object.__setattr__(self, 'coords', coords)
        object.__setattr__(self, 'uuid', id)

    def __eq__(self, value: object) -> bool:
        """
        Checks equality between two Node objects.

        Args:
            value (object): The object to compare against.

        Returns:
            bool: True if both nodes have the same id, otherwise False.
        """
        if not isinstance(value, Node):
            raise NotImplemented
        return self.id == value.id

    def __lt__(self, other: "Node") -> bool:
        """
        Less-than comparison between two nodes. A node is considered less than another 
        if its x or y coordinate is smaller.

        Args:
            other (Node): The node to compare against.

        Returns:
            bool: True if this node's x or y coordinate is smaller, otherwise False.
        """
        return self.coords.x < other.coords.x or self.coords.y < other.coords.y or self.coords.z < other.coords.z 


@dataclass(frozen=True)
class Map:
    """
    Represents a map composed of multiple nodes, identified by their coordinates and UUIDs.
    
    Attributes:
        lanes_nums (int): Number of lanes in the map.
        aisle_nums (int): Number of aisles in the map.
        map_id (str): The unique identifier of the map.
        coordinates (Dict[str, Node]): A dictionary mapping node IDs to Node objects.
    """
    lanes_nums: int
    aisle_nums: int
    level_nums: int 
    map_id: str
    coordinates: Dict[str, Node] = field(default_factory=dict)

    def get_node_by_coords(self, x: int, y: int, z: int) -> Union[Node, None]:
        """
        Retrieves a node based on its coordinates (x, y).

        Args:
            x (int): The x-coordinate of the node.
            y (int): The y-coordinate of the node.

        Returns:
            Node or None: The Node object if found, otherwise None.
        """
        for value in self.coordinates.values():
            if value.coords.x == x and value.coords.y == y and z == value.coords.z:
                return value
            

    def get_node_by_id(self, node_id: str) -> Union[Node, None]:
        """
        Retrieves a node based on its UUID.

        Args:
            node_id (str): The UUID of the node.

        Returns:
            Node: The Node object if found.

        Raises:
            KeyError: If the node does not exist in the map.
        """
        node = self.coordinates.get(node_id)
        if not node:
            raise KeyError(f"Node doesn't exist in Map with Id: {node_id}")
        return node

    def get_nodes_by_types(self, node_type: str) -> List[Node]: 
        nodes_to_return: List[Node] = []
        for node in self.coordinates.values(): 
            if node.node_type == node_type: 
                nodes_to_return.append(node)   
        return nodes_to_return       

    def get_map_length(self) -> int:
        """
        Returns the total number of nodes on the map.

        Returns:
            int: The number of nodes in the map.
        """
        return len(self.coordinates)


@dataclass
class Path: 
    nodes: List[Node]
    computation_time: float 