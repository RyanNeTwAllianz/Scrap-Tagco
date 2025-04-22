from typing import Dict, List
from utils.Get import get

def get_containers() -> List[Dict[str, str]]:
    containers = []
    res = get('sources')
    if res.status_code == 200:
        response = res.json()
        for data in response['data']:
            if  "x -" not in data['attributes']['label']:
                containers.append(
                    {
                        'id': data['id'], 
                        'name': data['attributes']['label']
                    })
        return containers
    else:
        print(f'Erreur {res.status_code} : {res.text}')
        return None