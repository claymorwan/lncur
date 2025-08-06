import os, pathlib

# Get working directory
str_dir = pathlib.Path().resolve()

def make(name):
    index_content = f"""[Icon Theme]
Name={name}
Comment=Insert description here
Inherits=breeze_cursors"""
    
    # Make the directories
    theme_dir_path = f"{str_dir}/{name}"
    os.mkdir(theme_dir_path)
    os.mkdir(f"{theme_dir_path}/cursors")

    # Make index.theme file and write content
    index_file = open(f"{theme_dir_path}/index.theme", "w")
    index_file.write(index_content)
    index_file.close()
