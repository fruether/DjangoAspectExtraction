__author__ = 'freddy'

import sys
import os

from TAP.Simple import *

sys.path.append("../../")
from rules.MigrationRule import MigrationRule_
import library.Rules.Filters.libs.ParseTree
plan(4)

rule = MigrationRule_()

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/migration.py")
file_path2 = os.path.join(project_path, "data/htmlForm.py")
file_path3 = os.path.join(project_path, "data/migration3.py")
file_path4 = os.path.join(project_path, "data/view.py")
file_path5 = os.path.join(project_path, "data/migration2.py")

with open(file_path, "r") as f:
    content = f.read()
with open(file_path2, "r") as f:
    content2 = f.read()

with open(file_path3, "r") as f:
    content3 = f.read()
with open(file_path5, "r") as f:
    content5 = f.read()

library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path4)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path3)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path5)

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/url.py","", content).skill,"Database/Migration", "Correct case for Modelforms")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", content2), None, "Wrong Case for ModelForms")
eq_ok(rule.match("A", "/a/b/c/d/e/mig.py","", content3).skill, "Database/Migration", "Correct case for Modelforms")
eq_ok( rule.match("A", "/a/b/c/d/e/mig.py","", content5).experience, 7, "Just some test")