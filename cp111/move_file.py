import os

from_dir="c:/Users/ADMIN/Download"
to_dir="c:/whiteHat/"
list_of_files=os.listdir(from_dir)

for file_name in list_of_files:
    name,extention=os.path.splittext(file_name)