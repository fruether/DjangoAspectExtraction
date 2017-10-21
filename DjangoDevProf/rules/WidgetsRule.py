__author__ = 'freddy'


import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, Or, RightAnd
from library.Rules.Filters import ParseTreeFilter, ContentFilter

class WidgetsRule_(BaseRule2.Rule):
    def __init__(self):
        ptf2 = ParseTreeFilter.ParseTreeFilter("def decompress(self, value)", True)
        ctf1 = ContentFilter.ContentFilter(r'import (django.forms.)?widgets' ,"regex_anywhere", True)
        pt1 = ParseTreeFilter.ParseTreeFilter("MultiWidget")
        expr1 = Or.Or(pt1, ptf2)

        expr = RightAnd.RightAnd(ctf1, expr1)
        super(WidgetsRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Forms/Widget"


