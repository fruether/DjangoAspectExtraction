from TAP.Simple   import *
import sys
sys.path.append("../../")
from rules.TemplateRule import TemplateRule_

import os


plan(6)

rule = TemplateRule_()
project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/rules/t"
file_path = os.path.join(project_path, "data/template.tl")
file_path2 = os.path.join(project_path, "data/model.py")
file_path3 = os.path.join(project_path, "data/templateTest.html")

with open(file_path, "r") as f:
    content = f.read()
with open(file_path2, "r") as f:
    content2 = f.read()
with open(file_path3, "r") as f:
    content3 = f.read()


#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/Admin.py","", ""),None, "Check Wrong")
eq_ok(rule.match("A", "/a/b/c/Templates/e/Admin.py","", "").skill, "Other/Templates", "Check Right")

#Check if the content filter works
eq_ok((rule.match("A", "/a/b/c/d/e/Admin.py", content, content)).skill, "Other/Templates", "Check Left side of rule")
eq_ok((rule.match("A", "/a/b/c/d/e/Admin.py", content, content)).experience, 12, "Check Left side of rule")
eq_ok((rule.match("A", "/a/b/c/d/e/Admin.py", content2, content2)), None, "Check Left side of rule")
eq_ok((rule.match("A", "/a/b/c/d/e/Admin.py", content3, content3)).experience, 66, "Check Left side of rule")