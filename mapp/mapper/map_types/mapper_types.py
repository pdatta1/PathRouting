from typing import * 

from dataclasses import dataclass, field, MISSING
from mapper.map_types.mapper_types import * 
from mapper.map_types.mapper_objects_types import *
from mapper.map_types.mapper_interfaces import MapEntityTypes

from algo.algo_types.map_types import Map 


@dataclass
class Entity: 
    map: Map = field(default=MISSING)
    entities: Dict[str, List[MapEntity]] = field(default_factory=dict)

    def check_entity_duplicates(self, arr: List[MapEntity], id: str) -> bool: 
        for x in arr: 
            if x.entity_id == id: 
                return True 
        return False 

    def insert_entity(self, entity_id: str, entity_type: str) -> None: 
        for key, value in self.entities.items(): 
            if key == entity_type: 
                if not self.check_entity_duplicates(value, entity_id):
                    value.append(
                        MapEntity(
                            entity_id=entity_id,
                            entity_type=entity_type
                        )
                    )


    def get_entity(self, entity_id: str, entity_type: str) -> Union[MapEntity, None]: 
        for key, value in self.entities.items(): 
            if key == entity_type: 
                for entity in value: 
                    if entity.entity_id == entity_id: 
                        return entity 
