__author__ = 'freddy'


import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import Or
from library.Rules.Filters import DirectoryFilter, FilenameFilter

class KnowledgeManagementRule_(BaseRule2.Rule):
    def __init__(self):
        ptf1 = FilenameFilter.FilenameFilter("ReadMe.mb")
        ctf1 = DirectoryFilter.DirectoryFilter("docs/")
        expr = Or.Or(ctf1, ptf1)
        super(KnowledgeManagementRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Other/KnowledgeManagement"




