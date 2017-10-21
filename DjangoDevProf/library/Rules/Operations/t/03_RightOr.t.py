__author__ = 'freddy'

import sys
#sys.path.append("../Filters")
sys.path.append("../../../")
from library.Rules.Filters.Filter import Filter

from library.Rules.Operations.RightOr import RightOr
from TAP.Simple   import *

class Test1(Filter):
    def __init__(self):
        super(Test1, self).__init__()
    def apply_filter(*args):
        return 12
class Test2(Filter):

    def __init__(self):
        super(Test2, self).__init__()

    def apply_filter(*args):
        return 14


t1 = RightOr(Test1(), Test2())
t2 = RightOr(Test2(), Test1())

plan(4)
eq_ok(t1.execute("A"), 14, "Check left")
eq_ok(t2.execute("A"), 12, "Check left")
eq_ok(RightOr(None, t1).execute("A"), 14, "Check left")
eq_ok(RightOr(t1, None).execute("A"), 14, "Check left")
