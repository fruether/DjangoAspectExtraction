__author__ = 'freddy'

import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import ParseTreeFilter, FilenameFilter

class AdminIntModel_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter("Admin.py")
        ctf1 = ParseTreeFilter.ParseTreeFilter("ModelAdmin")
        a = Or.Or(ctf1, ff1)
        super(AdminIntModel_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Model/Admininterface"


