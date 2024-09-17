Routing Single Floor Bias:
    - I want the find_path_on_same_level to route on the same level coordinate.
        - so an example will be, a raft receives an instructions to a specific path, let say the raft is on 
          level 1 and needs to go to level 5, we split the path, where we route in the same level(heading to the vtu),
          the raft travels via the vtu, upon exits, we route on level 5 to the target location.

    - I want to be able to add objects in the map on a node
        - VTUs
        - blocks 
        - robots
        - pallets
        - etc