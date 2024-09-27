from typing import * 

from dataclasses import dataclass, field, MISSING

from mapp.mapper.map_types.mapper_types import * 
from mapp.mapper.map_types.mapper_objects_types import *

from mapp.algo.algo_types.map_types import Map, Coords


@dataclass
class Entity: 
    map: Map = field(default=MISSING)
    map_entities: Dict[str, List[MapEntity]] = field(default_factory=dict)

    def check_entity_duplicates(self, arr: List[MapEntity], id: str) -> bool: 
        for x in arr: 
            if x.entity_id == id: 
                return True 
        return False 

    def insert_entity(
        self, 
        entity_id: str, 
        entity_type: str,
        entity_loc: Node,
        static: bool = True,
    ) -> None: 
        map_entity_object = MapEntity(
            entity_id=entity_id,
            entity_type=entity_type,
            entity_loc=entity_loc,
            static=static
        )
        if entity_type in self.map_entities: 
            if not self.check_entity_duplicates(self.map_entities[entity_type], entity_id):
                self.map_entities[entity_type].append(map_entity_object)
        else: 
            self.map_entities[entity_type] = [map_entity_object]
            
    def remove_entity(self, entity_id: str, entity_type: str) -> None: 
        for key, value in self.map_entities.items(): 
            if key == entity_type: 
                for entity_to_remove in value: 
                    if entity_to_remove.entity_id == entity_id: 
                        value.remove(entity_to_remove)

    def get_entity(self, entity_id: str, entity_type: str) -> Union[MapEntity, None]: 
        for key, value in self.map_entities.items(): 
            if key == entity_type: 
                for entity in value: 
                    if entity.entity_id == entity_id: 
                        return entity 
            
    def get_all_entities(self) -> Dict[str, List[MapEntity]] : 
        return self.map_entities
