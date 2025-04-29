from typing import List
from utils.Get import get
from utils.types import ContainerType

def get_containers() -> List[ContainerType]:
    containers = []
    res = get('sources')
    if res.status_code == 200:
        response = res.json()
        for data in response['data']:
            if  not data['attributes']['label'].startswith('x -'):
                containers.append(
                    {
                        'id': data['id'], 
                        'name': data['attributes']['label']
                    })
        print('Containers crawled')
        return containers
    else:
        raise Exception(f'Error {res.status_code} : {res.text}')