import re
from utils.types import ContainerType

def get_container_number_from_container_name(container: ContainerType) -> int:
    container_number = re.search(r'\[(\d+)\]', container['name'])
    container_number_value = int(container_number.group(1)) if container_number else 0
    
    return container_number_value