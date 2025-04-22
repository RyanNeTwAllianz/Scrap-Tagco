from utils.GetGlobalVars import get_global_vars
import requests # type: ignore

global_vars = get_global_vars()
siteId, baseUrl, headers = global_vars["siteId"], global_vars["baseUrl"], global_vars["headers"]

def get(url: str) -> requests.Response:
    res = requests.get(f'{baseUrl}/{siteId}/{url}', headers=headers)
    return res