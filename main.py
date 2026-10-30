import os
import shutil
temp_folder = os.environ.get('TEMP')
contents = os.listdir(temp_folder)
for i in contents:
    path = os.path.join(temp_folder, i)
    try:
        if os.path.isfile(path):
            os.remove(path)
            print(f'Deleted file: {path}')
        elif os.path.isdir(path):
            shutil.rmtree(path)
            print(f'Deleted folder: {path}')
    except Exception as e:
        print(f'Failed to delete {path}')