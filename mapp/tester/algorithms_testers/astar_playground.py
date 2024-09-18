
import random 
import time 

from tester.builders_testers.generate_map import generate_map
from algo.routings.a_star import AstarRouting
from mapper.map_types.mapper_interfaces import MapNodeTypes

grid_map = generate_map(50, 50, 10)
astar = AstarRouting(grid_map)

def test_generate_paths(): 
    
    start_node = grid_map.get_node_by_coords(x=0, y=0, z=0)
    end_node = grid_map.get_node_by_coords(x=10, y=8, z=5)

    print("Map Attributes: ")
    print(f"Aisles: {grid_map.aisle_nums} | Lanes: {grid_map.lanes_nums}")
    
    print("--------------------------------------------------------------------------")

    print(f"start node: {start_node}")
    print(f"end node: {end_node}")

    print("--------------------------------------------------------------------------")

    path = astar.find_path_on_same_level(start_node, end_node)

    print(f"nodes to travel through: {len(path.nodes)}")
    print(f"computation time: {path.computation_time:.6f} seconds")
    print("--------------------------------------------------------------------------")

    for node in path.nodes: 
        print(node)


def test_get_all_vtus(): 
    vtus = grid_map.get_nodes_by_types(MapNodeTypes.VTU.value)
    print("All VTUS: ")
    for vtu in vtus: 
        print(vtu)


def test_find_closest_vtu(): 

    start_node = grid_map.get_node_by_coords(4, 8, 0)
    closest_vtu = astar.find_closest_vtu(start_node)

    print("--------------------------------------------------------------------------")

    print(f"start node: {start_node}")
    print(f"end node: {closest_vtu}")

    path = astar.find_path_on_same_level(start_node, closest_vtu)
    print(f"nodes to travel through: {len(path.nodes)}")
    print(f"computation time: {path.computation_time:.6f} seconds")
    print("--------------------------------------------------------------------------")


    for node in path.nodes: 
        print(node)


def test_route_from_vtu_to_path(): 
    vtu_nodes = grid_map.get_nodes_by_types(MapNodeTypes.VTU.value)
    print(f"VTU length: {len(vtu_nodes)}")
    if len(vtu_nodes) > 0: 
        vtu_node = vtu_nodes[0]
        target_node = grid_map.get_node_by_coords(10, 8, vtu_node.coords.z)

        print("--------------------------------------------------------------------------")

        print(f"start node: {vtu_node}")
        print(f"end node: {target_node}")

        path = astar.find_path_on_same_level(vtu_node, target_node)
        print(f"nodes to travel through: {len(path.nodes)}")
        print(f"computation time: {path.computation_time:.6f} seconds")
        print("--------------------------------------------------------------------------")


        for node in path.nodes: 
            print(node)




if __name__ == '__main__': 
    test_route_from_vtu_to_path() 