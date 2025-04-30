import re

def guess_tag_type(script: str) -> str:
    match = re.search(r'<script[^>]*>(.*?)</script>', script, re.DOTALL)
    if not match:
        return "empty"

    js_code = match.group(1).strip()
    tag_type = []
    
    if 'tlz.px' in js_code:
        tag_type.append('px')
    
    if '.js' in js_code or 'tlz.js' in js_code:
        tag_type.append('js')
        
    return ' | '.join(tag_type)