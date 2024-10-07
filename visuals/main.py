import asyncio
from visualization_manager import VisualizationManager


from mapp.tester.builders_testers.generate_map import generate_map
from mapp.mapper.mappers.dynamic_mapper import DynamicMapper
from mapp.algo.routings.a_star import AstarRouting
from mapp.mapper.map_types.mapper_types import Entity 
from mapp.algo.algo_types.map_types import Map, Node, Coords 

from visuals.simulation import SimulationManager


async def main():
    grid_map = generate_map(10, 1)
    entity_manager = Entity(grid_map)
    mapper = DynamicMapper(entity=entity_manager)
    visualizer = VisualizationManager(1200, 800, 50)
    simulation = SimulationManager(mapper)

    async with mapper:
        mapper.register_algorithm('a_star', AstarRouting(mapper.entity))
        mapper.entity.insert_entity('Robot1', 'robot', grid_map.get_node_by_coords(2, 3, 0))
        mapper.entity.insert_entity('Robot2', 'robot', grid_map.get_node_by_coords(0, 3, 0))

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

        try:
            simulation.add_simulation('Robot1', 'robot', 'a_star', Coords(7, 0, 0))
            simulation.add_simulation('Robot2', 'robot', 'a_star', Coords(0, 8, 0))
            # simulation.add_simulation('Robot2', 'robot', 'a_star', Coords(4, 8, 0))
        except Exception as exc: 
            print(exc)
        finally:
            visualizer.visualize(simulation)

        

if __name__ == '__main__':
    asyncio.run(main())
