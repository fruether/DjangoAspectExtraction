
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, RightAnd
from library.Rules.Filters import ContentFilter, ParseTreeFilter

class HTMLFormsRule_(BaseRule2.Rule):
    def __init__(self):
        cf1 = ContentFilter.ContentFilter("import (django.)?forms", "regex_anywhere")
        ptf1 = ParseTreeFilter.ParseTreeFilter("Form")
        expr = RightAnd.RightAnd(cf1, ptf1)
        super(HTMLFormsRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Forms/HTML"


