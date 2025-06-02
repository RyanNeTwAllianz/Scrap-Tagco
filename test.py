from utils.GetGlobalVars import get_global_vars
from utils.Get import get


def test () -> None:
  
  res = get(f'')

  response = res.json()
  print(response)
    
    


test()
