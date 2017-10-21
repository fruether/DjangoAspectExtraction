__author__ = 'freddy'
from TAP.Simple   import *
import sys
sys.path.append('../Rules')
sys.path.append('../datas')
import BaseRule
import Skill
#import .datas.BaseRule.Rule

class Test(BaseRule.Rule):
    #These functions return the line of code, that is applicable to that skill
    def check_directory(self, type, filepath, diff, content):
        return 10

    def check_filename(self, type, filepath, diff, content):
        return 14

    def check_content(self, type, filepath, diff, content):
        return None

    def check_parse_tree(self, type, filepath, diff, content):
        return None

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test, self).__init__(["directory", "filename"], True,["A", "E"])

class Test2(BaseRule.Rule):
    #These functions return the line of code, that is applicable to that skill
    def check_directory(self, type, filepath, diff, content):
        return None

    def check_filename(self, type, filepath, diff, content):
        return None

    def check_content(self, type, filepath, diff, content):
        return 13

    def check_parse_tree(self, type, filepath, diff, content):
        return 9

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test2, self).__init__(["content", "parse_tree"], False,["A", "E"])

class Test3(BaseRule.Rule):
    #These functions return the line of code, that is applicable to that skill
    def check_directory(self, type, filepath, diff, content):
        return None

    def check_filename(self, type, filepath, diff, content):
        return None

    def check_content(self, type, filepath, diff, content):
        return 12

    def check_parse_tree(self, type, filepath, diff, content):
        return None

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test3, self).__init__(["content", "parse_tree"], True,["A", "E"])

class Test4(BaseRule.Rule):
    #These functions return the line of code, that is applicable to that skill
    def check_directory(self, type, filepath, diff, content):
        return None

    def check_filename(self, type, filepath, diff, content):
        return None

    def check_content(self, type, filepath, diff, content):
        return 12

    def check_parse_tree(self, type, filepath, diff, content):
        return None

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test4, self).__init__(["content", "parse_tree"], False,["A", "E"])

plan(7)

t1 = Test()
t2 = Test2()
t3 = Test3()
t4 = Test4()

eq_ok(t1.match("A", "", "", "").experience, 10, "Check if lines of code is right")
eq_ok(t1.match("E", "", "", "").skill, "Model/Data", "Check if Skill is right")
eq_ok(t1.match("M", "", "", ""), None, "Check for applicable")

eq_ok(t2.match("A", "", "", "").experience, 9, "Check if lines of code is right for or")
eq_ok(t2.match("E", "", "", "").skill, "Model/Data", "Check if Skill is right for or")

eq_ok(t3.match("E", "", "", ""), None, "Check if Skill is right for a failed and combination")

eq_ok(t4.match("E", "", "", "").experience, 12, "Check if Skill is right for one failed or")
