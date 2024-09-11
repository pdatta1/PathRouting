import random
from typing import Dict
from uuid import uuid4

from base.routing_base import Map, Node, Coords

# Function to generate a map
def generate_map(lanes_nums: int, aisle_nums: int) -> Map:
    coordinates: Dict[str, Node] = {}

    for x in range(lanes_nums):
        for y in range(aisle_nums):
            # Randomly assign the node type
            node_type = random.choice(["Aisle", "Lane"])
            
            # Create a Node with unique coordinates and ID
            node = Node(coords=Coords(x=x, y=y), node_type=node_type, id=str(uuid4()))
            
            # Store the node in the coordinates dictionary using its ID
            coordinates[node.id] = node

    # Create the Map object with generated coordinates
    return Map(lanes_nums=lanes_nums, aisle_nums=aisle_nums, map_id=str(uuid4()), coordinates=coordinates)

