
from mapper.mappers.dynamic_mapper import DynamicMapper
from algo.routings.a_star import AstarRouting

from mapper.map_types.mapper_types import Entity 
from tester.builders_testers.generate_map import generate_map

import asyncio 

async def main(): 
    grid_map = generate_map(50, 50, 10)
    entity = Entity(map=grid_map)
    mapper = DynamicMapper(entity=entity) 
    async with mapper: 
        mapper.register_algorithm('a_star', AstarRouting(mapper.entity.map))
        mapper.entity.insert_entity('Robot1', 'Robot', grid_map.get_node_by_coords(7, 3, 0))
        mapper.entity.insert_entity('Robot2', 'Robot', grid_map.get_node_by_coords(8, 3, 0))
        mapper.entity.insert_entity('VTU1', 'VTU', grid_map.get_node_by_coords(6, 8, 0))
        mapper.entity.insert_entity('Pallet1', 'Pallet', grid_map.get_node_by_coords(9, 3, 0))

        
        routing: AstarRouting = mapper.get_algorithm('a_star')

        robot_1 = mapper.entity.get_entity('Robot1', 'Robot')
        path = routing.find_path_on_same_level(robot_1.entity_loc, mapper.entity.map.get_node_by_coords(5, 8, 0))
        for node in path.nodes: 
            print(node)


if __name__ == '__main__': 
    asyncio.run(main())