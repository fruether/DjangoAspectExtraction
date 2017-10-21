__author__ = 'freddy'
import re

"""
Check if we find that regex somewhere in the filename
    return:
        True if yes
        False if not
"""
def match_filename_somewhere(str, base_path):
    regex = "(.)*" + str + "(.)*"
    return match_filename_regex(regex, base_path)

"""
Check if we find that regex in the middle of thefilename
    return:
        True if yes
        False if not
"""
def match_filename_middle(str, base_path):
    regex = "(.)+" + str + "(.)+"
    return match_filename_regex(regex, base_path)

"""
Check if a specific regex matched the filename
    return:
        True if yes
        False if not
"""
def match_filename_regex(regex, base_path):
    file_name = extract_filename(base_path)
    if re.match(regex, file_name):
        return True
    return False
"""
Check if a filename starts with a specific name
    return:
        True if yes
        False if not
"""
def match_filename_start(start, base_path):
    file_name = extract_filename(base_path)
    return file_name.startswith(start)

"""
Check if a filename ends with a specific name
    return:
        True if yes
        False if not
"""
def match_filename_suffix(suffix, base_path):
    return base_path.endswith(suffix)

"""
Check if a filename is identical to a string
    return:
        True if yes
        False if not
"""
def match_filename(name, base_path):
    return name == extract_filename(base_path)

"""
This function extracts a filename out of a path a/b/c/d.txt => t.txt
    path: The path
    return: The filename
"""
def extract_filename(path):
    components = path.split("/")
    return components[-1]


