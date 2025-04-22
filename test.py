
from utils.GetTags import get_tags
from utils.GetContainers import get_containers
from utils.ConvertToCsv import convert_to_csv

containers = get_containers()
tags = get_tags(containers)
convert_to_csv(tags)