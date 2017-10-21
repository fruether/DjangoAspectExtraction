__author__ = 'freddy'

import sys
import os

from TAP.Simple   import *

sys.path.append("../../")
from rules.ModelFormsRule import ModelFormsRule_
import library.Rules.Filters.libs.ParseTree
plan(2)

rule = ModelFormsRule_()

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/modelForm.py")
file_path2 = os.path.join(project_path, "data/htmlForm.py")

with open(file_path, "r") as f:
    content = f.read()
with open(file_path2, "r") as f:
    content2 = f.read()

library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path)
#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/url.py","", content).skill,"Forms/Model", "Correct case for Modelforms")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", content2), None, "Wrong Case for ModelForms")
