import random
from typing import Dict, List 
from uuid import uuid4
from algo_types.map_types import Map, Node, Coords

# Function to generate a 3D map
def generate_map(lanes_nums: int, aisle_nums: int, level_nums: int) -> Map:
    coordinates: Dict[str, Node] = {}
    vtu_objects: List[Node] = [] 
    new_nodes: List[Node] = [] 

    for x in range(level_nums):
        vtu_object = Node(coords=Coords(x=6, y=8, z=x), node_type="vtu", id=str(uuid4()))
        vtu_objects.append(vtu_object)

    for x in range(lanes_nums):
        for y in range(aisle_nums):
            for z in range(level_nums):
                # Randomly assign the node type (Aisle or Lane)
                node_type = random.choice(["aisle", "lane", ])
                
                if not any(coordinate.coords.x == x and coordinate.coords.y == y and coordinate.coords.z == z for coordinate in vtu_objects):
                    node = Node(coords=Coords(x=x, y=y, z=z), node_type=node_type, id=str(uuid4()))
                    new_nodes.append(node)

    for vtu in vtu_objects: 
        coordinates[vtu.id] = vtu   
    
    for node in new_nodes: 
        coordinates[node.id] = node 
                    
    # Create and return the 3D Map object

    return Map(lanes_nums=lanes_nums, aisle_nums=aisle_nums, level_nums=level_nums, map_id=str(uuid4()), coordinates=coordinates)


# TODO avoid adding duplicate nodes