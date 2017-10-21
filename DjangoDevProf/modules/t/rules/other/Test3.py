
import sys
sys.path.append("../../../../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import FilenameFilter, Filter


class Test3_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter("t.xml", "")
        df1 = Test3_.DirectoryFilter3()
        a = Or.Or(ff1, df1)
        super(Test3_, self).__init__(a,["A", "E"])

    def get_skill_string(self):
        return "Model/Data"

    class DirectoryFilter3(Filter.Filter):
        def apply_filter(self, type, filepath, diff, content):
            return None
        def __init__(self):
            super(Test3_.DirectoryFilter3, self).__init__()



