from typing import List
from abc import abstractmethod, ABC
from algo_types.map_types import Map, Node

class PathRoutingBase(ABC):
    """
    PathRoutingBase is an abstract base class that defines the essential methods
    for pathfinding algorithms. Classes that inherit from PathRoutingBase must
    implement these methods to define their own pathfinding logic.
    """

    def __init__(self, map: Map) -> None:
        """
        Initializes the PathRoutingBase with a given map. The map contains the
        nodes and their relationships that the pathfinding algorithm will use.

        Args:
            map (Map): The map on which pathfinding will be performed.
        """
        self._map = map

    @abstractmethod
    def heuristic(self, current_node: Node, target_node: Node) -> int:
        """
        Abstract method to compute the heuristic value for a given node. The 
        heuristic is typically a measure of distance from the current node to the 
        target node.

        Args:
            current_node (Node): The current node being evaluated.
            target_node (Node): The goal node for the pathfinding algorithm.

        Returns:
            int: The heuristic distance between the current node and the target node.
        """
        pass

    @abstractmethod
    def get_neighbors(self, node: Node) -> List[Node]:
        """
        Abstract method to retrieve the neighboring nodes of a given node. These 
        neighbors are determined based on the movement rules defined for the map.

        Args:
            node (Node): The node for which to find neighbors.

        Returns:
            List[Node]: A list of neighboring nodes.
        """
        pass

    @abstractmethod
    def find_path(self, current_node: Node, target_node: Node) -> List[Node]:
        """
        Abstract method to find the optimal path from the current node to the 
        target node. The method must return the sequence of nodes that constitutes
        the shortest path between the two nodes.

        Args:
            current_node (Node): The starting node.
            target_node (Node): The goal node.

        Returns:
            List[Node]: A list of nodes representing the optimal path from the 
                        start node to the target node.
        """
        pass
