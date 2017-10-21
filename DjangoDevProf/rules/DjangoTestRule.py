
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, Or, RightAnd
from library.Rules.Filters import ParseTreeFilter, ContentFilter

class DjangoTestRule_(BaseRule2.Rule):
    def __init__(self):
        ptf1 = ParseTreeFilter.ParseTreeFilter("TestCase")
        ctf1 = ContentFilter.ContentFilter(r'import (django.test.)?TestCase' ,"regex_anywhere")
        ctf2 = ContentFilter.ContentFilter(r'import (django.)test' ,"regex_anywhere")
        expr_pre = Or.Or(ctf1, ctf2)
        expr    = RightAnd.RightAnd(expr_pre, ptf1)
        super(DjangoTestRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Test/Django"


