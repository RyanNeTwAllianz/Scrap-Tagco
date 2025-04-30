import re

def guess_x1_time(script: str) -> str:
    matches = re.findall(r'<script[^>]*>(.*?)</script>', script, re.DOTALL)
    if not matches:
        return ''
    
    results = []
    for js_code in matches:
        js_code = js_code.replace(" ", "").replace("\n", "")

        calls = re.findall(r"tlz\.x1\('([^']*)'.*?function\(\)\{(.*?)\},'([^']*)'\);", js_code, re.DOTALL)
        x1time = re.findall(r"tlz.x1", js_code, re.DOTALL)

        for call in calls:
            results.append(call[2])
        
        for i in range(len(x1time) - len(calls)):
            results.append('page')

    return ' | '.join(results)