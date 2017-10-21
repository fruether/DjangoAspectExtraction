__author__ = 'freddy'


__author__ = 'freddy'
import sys

from TAP.Simple   import *

sys.path.append('../../')

from library.Rules.Operations.And import And
from library.Rules.Operations.Or import Or
from library.Rules.Operations.Not import Not
from library.Rules.Filters.Filter import Filter
from library.Rules.BaseRule2 import Rule
#from library.Rules.results.ExpirienceAtom import ExperienceAtom
#import .datas.BaseRule.Rule

class FilenameFilter(Filter):
    def apply_filter(self, type, filepath, diff, content):
        return 14
    def __init__(self):
        super(FilenameFilter, self).__init__()

class Test(Rule):
    class DirectoryFilter(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return 10
        def __init__(self):
            super(Test.DirectoryFilter, self).__init__()


    #These functions return the line of code, that is applicable to that skill
    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        f1 = Test.DirectoryFilter()
        f2 = FilenameFilter()

        super(Test, self).__init__(And(f1, f2), ["A", "E"])

class Test2(Rule):
    class DirectoryFilter(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return 9
        def __init__(self):
            super(Test2.DirectoryFilter, self).__init__()

    #These functions return the line of code, that is applicable to that skill
    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        f1 = Test2.DirectoryFilter()
        f2 = FilenameFilter()

        super(Test2, self).__init__(Or(f1, f2), ["A", "E"])


class Test3(Rule):
    class DirectoryFilter(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return None
        def __init__(self):
            super(Test3.DirectoryFilter, self).__init__()

    #These functions return the line of code, that is applicable to that skill
    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        f1 = Test3.DirectoryFilter()
        f2 = FilenameFilter()

        super(Test3, self).__init__(And(f1, f2), ["A", "E"])

class Test4(Rule):
    class DirectoryFilter(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return 4
        def __init__(self):
            super(Test4.DirectoryFilter, self).__init__()
    class DirectoryFilter2(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return 9
        def __init__(self):
            super(Test4.DirectoryFilter2, self).__init__()
    class DirectoryFilter3(Filter):
        def apply_filter(self, type, filepath, diff, content):
            return None
        def __init__(self):
            super(Test4.DirectoryFilter3, self).__init__()


    #These functions return the line of code, that is applicable to that skill
    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        f1 = Test4.DirectoryFilter()
        f2 = FilenameFilter()
        f3 = Test4.DirectoryFilter2()
        f4 = Test4.DirectoryFilter3()
        super(Test4, self).__init__(Or(And(f1, f2), And(f3, f4)), ["A", "E"])

class Test5(Rule):

    #These functions return the line of code, that is applicable to that skill
    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        f2 = FilenameFilter()

        super(Test5, self).__init__(Not(f2), ["A", "E"])


plan(8)

t1 = Test()
t2 = Test2()
t3 = Test3()
t4 = Test4()
t5 = Test5()

eq_ok(t1.match("A", "", "", "").experience, 12, "Check if lines of code is right")
eq_ok(t1.match("E", "", "", "").skill, "Model/Data", "Check if Skill is right")
eq_ok(t1.match("M", "", "", ""), None, "Check for applicable")

eq_ok(t2.match("A", "", "", "").experience, 11, "Check if lines of code is right for or")
eq_ok(t2.match("E", "", "", "").skill, "Model/Data", "Check if Skill is right for or")

eq_ok(t3.match("E", "", "", ""), None, "Check if Skill is right for a failed and combination")

eq_ok(t4.match("E", "", "", "").experience, 4, "Check if Skill is right for one failed or")
eq_ok(t5.match("E", "", "", ""), None, "Check if Skill is right for Not")
