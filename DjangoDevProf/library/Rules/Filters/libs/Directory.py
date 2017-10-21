__author__ = 'freddy'


base_path = ""
'''
filepath : The directory that should be searched
directory: The filepath
'''

#("/a/b/c/d/e", "/d/e")
def match_directory(file_directory, path_to_match):
    global base_path
    rel_filepath = file_directory.replace(base_path, "")

    if(path_to_match[0] == "/"):
        path_to_match = path_to_match[1:]

    file_dir = rel_filepath.split("/")
    directory_dir = path_to_match.split("/")
    try:
      pos = file_dir.index(directory_dir[0])
    except ValueError:
        return False

    for i in range(0, len(directory_dir)):
        if directory_dir[i] == "":
            continue
        if(file_dir[pos + i] != directory_dir[i]):
            return False
    return True


def setup_basepath(base):
    global base_path
    base_path = base


def drop_filename(str):
    file_dir = str.split("/")
    if file_dir[-1].find(".") != -1:
        #print file_dir[-1]
        return '/'.join(file_dir[0:-1])

    return str
