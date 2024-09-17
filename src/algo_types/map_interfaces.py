
from enum import Enum 

class MapNodeTypes(Enum): 
    Lane="lane"
    Aisle="aisle"
    VTU="vtu"

class MapEntityTypes(Enum): 
    Robot="robot"
    VTU="vtu"
    Blocker="blocker"
    Pallet="pallet"