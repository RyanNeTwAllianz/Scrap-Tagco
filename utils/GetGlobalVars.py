import json
from utils.types import GlobalVars 

def get_global_vars() -> GlobalVars:
    with open('./env.json', 'r') as file:
        data = json.load(file)

    siteId = data.get('siteId')
    baseUrl = data.get('baseUrl')
    token = data.get('token')
    headers = {
        'Content-Type': 'application/json',
        "Authorization": f"Bearer {token}"
        }
    
    if not siteId or not token or not baseUrl:
        raise Exception('Can t get env vars, check README')
            
    return {'siteId': siteId, 'baseUrl': baseUrl, 'headers': headers}