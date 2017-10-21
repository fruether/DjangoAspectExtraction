
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, Not, Or
from library.Rules.Filters import ParseTreeFilter, ContentFilter,FilenameFilter

class GenerellTest_(BaseRule2.Rule):
    def __init__(self):
        ctf1 = ContentFilter.ContentFilter(r'import (django.test.)?TestCase' ,"regex_anywhere")
        ctf2 = ContentFilter.ContentFilter(r'import (django.)test' ,"regex_anywhere")
        expr1 = Not.Not(Or.Or(ctf1, ctf2))

        ctf3 = ParseTreeFilter.ParseTreeFilter(r'def test_(.)*(self(,(.)*)*)' , True, True)
        ff1 = FilenameFilter.FilenameFilter("Test","somewhere")
        expr2 = Or.Or(ff1, ctf3)

        expr  = And.And(expr2, expr1)
        super(GenerellTest_, self).__init__(expr2,["A", "M"])

    def get_skill_string(self):
        return "Test/Generell"
