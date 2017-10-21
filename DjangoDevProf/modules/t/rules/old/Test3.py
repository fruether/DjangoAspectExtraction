import sys
sys.path.append("../../../../")
from library.Rules.Filters.libs import Directory
from library.Rules import BaseRule

class Test3_(BaseRule.Rule):
    def check_directory(self, type, filepath, diff, content):
        if Directory.match_directory("/c/g/a/b/c/d/e", "d/e"):
            return 12
        return None

    def check_filename(self, type, filepath, diff, content):
       # if Filename.match_filename("Admin.py", filepath):
       #     return len(Diff.get_modified_lines(diff))
        return 15

    def check_content(self, type, filepath, diff, content):
        return None

    def check_parse_tree(self, type, filepath, diff, content):
        #return ParseTree.match_baseclass("admin.ModelAdmin", content, diff)
        return 33

    def get_skill_string(self):
        return "Model/Data"

    def __init__(self):
        super(Test3_, self).__init__(["directory"], False,["A", "E"])

