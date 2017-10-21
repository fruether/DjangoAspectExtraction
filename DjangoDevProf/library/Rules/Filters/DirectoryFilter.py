__author__ = 'freddy'
import sys
sys.path.append("../../")
sys.path.append("../../../")
from Filter import Filter
import libs.Directory
import library.Diff
import logging

class DirectoryFilter(Filter):

    """
    The constructor which specifies the way the filter should be executed
        directory: The directory that should be searched for
    """
    def __init__(self, directory):
        self.directory = directory

    """
        This function will apply the filter, who was setup with specific arguments, to specific functions
        args: Used for rules
        return: None for no skill found otherwise amount ot EA's a Int
    """
    def apply_filter(self, type, filepath, diff, content):
        file_directory = libs.Directory.drop_filename(filepath)
        if libs.Directory.match_directory(file_directory, self.directory):
            if diff:
                return len(library.Diff.get_modified_lines(diff))
            logging.warning("The diff is None for %s", filepath)
            return len(content.splitlines())
        return None


