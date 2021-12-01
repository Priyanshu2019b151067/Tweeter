import os
import random
from posixpath import basename
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(basename)
    return name,ext
    
def upload_image_path(instance,filename):
    new_filename = random.randint(1,3910209312)
    name,ext = get_filename_ext(filename)
    final_filename = f'{new_filename}{ext}'
    return f'products/{new_filename}/{final_filename}'