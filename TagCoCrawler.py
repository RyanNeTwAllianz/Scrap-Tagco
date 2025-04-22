import requests # type: ignore
import pandas as pd # type: ignore
from datetime import datetime
import json

with open('env.json', 'r') as file:
    data = json.load(file)

siteId = data.get('siteId')
baseUrl = data.get('baseUrl')
headers = {
    'Content-Type': 'application/json',
    "Authorization": f"Bearer {data.get('token')}"
    }


def Simplify(tag):
    attrs = tag.get('attributes', {})
    return {
        'id': tag.get('id'),
        'container_id': attrs.get('container_id'),
        'tag_name': attrs.get('name'),
        'order': attrs.get('order'),
        'disabled': attrs.get('disabled'),
        'script': attrs.get('tag_code'),
    }

def GetTags():
    tags = []
    res = requests.get(f'{baseUrl}/{siteId}/tms/web-tags', headers=headers)
    if res.status_code == 200:
        response = res.json()
        for data in response['data']:
            tags.append(Simplify(data))
        return tags
    else:
        print(f'Erreur {res.status_code} : {res.text}')
        return None

def ConvertToCsv(tags):
    fileName = 'Tags_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    df = pd.DataFrame(tags)
    df.to_csv(f'{fileName}.csv', index=False, sep=';', encoding='utf-8')
    print(f'Fichier créé : {fileName}.csv')



#Main
tags = GetTags()
ConvertToCsv(tags)