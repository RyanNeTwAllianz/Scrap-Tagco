import pandas as pd # type: ignore
from datetime import datetime
from utils.types import CondensedTagType
from typing import List

def convert_to_csv(tags: List[CondensedTagType]) -> None:
    fileName = 'Tags_' + datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    
    df = pd.DataFrame(tags)
    df.to_csv(f'{fileName}.csv', index=False, sep=';', encoding='utf-8')
    
    print(f'File created : {fileName}.csv')