import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.DataModelRule import DataModelRule_
import library.Rules.Filters.libs.ParseTree
import library.InheritanceTree
import os


plan(3)

rule = DataModelRule_()
project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/model.py")
file_path2 = os.path.join(project_path, "data/model2.py")
file_path3 = os.path.join(project_path, "data/model3.py")

with open(file_path, "r") as f:
    content = f.read()
with open(file_path2, "r") as f:
    content2 = f.read()
with open(file_path3, "r") as f:
    content3 = f.read()



#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/Admin.py","", content),None, "Check without parsing")
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path2)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path3)

eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", content).skill, "Model/Data", "Check after setup of parse tree")
eq_ok(rule.match("A", "/a/b/c/d/e/model2.py","", content2).experience, 21, "Check if loc is right for A files ")

#print >> sys.stderr, rule.match("A", "/a/b/c/d/e/model2.py","", content3).experience