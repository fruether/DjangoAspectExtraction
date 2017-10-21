__author__ = 'freddy'



import sys
sys.path.append("../")


from library.Rules import BaseRule2
from library.Rules.Operations import And, RightAnd
from library.Rules.Filters import ParseTreeFilter, ContentFilter

class MigrationRule_(BaseRule2.Rule):
    def __init__(self):
        ptf1 = ParseTreeFilter.ParseTreeFilter("Migration")
        ctf1 = ContentFilter.ContentFilter(r'((import (django.db.)?migrations)|(import (.)+, migrations))' ,"regex_anywhere")
        expr = RightAnd.RightAnd(ctf1, ptf1)
        super(MigrationRule_, self).__init__(expr,["A", "M"])

    def get_skill_string(self):
        return "Database/Migration"




