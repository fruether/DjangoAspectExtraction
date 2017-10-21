__author__ = 'freddy'


import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, RightAnd
from library.Rules.Filters import FilenameFilter, ContentFilter

class SqlRule_(BaseRule2.Rule):
    def __init__(self):
        ff1 = FilenameFilter.FilenameFilter(".sql", "suffix")
        regex_insert = r'INSERT INTO (.)* VALUES(((.)+,)*(.)+);'
        cf2 = ContentFilter.ContentFilter(regex_insert, "regex", True, True)
        expr = RightAnd.RightAnd(ff1, cf2)
        super(SqlRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Database/SQL"




