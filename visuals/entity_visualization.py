
from abc import abstractmethod, ABC
from typing import Dict 

from pygame import (
    draw, 
    image,
    transform,
    Rect,
    Surface,
)

from mapp.mapper.map_types.mapper_objects_types import MapEntity


class MapEntityDrawStrategy(ABC): 
    @abstractmethod
    def draw(
        self, 
        screen: Surface,
        entity: MapEntity,
        x_offset: float, 
        y_offset: float,
        scale: float
    ): 
        ...


class RobotEntityDrawStrategy(MapEntityDrawStrategy):
    def __init__(self):
        # Load and scale the robot icon
        self.robot_icon = image.load('visuals/assets/images/robot.svg')  # Path to your image
        self.robot_icon = transform.scale(self.robot_icon, (20, 20))  # Adjust size if needed

    def draw(
        self,
        screen: Surface,
        entity: MapEntity,
        x_offset: float,
        y_offset: float,
        scale: float
    ):
        # Calculate robot position
        x: float = entity.entity_loc.coords.x * scale
        y: float = entity.entity_loc.coords.y * scale
        
        # Blit (draw) the robot icon at the calculated position
        screen.blit(self.robot_icon, (x + x_offset - self.robot_icon.get_width() // 2, 
                                      y + y_offset - self.robot_icon.get_height() // 2))


class VTUEntityDrawStrategy(MapEntityDrawStrategy):
    def __init__(self):
        # Load and scale the robot icon
        self.robot_icon = image.load('visuals/assets/images/vtu.svg')  # Path to your image
        self.robot_icon = transform.scale(self.robot_icon, (20, 20))  # Adjust size if needed

    def draw(
        self,
        screen: Surface,
        entity: MapEntity,
        x_offset: float,
        y_offset: float,
        scale: float
    ):
        # Calculate robot position
        x: float = entity.entity_loc.coords.x * scale
        y: float = entity.entity_loc.coords.y * scale
        
        # Blit (draw) the robot icon at the calculated position
        screen.blit(self.robot_icon, (x + x_offset - self.robot_icon.get_width() // 2, 
                                      y + y_offset - self.robot_icon.get_height() // 2))


class PalletEntityDrawStrategy(MapEntityDrawStrategy):
    def __init__(self):
        # Load and scale the robot icon
        self.robot_icon = image.load('visuals/assets/images/pallet.svg')  # Path to your image
        self.robot_icon = transform.scale(self.robot_icon, (20, 20))  # Adjust size if needed

    def draw(
        self,
        screen: Surface,
        entity: MapEntity,
        x_offset: float,
        y_offset: float,
        scale: float
    ):
        # Calculate robot position
        x: float = entity.entity_loc.coords.x * scale
        y: float = entity.entity_loc.coords.y * scale
        
        # Blit (draw) the robot icon at the calculated position
        screen.blit(self.robot_icon, (x + x_offset - self.robot_icon.get_width() // 2, 
                                      y + y_offset - self.robot_icon.get_height() // 2))

class MapEntityDrawFactory: 
    def __init__(self) -> None:
        self.draw_factory: Dict[str, MapEntityDrawStrategy] = {} 

    def register_draw_strategy(self, draw_name: str, draw: MapEntityDrawStrategy) -> None: 
        self.draw_factory[draw_name] = draw 

    def get_draw_strategy(self, draw_name: str) -> MapEntityDrawStrategy: 
        return self.draw_factory[draw_name]
        