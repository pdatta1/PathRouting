import random
from typing import Dict, List, Tuple 
from uuid import uuid4

from mapp.algo.algo_types.map_types import Map, Node, Coords

from typing import List, Tuple

from typing import Dict, List, Tuple
from uuid import uuid4
from mapp.algo.algo_types.map_types import Map, Node, Coords


def generate_map(lanes_nums: int, level_nums: int) -> Map:
    coordinates: Dict[str, Node] = {}
    vtu_objects: List[Node] = []
    new_nodes: Dict[Tuple[int, int, int], Node] = {}  # Use (x, y, z) as keys to prevent duplicates

    # Define the y-coordinates for the two horizontal aisles
    aisle_positions = [3, 6]  # Aisles at y=3 and y=6 (across all lanes)

    # Generate VTU objects
    for z in range(level_nums):
        vtu_object = Node(coords=Coords(x=6, y=8, z=z), node_type="vtu", id=str(uuid4()))
        vtu_objects.append(vtu_object)

    # Generate the lanes and aisles
    for x in range(lanes_nums):
        for z in range(level_nums):
            for y in range(9):
                # Determine node type
                if y in aisle_positions:
                    node_type = "aisle"
                else:
                    node_type = "lane"

                # Check if the position is free before adding a new node
                if (x, y, z) not in new_nodes:
                    node = Node(coords=Coords(x=x, y=y, z=z), node_type=node_type, id=str(uuid4()))
                    new_nodes[(x, y, z)] = node

    # Establish connections between neighboring nodes with restricted movement based on node type
    for (x, y, z), node in new_nodes.items():
        neighbors = []

        if y in aisle_positions:  # Aisle travel (left-right on the x-axis)
            for dx in [-1, 1]:  # Only horizontal movement
                neighbor_coords = (x + dx, y, z)
                if neighbor_coords in new_nodes:
                    neighbors.append(new_nodes[neighbor_coords])

            # Allow vertical movement at specific intersections (where aisle meets lane)
            for dy in [-1, 1]:  # Up-down movement only at intersections
                neighbor_coords = (x, y + dy, z)
                if neighbor_coords in new_nodes:
                    neighbors.append(new_nodes[neighbor_coords])

        else:  # Lane travel (up-down on the y-axis)
            for dy in [-1, 1]:  # Only vertical movement
                neighbor_coords = (x, y + dy, z)
                if neighbor_coords in new_nodes:
                    neighbors.append(new_nodes[neighbor_coords])

            # Allow horizontal movement at intersections (where lane meets aisle)
            for dx in [-1, 1]:  # Left-right movement only at intersections
                neighbor_coords = (x + dx, y, z)
                if neighbor_coords in new_nodes and y in aisle_positions:
                    neighbors.append(new_nodes[neighbor_coords])

        # Add connections to the current node
        node.add_connection(neighbors)

    # Add VTU objects to the coordinates dictionary
    for vtu in vtu_objects:
        coordinates[vtu.id] = vtu

    # Add other nodes to the coordinates dictionary, ensuring no overlap
    for node in new_nodes.values():
        coordinates[node.id] = node

    # Create and return the 3D Map object
    return Map(lanes_nums=lanes_nums, aisle_nums=len(aisle_positions), level_nums=level_nums, map_id=str(uuid4()), coordinates=coordinates)
