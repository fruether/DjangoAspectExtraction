
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, Or, RightAnd
from library.Rules.Filters import ContentFilter, ParseTreeFilter

class ModelFormsRule_(BaseRule2.Rule):
    def __init__(self):
        cf1 = ContentFilter.ContentFilter(r'import (django.)?forms', "regex_anywhere")
        cf2 = ContentFilter.ContentFilter(r'import (django.forms.)?ModelForm', "regex_anywhere")
        expr_or = Or.Or(cf1, cf2)

        ptf1 = ParseTreeFilter.ParseTreeFilter("ModelForm")
        expr = RightAnd.RightAnd(expr_or, ptf1)
        super(ModelFormsRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Forms/Model"



