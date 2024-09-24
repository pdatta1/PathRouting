import pygame
import time  

from mapp.algo.algo_types.map_types import Map, Node, Coords 
from mapp.mapper.map_types.mapper_objects_types import MapEntity
from mapp.mapper.map_types.mapper_types import Entity
from typing import List, Dict

from mapp.mapper.mappers.dynamic_mapper import DynamicMapper
from mapp.algo.routings.a_star import AstarRouting

from visuals.node_visualization import (
    AisleDrawStrategy,
    LaneDrawStrategy,
    VTUDrawStrategy,
    DrawStrategyFactory,
)
from visuals.entity_visualization import (
    VTUEntityDrawStrategy,
    RobotEntityDrawStrategy,
    PalletEntityDrawStrategy,
    MapEntityDrawFactory,
)
from visuals.simulation import SimulationManager


class VisualizationManager:
    def __init__(self, screen_width: int, screen_height: int, scale: int):
        pygame.init()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode((screen_width, screen_height))
        self.clock = pygame.time.Clock()
        self.scale = scale
        self.running = True

        pygame.display.set_caption('3D Map Visualization')

        self.map_component_factory = DrawStrategyFactory()
        self.entity_component_factory = MapEntityDrawFactory()
        self.load_map_components()
        self.load_entity_components()

    def load_map_components(self) -> None: 
        if self.map_component_factory: 
            self.map_component_factory.register_draw_strategy('aisle', AisleDrawStrategy())
            self.map_component_factory.register_draw_strategy('lane', LaneDrawStrategy())
            self.map_component_factory.register_draw_strategy('vtu', VTUDrawStrategy())

    def load_entity_components(self) -> None: 
        if self.entity_component_factory: 
            self.entity_component_factory.register_draw_strategy('robot', RobotEntityDrawStrategy())  # Uses robot icon
            self.entity_component_factory.register_draw_strategy('vtu', VTUEntityDrawStrategy())
            self.entity_component_factory.register_draw_strategy('pallet', PalletEntityDrawStrategy())

    def calculate_center_offset(self, map_obj: Map):
        max_x = map_obj.lanes_nums * self.scale
        max_y = map_obj.aisle_nums * self.scale
        x_offset = (self.screen_width - max_x) // 2
        y_offset = (self.screen_height - max_y) // 2
        return x_offset, y_offset

    def draw_node(self, node: Node, x_offset: int, y_offset: int):
        strategy = self.map_component_factory.get_draw_strategy(node.node_type)
        if strategy:
            strategy.draw(self.screen, node, x_offset, y_offset, self.scale)

        # Draw text with coordinates
        font = pygame.font.Font(None, 12)  # Adjust font size as needed
        text = f"({node.coords.x}, {node.coords.y}, {node.coords.z})"
        text_surface = font.render(text, True, (0, 0, 0))  # Black text
        text_rect = text_surface.get_rect()
        text_rect.center = (x_offset + node.coords.x * self.scale + self.scale // 2, y_offset + node.coords.y * self.scale + self.scale // 2)
        self.screen.blit(text_surface, text_rect)

    def draw_entity(self, entity: MapEntity, x_offset: float, y_offset: float): 
        entity_strategy = self.entity_component_factory.get_draw_strategy(entity.entity_type)
        if entity_strategy: 
            entity_strategy.draw(self.screen, entity, x_offset, y_offset, self.scale)

    def visualize(
        self, 
        simulation: SimulationManager, 
    ):
        x_offset, y_offset = self.calculate_center_offset(simulation.mapper.entity.map)


        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.screen.fill((255, 255, 255))

            # Draw all map nodes
            for node in simulation.mapper.entity.map.coordinates.values():
                self.draw_node(node, x_offset, y_offset)

            # Draw all entities
            for entity_list in simulation.mapper.entity.map_entities.values():
                for entity in entity_list:
                    self.draw_entity(entity, x_offset, y_offset)
            
            simulation.run_simulation()
                        
            self.draw_entity(entity, x_offset, y_offset)
            pygame.display.flip()
            self.clock.tick(2)  # Adjust the speed (2 frames per second)

        pygame.quit()

