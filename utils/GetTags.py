from utils.Get import get 
from typing import List, Dict
import re

def simplify(tag, container):
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

def get_tags (containers: List[Dict[str, str]]):
    tags = []
    res = get('tms/web-tags')
    if res.status_code == 200:
        response = res.json()
        for data in response['data']:
            container_id = data.get('attributes').get('container_id')
            container =  next((d for d in containers if d['id'] == str(container_id)), None)
            if container:
                tags.append(simplify(data, container))
            tags.sort(key=lambda obj: obj['order'])
            tags.sort(key=lambda obj: obj['container_number'])
        return tags
    else:
        print(f'Erreur {res.status_code} : {res.text}')
        return None