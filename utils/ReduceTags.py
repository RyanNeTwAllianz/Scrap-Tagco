from utils.types import TagType, CondensedTagType, ContainerType
from utils.GuessToolFromContainerName import guess_tool_from_container_name
from utils.GuessEventType import guess_event_type
from utils.GuessTagType import guess_tag_type
from utils.GuessDupeX1 import guess_dupe_x1
from utils.GuessX1Time import guess_x1_time
from typing import List
import re

def simplify(tag: TagType, container: ContainerType) -> CondensedTagType:
    attrs = tag.get('attributes', {})
    
    container_number = re.search(r'\[(\d+)\]', container['name'])
    container_number_value = int(container_number.group(1)) if container_number else 0
    
    return {
        'container_number': container_number_value,
        'container_name': container['name'],
        'tools': guess_tool_from_container_name(attrs.get('name')),
        'comment': '',
        'tag_name': attrs.get('name'),
        'event_type': guess_event_type(attrs.get('name')),
        'tag_type': guess_tag_type(attrs.get('tag_code')),
        'dupe_x1_time': guess_x1_time(attrs.get('tag_code')),
        'dupe_x1_param': guess_dupe_x1(attrs.get('tag_code')),
        'disabled': 'Disactivated' if attrs.get('disabled') else 'Activated',
        'order': attrs.get('order'),
        'script': attrs.get('tag_code'),
        'tag_id': tag.get('id'),
        'container_id': attrs.get('container_id')
    }

def reduce_tags(tags: List[TagType] ,containers: List[ContainerType]) -> List[CondensedTagType]:
    new_tags = []
    for tag in tags:
        container_id = tag.get('attributes').get('container_id')
        container =  next((d for d in containers if d['id'] == str(container_id)), None)
        if container:
            new_tags.append(simplify(tag, container))
    
    new_tags.sort(key=lambda obj: obj['order'])
    new_tags.sort(key=lambda obj: obj['container_name'])
    new_tags.sort(key=lambda obj: obj['container_number'])
    print('Tags reduced')
    return new_tags