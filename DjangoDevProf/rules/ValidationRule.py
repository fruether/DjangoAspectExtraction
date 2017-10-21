
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, RightAnd
from library.Rules.Filters import ParseTreeFilter, ContentFilter

class ValidationRule_(BaseRule2.Rule):
    def __init__(self):
        cf1 = ContentFilter.ContentFilter("import (django.core.exceptions.)?ValidationError", "regex_anywhere")
        cf2 = ParseTreeFilter.ParseTreeFilter(r'def validate_(.)+(((.),)*)', True, True)
        expr = RightAnd.RightAnd(cf1, cf2)
        super(ValidationRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Validation"


