from utils.types import TagType, CondensedTagType, ContainerType
from typing import List
import re

def simplify(tag: TagType, container: ContainerType) -> CondensedTagType:
    attrs = tag.get('attributes', {})
    
    container_number = re.search(r'\[(\d+)\]', container['name'])
    container_number_value = int(container_number.group(1)) if container_number else 0
    
    return {
        'id': tag.get('id'),
        'container_id': attrs.get('container_id'),
        'container_number': container_number_value,
        'container_name': container['name'],
        'tag_name': attrs.get('name'),
        'order': attrs.get('order'),
        'disabled': attrs.get('disabled'),
        'script': attrs.get('tag_code'),
    }

def reduce_tags(tags: List[TagType] ,containers: List[ContainerType]) -> List[CondensedTagType]:
    new_tags = []
    for tag in tags:
        container_id = tag.get('attributes').get('container_id')
        container =  next((d for d in containers if d['id'] == str(container_id)), None)
        if container:
            new_tags.append(simplify(tag, container))
    
    new_tags.sort(key=lambda obj: obj['order'])
    new_tags.sort(key=lambda obj: obj['container_number'])
    return new_tags