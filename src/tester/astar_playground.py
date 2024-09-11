
from generate_map import generate_map

from algo.routings.a_star import AstarRouting

def main(): 
    
    grid_map = generate_map(20, 20)
    start_node = grid_map.get_node_by_coords(x=0, y=0)
    end_node = grid_map.get_node_by_coords(x=10, y=4)

    print(f"start node: {start_node}")
    print(f"end node: {end_node}")

    print("--------------------------------------------------------------------------")

    astar = AstarRouting(grid_map)
    path = astar.find_path(start_node, end_node)

    for node in path: 
        print(node)


if __name__ == '__main__': 
    main() 