__author__ = 'freddy'

from abc import ABCMeta, abstractmethod
import sys
sys.path.append("../../")
from library.datas.Skill import Skill
import sys

"""
#Not used in that version. Just here for role backs
"""
class Rule:
    __metaclass__ = ABCMeta
    #These functions return the line of code, that is applicable to that skill
    @abstractmethod
    def check_directory(self, type, filepath, diff, content): pass
    @abstractmethod
    def check_filename(self, type, filepath, diff, content): pass
    @abstractmethod
    def check_content(self, type, filepath, diff, content): pass
    @abstractmethod
    def check_parse_tree(self, type, filepath, diff, content): pass
    @abstractmethod
    def get_skill_string(self): pass


    def __init__(self, filters, comb_and, applicable):
        self.ands = filters
        self.comb_and = comb_and
        if len(applicable) > 3:
            print >> sys.stderr, "A rule can't have more than 3 applicables. Just Modify, Add, Delete is available"

        self.applicable = applicable

    def match(self, type, *args):
        if type not in self.applicable:
            return None
        #Call all the check Funktions for and and ors if applicable
        results = []
        if self.comb_and:
            return self.match_ands(type, *args)
        else:
            return self.match_ors(type, *args)

    def merge(self, results):
        if len(results) == 0:
            return None
        minimum = min(results)
        return Skill(self.get_skill_string(), minimum)

    def match_ands(self,  *args):
        if len(self.ands) == 0:
            return []
        results = []
        for filter in self.ands:
            func = getattr(self, "check_" + filter, None)
            result = func(*args)
            if result == None:
                return None
            results.append(result)
        return self.merge(results)


    def match_ors(self, *args):
        if len(self.ands) == 0:
            return []
        results = []
        for filter in self.ands:
            func = getattr(self, "check_" + filter, None)
            result = func(*args)
            if result != None:
                results.append(result)

        return self.merge(results)


