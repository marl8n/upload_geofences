from os import listdir
from os.path import isfile

def get_dir_filnames(dir_name):
    filenames = [f'{dir_name}/{file}' for file in listdir(dir_name) if isfile(f'{dir_name}/{file}')]
    return filenames