from utils.GetTags import get_tags
from utils.GetContainers import get_containers
from utils.ConvertToCsv import convert_to_csv
from utils.ReduceTags import reduce_tags
from utils.CreateFolder import create_folder

def main () -> None:
    #Crée le dossier "exports" s'il n'existe pas
    create_folder()
    
    #Récuperer les containers
    containers = get_containers()
    
    #Récuperer les Tags
    tags = get_tags()
    
    #Matcher les tags avec leur containers et construis l'ojet new_tag qui inclut toute les infos du csv finale
    new_tags = reduce_tags(tags, containers)
    
    #Convertie en CSV et le place dans le dossiers "exports"
    convert_to_csv(new_tags)
    
    
main()
