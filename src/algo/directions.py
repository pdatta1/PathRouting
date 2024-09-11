from typing import List, Tuple, Dict, Union
from algo_types.map_types import Node
from base.direction_base import DirectionProtocol

class AisleDirections(DirectionProtocol):
    """
    AisleDirections is a concrete implementation of the DirectionProtocol.
    It defines the valid movement directions for nodes of type 'Aisle', which 
    are restricted to vertical movements (up and down).
    """

    def get_directions(self) -> List[Tuple[int, int]]:
        """
        Provides the movement directions for aisle nodes. Aisles allow movement 
        only in the vertical direction (up and down).

        Returns:
            List[Tuple[int, int]]: A list of direction tuples. Each tuple represents
            the change in x and y coordinates.
        """
        return [(0, 1), (0, -1)]  # Up (0, 1), Down (0, -1)

class LaneDirections(DirectionProtocol):
    """
    LaneDirections is a concrete implementation of the DirectionProtocol.
    It defines the valid movement directions for nodes of type 'Lane', which 
    are restricted to horizontal movements (left and right).
    """

    def get_directions(self) -> List[Tuple[int, int]]:
        """
        Provides the movement directions for lane nodes. Lanes allow movement 
        only in the horizontal direction (left and right).

        Returns:
            List[Tuple[int, int]]: A list of direction tuples. Each tuple represents
            the change in x and y coordinates.
        """
        return [(1, 0), (-1, 0)]  # Right (1, 0), Left (-1, 0)

class RouteDirectionFactory:
    """
    RouteDirectionFactory is responsible for managing and retrieving direction 
    protocols based on node types (Aisle, Lane). This uses the factory pattern 
    to allow dynamic protocol registration and retrieval.
    """

    def __init__(self) -> None:
        """
        Initializes the RouteDirectionFactory by creating an empty direction 
        protocol registry.
        """
        self.__direction_registry: Dict[str, DirectionProtocol] = {}

    def register_direction_protocol(
        self, 
        direction_protocol_tag: str, 
        direction_protocol: DirectionProtocol
    ) -> None:
        """
        Registers a direction protocol in the factory using a string tag.

        Args:
            direction_protocol_tag (str): A unique tag representing the node type 
                                          (e.g., 'Aisle', 'Lane').
            direction_protocol (DirectionProtocol): The direction protocol implementation 
                                                    for the corresponding tag.
        """
        self.__direction_registry[direction_protocol_tag] = direction_protocol

    def get_direction_protocol(
        self, 
        direction_protocol_tag: str
    ) -> DirectionProtocol:
        """
        Retrieves the direction protocol corresponding to the provided tag.

        Args:
            direction_protocol_tag (str): The tag of the direction protocol to retrieve.

        Returns:
            DirectionProtocol: The corresponding direction protocol instance.
        """
        direction_protocol: Union[DirectionProtocol, None] = self.__direction_registry.get(direction_protocol_tag)
        return direction_protocol

    def get_direction_registry(self) -> Dict[str, DirectionProtocol]:
        """
        Returns the complete direction protocol registry.

        Returns:
            Dict[str, DirectionProtocol]: A dictionary mapping direction protocol tags 
                                          to their respective direction protocol instances.
        """
        return self.__direction_registry
