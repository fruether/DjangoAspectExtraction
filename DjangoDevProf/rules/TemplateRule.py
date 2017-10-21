
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or, RightOr
from library.Rules.Filters import DirectoryFilter, ContentFilter

class TemplateRule_(BaseRule2.Rule):
    def __init__(self):
        df1 = DirectoryFilter.DirectoryFilter("Templates/")
        regular1 = r'({%[^%]*%})'
        regular2 = r'({{[^}]*}})'
        cf2 = ContentFilter.ContentFilter(r'' + regular1 + '|' + regular2, "regex", True, True)
        a = RightOr.RightOr(df1, cf2)
        super(TemplateRule_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Other/Templates"


