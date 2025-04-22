import json
from typing import Tuple, Dict

def get_global_vars() -> Tuple[int, str, Dict[str, str]]:
    with open('./env.json', 'r') as file:
        data = json.load(file)

    siteId = data.get('siteId')
    baseUrl = data.get('baseUrl')
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {data.get('token')}"
        }
    
    return {'siteId': siteId, 'baseUrl': baseUrl, 'headers': headers}