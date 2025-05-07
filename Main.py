from utils.GetTags import get_tags
from utils.GetContainers import get_containers
from utils.ConvertToCsv import convert_to_csv
from utils.ReduceTags import reduce_tags

def main () -> None:
    containers = get_containers()
    tags = get_tags()
    new_tags = reduce_tags(tags, containers)
    convert_to_csv(new_tags)
    
    
main()