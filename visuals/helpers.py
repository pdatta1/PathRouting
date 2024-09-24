
import os 
import visuals 

from typing import Any 

def get_directory(
    file_path: str, 
    file_module: Any
) -> str: 
    file_module: str = os.path.dirname(file_module.__file__)
    file_dir: str = os.path.join(file_module, file_path)
    return file_dir