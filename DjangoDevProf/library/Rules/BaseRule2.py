__author__ = 'freddy'


import sys
from abc import ABCMeta, abstractmethod
sys.path.append("../../")
from library.datas.Skill import Skill

import logging

class Rule:
    __metaclass__ = ABCMeta
    #Return the skill that function described
    @abstractmethod
    def get_skill_string(self): pass

    def __init__(self, expr, applicable):

        self.logicalOperation = expr
        if len(applicable) > 3:
            logging.error("A rule can't have more than 3 applicable arguments")
            print >> sys.stderr, "A rule can't have more than 3 applicables. Just Modify, Add, Delete is available"

        self.applicable = applicable

    """
    This function matches the rules with given arguments. In fact that is done by executing the Logical expression and then creating a Skill object (if applicable)
        type: Mode of file on git (Added, Deleted)
        *argy => The other args

        return: None if rule said it has no skills otherwise the found skills
    """
    def match(self, type, *args):
        if type not in self.applicable:
            return None
        #Call all the check Funktions for and and ors if applicable
        result = self.logicalOperation.execute(type, *args)
        if result == None:
            return None
        return Skill(self.get_skill_string(), result)

    """
    This function matches the rules with given arguments. In fact that is done by executing the Logical expression and then creating a Skill object (if applicable)
        type: Mode of file on git (Added, Deleted)
        *argy => The other args

        return: None if rule said it has no skills otherwise the found skills
    """
    def match2(self, type, *args):
        if type not in self.applicable:
            return None
        #Call all the check Funktions for and and ors if applicable
        result = self.logicalOperation.execute(type, *args)
        if result() == None:
            return None
        return Skill(self.get_skill_string(), result())
