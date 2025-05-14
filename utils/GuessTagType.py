import re

def guess_tag_type(script: str) -> str:
    match = re.search(r'<script[^>]*>(.*?)</script>', script, re.DOTALL)
    if not match:
        return "empty"
    
    js_guesses = ['.js', 'tlz.js', 'tlz.gt', 'tlz.fb', 'ttq.track', 'transaction:send', 'trackGoal', 'uetq.push', '_tfa.push', '__dot.push', 'tip.push', '__ISDK.push']

    js_code = match.group(1).strip()
    tag_type = []
    
    if 'tlz.px' in js_code:
        tag_type.append('px')
    
    if any(j in js_code for j in js_guesses):
        tag_type.append('js')
        
    return ' | '.join(tag_type)