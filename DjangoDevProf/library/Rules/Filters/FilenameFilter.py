__author__ = 'freddy'
import sys
sys.path.append("../../")
sys.path.append("../../../")
from Filter import Filter
import libs.Filename
import library.Diff

class FilenameFilter(Filter):
    """
    The constructor which specifies the way the filter should be executed
        str: The string that should be contained in the filenemae
        filter: The function that should be executed in the library (middle of filename, end of filename , and so on)
    """
    def __init__(self, str, filter = ""):
        self.filter = ["somewhere", "middle", "start", "suffix", "", "regex"]
        if filter not in self.filter:
            print sys.stderr, "Error, we can't apply your filter, Make sure the name is valid: " + filter
            self.filter = ""
        self.filter = filter
        self.base_name = "match_filename"
        self.str = str.upper()

    """
        This function will apply the filter, who was setup with specific arguments, to specific functions
        args: Used for rules
        return: None for no skill found otherwise amount ot EA's a Int
    """
    def apply_filter(self, type, filepath, diff, content):
        if self.filter == "":
           func =  getattr(libs.Filename, self.base_name)
           if func(self.str, filepath.upper()):
              return len(library.Diff.get_modified_lines(diff)) if diff != None else len(content.splitlines())
        else:
            function_name = self.base_name + "_" + self.filter
            func = getattr(libs.Filename, function_name)
            if func(self.str, filepath.upper()):
                if diff:
                    return len(library.Diff.get_modified_lines(diff))
                return len(content.splitlines())
        return None
