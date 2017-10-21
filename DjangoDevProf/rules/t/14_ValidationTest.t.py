__author__ = 'freddy'

from TAP.Simple   import *
import sys
sys.path.append("../../")
from rules.ValidationRule import ValidationRule_
import os


plan(2)

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/validate.py")
with open(file_path, "r") as f:
    content = f.read()

file_path2 = os.path.join(project_path, "data/htmlForm.py")
with open(file_path2, "r") as f:
    content2 = f.read()

rule = ValidationRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/data.sql",content, content).skill,"Validation", "Check rule correct")

eq_ok(rule.match("A", "/a/b/c/d/e/test.py",content2, ""), None, "Check rule - wrong")
