import re

def guess_var_from_tool(tool: str) -> str:

    vars = {
        'cm': 'session_id:',
        'aw': 'transaction_id:',
        'facebook': 'eventID:',
        'weedo it': '&idr=',
        'ocead': '&leadid=',
        'oceads': '&leadid=',
        'powerspace': 'clid:',
        'adrenalead' :  '_nAdztr.push([setTransactionId,',
        'cs': 'id:',
        'wz': 'orderid:',
        'taboola': 'orderid:'
    }
        
    return vars.get(tool, '')



def dupe_key(tool: str, script: str) -> str:
    js_code = script.replace("\n", "").replace('"', "").replace("'", "")
    var = guess_var_from_tool(tool)
    
    if var:
        #regex = re.findall(f'{re.escape(var)}[^,{"}"}/\\]]*', js_code)
        regex = re.findall(f'{re.escape(var)}[^,{{"}}\\]]*(?=//|[^/])', js_code)
        dupes = [r for r in regex if r and r.strip() != var]
        return ' | '.join(dupes)

    
    return ''