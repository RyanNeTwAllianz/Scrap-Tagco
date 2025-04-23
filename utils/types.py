from dataclasses import dataclass
from typing import Literal, List, TypedDict

@dataclass
class CondensedTagType():
    id: str
    container_id: str
    container_number: int
    container_name: str
    tag_name: str
    order: int
    disabled: bool
    script: str
    
@dataclass
class ContainerType():
    id: str
    name: str

@dataclass
class Attributes:
    name: str
    tag_code: str
    disabled: bool
    timeout: int
    position: int
    variables_mappings: List 
    
    
@dataclass
class TagType():
    type: Literal["tms/web-tags"]
    id: str
    attributes: Attributes
    

class Headers(TypedDict):
    Authorization: str
    __annotations__ = {
        'Content-Type': Literal['application/json']
    }       
    
@dataclass
class GlobalVars():
    siteId: int
    baseUrl: str
    headers : Headers