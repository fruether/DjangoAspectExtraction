__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.AdminIntModel import AdminIntModel_
import library.Rules.Filters.libs.ParseTree
import library.InheritanceTree
import os


plan(3)

rule = AdminIntModel_()
project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/admin.py")
with open(file_path, "r") as f:
    content = f.read()


#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/Admin.py","", "").skill,"Model/Admininterface", "Check filename")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check filename - wrong")

library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path)
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", content).skill, "Model/Admininterface", "Check filename - wrong")
