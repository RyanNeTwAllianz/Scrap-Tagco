import re

def guess_tag_type(script: str) -> str:
    match = re.search(r'<script[^>]*>(.*?)</script>', script, re.DOTALL)
    if not match:
        return "empty"

    js_code = match.group(1).strip()
    
    if 'tlz.px' in js_code:
        other_code = re.sub(r'tlz\.px.*?;', '', js_code)
        if other_code.strip():
            return "js | px"
        else:
            return "px"
    
    return "js"