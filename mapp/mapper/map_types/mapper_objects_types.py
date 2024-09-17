
from typing import * 

from dataclasses import dataclass, field, MISSING

@dataclass
class MapEntity: 
    entity_id: str = field(default=MISSING, compare=True)
    entity_type: str = field(default=MISSING)
