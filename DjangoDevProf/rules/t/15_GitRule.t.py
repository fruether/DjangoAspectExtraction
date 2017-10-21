__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.GitRule import GitRule_


plan(2)


rule = GitRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/.gitignore","", "").skill,"Administration/VCS", "Check rule correct")

eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check rule - wrong")

