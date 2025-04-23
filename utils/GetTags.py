from utils.Get import get 
from typing import List
from utils.types import TagType

def get_tags () -> List[TagType]:
    res = get('tms/web-tags')
    if res.status_code == 200:
        response = res.json()
        return response['data']
    else:
        raise Exception(f'Error {res.status_code} : {res.text}')