
from typing import Dict, List, Union, Tuple
from dataclasses import dataclass

from mapp.tester.builders_testers.generate_map import generate_map
from mapp.algo.routings.a_star import AstarRouting, Entity, Map, Node, Path
from mapp.mapper.map_types.mapper_objects_types import MapEntity
from mapp.mapper.mappers.dynamic_mapper import DynamicMapper

import random 

"""
grid_map = generate_map(10, 1)
entity = Entity(map=map, map_entities=dict)
mapper = DynamicMapper(entity=entity)
mapper.register_algorithm('a_star', AstarRouting(mapper.entity))
mapper.entity.insert_entity('Robot1', 'robot', grid_map.get_node_by_coords(2, 3, 0))
# mapper.entity.insert_entity('Robot2', 'robot', grid_map.get_node_by_coords(0, 3, 0))
# mapper.entity.insert_entity('VTU1', 'vtu', grid_map.get_node_by_coords(6, 3, 0))
mapper.entity.insert_entity('Pallet1', 'pallet', grid_map.get_node_by_coords(5, 4, 0))
mapper.entity.insert_entity('Pallet2', 'pallet', grid_map.get_node_by_coords(7, 4, 0))
mapper.entity.insert_entity('Pallet3', 'pallet', grid_map.get_node_by_coords(7, 5, 0))
mapper.entity.insert_entity('Pallet4', 'pallet', grid_map.get_node_by_coords(4, 5, 0))
mapper.entity.insert_entity('Pallet5', 'pallet', grid_map.get_node_by_coords(0, 4, 0))
mapper.entity.insert_entity('Pallet6', 'pallet', grid_map.get_node_by_coords(1, 4, 0))
mapper.entity.insert_entity('Pallet7', 'pallet', grid_map.get_node_by_coords(2, 4, 0))
mapper.entity.insert_entity('Pallet8', 'pallet', grid_map.get_node_by_coords(3, 4, 0))
mapper.entity.insert_entity('Pallet9', 'pallet', grid_map.get_node_by_coords(6, 5, 0))


"""

@dataclass
class MapEntityConfig:
    quantity: int 
    static: bool


class AStarPlayground: 
    def __init__(
        self, 
        entities_config: Dict[str, int]
    ) -> None: 
        self.mapper = self.construct_mapper() 

        self.register_algorithms() 
        self.load_map_entities(entities_config) 

    def construct_mapper(self) -> DynamicMapper: 
        grid_map = generate_map(10, 1)
        entity = Entity(map=grid_map)
        mapper = DynamicMapper(entity=entity)
        return mapper 
    
    def register_algorithms(self) -> None:
        self.mapper.register_algorithm('a_star', AstarRouting(self.mapper.entity))

    def get_random_node(self) -> Union[Node, None]: 
        return random.choice(list(self.mapper.entity.map.coordinates.values()))
        
    def load_map_entities(
        self,
        attrs: Dict[str, MapEntityConfig]
    ) -> None: 
        
        for key, value in attrs.items(): 
            if value.quantity <= len(self.mapper.entity.map.coordinates):
                for x in range(1, value.quantity + 1): 
                    random_node: Union[Node, None] = self.get_random_node()
                    if random_node:
                        self.mapper.entity.insert_entity(f"{key}_{x}", key, random_node, value.static)        
        
    def get_path_for_entity(self, entity_id: str, entity_type: str, target_coords: Tuple[int, int, int]) -> None: 
        entity: Union[MapEntity, None] = self.mapper.entity.get_entity(entity_id, entity_type)
        if not entity: 
            raise Exception(f'Entity {entity_id} not found in {entity_type} Type')
        
        target_node: Union[Node, None] = self.mapper.entity.map.get_node_by_coords(target_coords[0], target_coords[1], target_coords[2])
        if not target_node:
            raise Exception(f'Cannot find Location x={target_coords[0]}, y={target_coords[1]}, z={target_coords[2]} in map')
        
        path: Path = self.mapper.get_algorithm('a_star').find_path(entity.entity_loc, target_node)
        if path: 
            for x in range(len(path.nodes) - 1): 
                print(f"{path.nodes[x].coords} ---> {path.nodes[x + 1].coords}")

            obstacles: List[MapEntity] = self.get_obstacle_for_path(entity, path)
            # print("All Entities")
            # all_entities = self.mapper.entity.get_all_entities()
            # for key, value in all_entities.items(): 
            #     for ent in value: 
            #         print(ent.entity_loc.id)
            # print('End of All Entities')
            for obstacle in obstacles: 
                # print(f'Obstacle Detected [{obstacle.entity_id}] at {obstacle.entity_loc.coords}')
                print(f'obstacle detected: {obstacle.entity_id} at {obstacle.entity_loc.coords}')

    def get_obstacle_for_path(self, entity: MapEntity, path: Path) -> List[MapEntity]: 
        obstacles: List[MapEntity] = [] 

        for node in path.obstacles: 
            matched_entity: Union[MapEntity, None] = self.mapper.entity.get_entity_by_node(node, entity_type=entity.entity_type)
            if matched_entity: 
                obstacles.append(matched_entity)
        return obstacles

def main(): 
    entities_config: Dict[str, MapEntityConfig] = {
        "robot": MapEntityConfig(quantity=5, static=False),
        "pallet": MapEntityConfig(quantity=10, static=True),
    }
    playground = AStarPlayground(entities_config=entities_config)

    try: 
        playground.get_path_for_entity('robot_4', 'robot', (3, 7, 0))
    except Exception as exc: 
        print(f"Exception Occurred: {exc}")
    



if __name__ == '__main__': 
    main() 