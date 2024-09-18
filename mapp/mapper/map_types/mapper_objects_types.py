
from typing import * 

from dataclasses import dataclass, field, MISSING

from algo.algo_types.map_types import Node

@dataclass
class MapEntity: 
    entity_id: str = field(default=MISSING, compare=True)
    entity_type: str = field(default=MISSING)
    entity_loc: Node = field(default=MISSING)
