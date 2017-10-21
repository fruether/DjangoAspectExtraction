__author__ = 'freddy'
import sys
sys.path.append("../../")
sys.path.append("../../../")
from Filter import Filter
import library.Rules.Filters.libs.ParseTree

class ParseTreeFilter(Filter):
    """
        The constructor which specifies the way the filter should be executed
        bases: The baseclass the class should have or the signature of a function
        function: The function that should be executed in the library (function or class)
        regex: Should be searched by regex or plain content (just important for function = True)
    """
    def __init__(self, bases, function = False, regex = False):
        self.bases = bases
        self.function = function
        self.regex = regex

    """
        This function will apply the filter, who was setup with specific arguments, to specific functions
        args: Used for rules
        return: None for no skill found otherwise amount ot EA's a Int
    """
    def apply_filter(self, type, filepath, diff, content):
        if self.function:
            return library.Rules.Filters.libs.ParseTree.match_function(type, self.bases, self.regex, content, diff)
        return library.Rules.Filters.libs.ParseTree.match_baseclass(type, self.bases, content, diff)