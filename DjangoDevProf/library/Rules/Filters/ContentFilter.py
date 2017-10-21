__author__ = 'freddy'
import sys
sys.path.append("../../")
sys.path.append("../../../")
from Filter import Filter
import libs.Content
import library.Diff
import logging

class ContentFilter(Filter):

    """
    The constructor which specifies the way the filter should be executed
        str: The string that should be contained in the Directory
        filter: The function that should be executed in the library (middle of filename, end of filename , and so on)
        diff: Should be searched in the diff or in the content. Default will be Content
        finds: Should be counted by amount of finds (of str) or by the lines added. Default will be lines added
    """
    def __init__(self, str, filter = "string", diff = False, finds = False):
        self.filters = ["regex", "string", "string_kmp", "regex_anywhere"]
        if filter not in self.filters:
            logging.error("The filter argument is invalid")
            print sys.stderr, "Error, we can't apply your filter, Make sure the name is valid: " + filter
            self.filter = ""
        self.filter = filter
        self.base_name = "match_content"
        self.str = str
        self.lookdif = diff
        self.finds = finds

    """
        This function will apply the filter, who was setup with specific arguments, to specific functions
        args: Used for rules
        return: None for no skill found otherwise amount ot EA's a Int
    """
    def apply_filter(self, type, filepath, diff, content):
        if self.filter == "":
           func =  getattr(libs.Content, self.base_name)
        else:
            function_name = self.base_name + "_" + self.filter
            if self.finds:
                function_name += "_count"
            func = getattr(libs.Content, function_name)

        argument = library.Diff.filter_added_lines(diff) if self.lookdif and type != "A" else content
        if self.finds:
            return func(argument, self.str)

        if diff is not None:
            if func(argument, self.str):
                 return len(library.Diff.get_modified_lines(diff)) if type != "A" else len(content.splitlines())
        else:
            logging.warning("The diff is None in ContentFilter and file %s", filepath)
            if func(content, self.str):
                return len(content.splitlines())

        return None

