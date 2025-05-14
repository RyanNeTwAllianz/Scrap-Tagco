import os
import sys

def create_folder():
    root_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    exports_path = os.path.join(root_dir, 'exports')
    
    if not os.path.exists(exports_path):
        os.makedirs(exports_path)
        print(f"Folder created: {exports_path}")

    return exports_path
