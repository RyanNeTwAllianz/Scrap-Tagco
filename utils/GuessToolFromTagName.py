from utils.enums import ToolEnum

def guess_tool_from_tag_name(tag_name: str) -> str :
    tools = tag_name.split('-')[0]
    tools = [tools] if ',' not in tools else tools.split(',')
        
    t = []    
    tools_enum = list(set(item.value.lower() for item in ToolEnum))
    
    for tool in tools:
        tool = tool.strip().lower()
        tool = tool if ' ' not in tool else tool.split(' ')[0]
        
        if tool in tools_enum:
            tool = 'facebook' if tool == 'fb' else tool
            tool = 'weedo it' if tool == 'weedo' else tool
            t.append(tool)
    
    return ' | '.join(t)