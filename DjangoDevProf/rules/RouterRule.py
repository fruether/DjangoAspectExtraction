
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import FilenameFilter

class RouterRule_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter("url.py", "")
        a = Or.Or(ff1, None)
        super(RouterRule_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Other/Router"


