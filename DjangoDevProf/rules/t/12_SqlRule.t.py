__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.SqlRule import SqlRule_
import os


plan(4)

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/datas.sql")
with open(file_path, "r") as f:
    content = f.read()

file_path2 = os.path.join(project_path, "data/htmlForm.py")
with open(file_path2, "r") as f:
    content2 = f.read()

rule = SqlRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/data.sql",content, content).skill,"Database/SQL", "Check rule correct")
eq_ok(rule.match("A", "/a/b/c/fixtures/e/data.sql","", content).experience, 2, "Check rule correct")

#print >> sys.stderr, rule.match("A", "/a/b/c/fixtures/e/data.sql","", content).loc
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check rule - wrong")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py",content2, ""), None, "Check rule - wrong")
