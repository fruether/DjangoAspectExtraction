
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import FilenameFilter


class GitRule_(BaseRule2.Rule):
    def __init__(self):
        cf1 = FilenameFilter.FilenameFilter(".git", "start")
        expr = Or.Or(cf1, None)
        super(GitRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Administration/VCS"


