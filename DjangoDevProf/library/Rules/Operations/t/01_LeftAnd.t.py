__author__ = 'freddy'

import sys
#sys.path.append("../Filters")
sys.path.append("../../../")
from library.Rules.Filters.Filter import Filter

from library.Rules.Operations.LeftAnd import LeftAnd
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


t1 = LeftAnd(Test1(), Test2())
t2 = LeftAnd(Test2(), Test1())

plan(4)
eq_ok(t1.execute("A"), 12, "Check left")
eq_ok(t2.execute("A"), 14, "Check left")
eq_ok(LeftAnd(None, t1).execute("A"), None, "Check left")
eq_ok(LeftAnd(t1, None).execute("A"), None, "Check left")
