__author__ = 'freddy'

__author__ = 'freddy'


import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import FilenameFilter

class BuildManagementRule_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter("Makefile")
        expr = Or.Or(ff1, None)
        super(BuildManagementRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Administration/Buildmangament"





