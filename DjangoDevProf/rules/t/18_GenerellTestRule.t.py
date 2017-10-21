__author__ = 'freddy'

from TAP.Simple   import *
import sys
import os
sys.path.append("../../")
from rules.GenerellTest import GenerellTest_



plan(2)


rule = GenerellTest_()

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/generellTest.py")
file_path2 = os.path.join(project_path, "data/htmlForm.py")

with open(file_path, "r") as f:
    content = f.read()
with open(file_path2, "r") as f:
    content2 = f.read()


#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/url.py","", content).skill,"Test/Generell", "Correct case for Modelforms")
#print >> sys.stderr, rule.match("A", "/a/b/c/d/e/test.py","", content2)
eq_ok(rule.match("A", "/a/b/c/d/e/htmlForrm.py","", content2), None, "Wrong Case for ModelForms")
