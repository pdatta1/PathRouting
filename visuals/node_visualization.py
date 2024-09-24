from abc import ABC, abstractmethod
from typing import Dict   
from pygame import (
    draw, 
    Rect,
    Surface
)
from mapp.algo.algo_types.map_types import Node 


class MapNodeDrawStrategy(ABC):
    @abstractmethod
    def draw(
        self, 
        screen: Surface, 
        node: Node, 
        x_offset: float, 
        y_offset: float,
        scale: float
    ):
        pass

class AisleDrawStrategy(MapNodeDrawStrategy):
    def draw(self, screen, node, x_offset, y_offset, scale):
        x, y = node.coords.x * scale, node.coords.y * scale
        color = (0, 255, 0)
        rect_width, rect_height = scale // 2, scale // 2
        draw.rect(screen, color, Rect(x + x_offset - rect_width // 2, y + y_offset - rect_height // 2, rect_width, rect_height))

class LaneDrawStrategy(MapNodeDrawStrategy):
    def draw(self, screen, node, x_offset, y_offset, scale):
        x, y = node.coords.x * scale, node.coords.y * scale
        color = (0, 0, 255)
        draw.circle(screen, color, (x + x_offset, y + y_offset), 10)

class VTUDrawStrategy(MapNodeDrawStrategy):
    def draw(self, screen, node, x_offset, y_offset, scale):
        x, y = node.coords.x * scale, node.coords.y * scale
        color = (255, 0, 0)
        draw.circle(screen, color, (x + x_offset, y + y_offset), 10)


# Factory for creating draw strategies
class DrawStrategyFactory:
    def __init__(self) -> None: 
        self.draw_factory: Dict[str, MapNodeDrawStrategy] = {} 
    

    def register_draw_strategy(self, draw_name: str, draw: MapNodeDrawStrategy) -> None: 
        self.draw_factory[draw_name] = draw

    def get_draw_strategy(self, draw_name: str) -> MapNodeDrawStrategy: 
        return self.draw_factory[draw_name]
    


