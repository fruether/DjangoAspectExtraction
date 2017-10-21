
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, RightAnd
from library.Rules.Filters import ParseTreeFilter, ContentFilter

class DataModelRule_(BaseRule2.Rule):
    def __init__(self):
        ptf1 = ParseTreeFilter.ParseTreeFilter("Model")
        ctf1 = ContentFilter.ContentFilter(r'import (django.db.)?models' ,"regex_anywhere")
        a = RightAnd.RightAnd(ctf1, ptf1)
        super(DataModelRule_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Model/Data"


