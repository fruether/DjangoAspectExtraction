
import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import DirectoryFilter, FilenameFilter

class FixtureRule_(BaseRule2.Rule):
    def __init__(self):
        df1 = DirectoryFilter.DirectoryFilter("fixtures/")
        ff1 = FilenameFilter.FilenameFilter("initial_data.(json|xml|yaml)", "regex")
        a = Or.Or(ff1, df1)
        super(FixtureRule_, self).__init__(a,["A", "M"])

    def get_skill_string(self):
        return "Database/Fixture"


