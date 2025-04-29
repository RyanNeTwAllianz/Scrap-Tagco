import re
from typing import List

def guess_dupe_x1(script: str) -> str:
    results = []
    
    matches = re.findall(r'<script[^>]*>(.*?)</script>', script, re.DOTALL)
    if not matches:
        return ''

    for js_code in matches:
        calls = re.findall(r'tlz\.x1\s*\((.*?)\)', js_code, re.DOTALL)
        for call in calls:
            param1s_raw = call.split(',')[0]
            if 'tlz' not in param1s_raw:
                results.append('none')
            else:
                for p in param1s_raw.split('+'):
                    if 'tlz' in p:
                        param = p.replace('tlz', "").replace('_', '').replace('.', ' ').replace("'", "")
                        param = param.strip()
                        results.append(param)
    return ' | '.join(results)