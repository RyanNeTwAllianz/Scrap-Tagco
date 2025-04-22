import pandas as pd # type: ignore
from datetime import datetime

def convert_to_csv(tags):
    fileName = 'Tags_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    df = pd.DataFrame(tags)
    df.to_csv(f'{fileName}.csv', index=False, sep=';', encoding='utf-8')
    print(f'Fichier créé : {fileName}.csv')