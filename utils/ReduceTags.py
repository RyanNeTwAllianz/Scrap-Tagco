from utils.types import TagType, CondensedTagType, ContainerType
from utils.GuessToolFromTagName import guess_tool_from_tag_name
from utils.GuessEventType import guess_event_type
from utils.GuessTagType import guess_tag_type
from utils.GuessDupeX1 import guess_dupe_x1
from utils.GuessX1Time import guess_x1_time
from utils.GetContainerNumberFromContainerName import get_container_number_from_container_name
from typing import List
from utils.DupeKey import dupe_key

#
def simplify(tag: TagType, container: ContainerType) -> CondensedTagType:
    attrs = tag.get('attributes', {})
    script = attrs.get('tag_code')
    tool = guess_tool_from_tag_name(attrs.get('name'))
    
    return {
        'container_number': get_container_number_from_container_name(container),
        'container_name': container['name'],
        'tool': tool,
        'comment': '',
        'tag_name': attrs.get('name'),
        'event_type': guess_event_type(attrs.get('name')),
        'dupe_key': dupe_key(tool, script),
        'tag_type': guess_tag_type(script),
        'dupe_x1_time': guess_x1_time(script),
        'dupe_x1_param': guess_dupe_x1(script),
        'disabled': 'Disactivated' if attrs.get('disabled') else 'Activated',
        'order': attrs.get('order'),
        'script': script,
        'tag_id': tag.get('id'),
        'container_id': attrs.get('container_id')
    }

#Return la liste de tags qui sera affiché en excel par la suite
def reduce_tags(tags: List[TagType] ,containers: List[ContainerType]) -> List[CondensedTagType]:
    new_tags = []
    for tag in tags:
        container_id = tag.get('attributes').get('container_id')
        container = None
        #Trouver le container lié au tag
        for c in containers:
            if  str(get_container_number_from_container_name(c)) == str(container_id):
                container = c
        if container:
            #Ajoute a notre liste le tag traité par la fonction "simplify"
            new_tags.append(simplify(tag, container))
    
    #Ranger les tags dans l'ordre en premier par ordre d'éxecution puis par nom (Meme ordre que sur l'app TagCo)
    new_tags.sort(key=lambda obj: obj['order'])
    new_tags.sort(key=lambda obj: obj['container_name'])
    print('Tags reduced')
    return new_tags