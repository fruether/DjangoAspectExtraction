__author__ = 'freddy'

from TAP.Simple   import *
import sys
sys.path.append("../../")
from rules.BuildManagementRule import BuildManagementRule_



plan(2)


rule = BuildManagementRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/Makefile","", "").skill,"Administration/Buildmangament", "Check rule correct")

eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check rule - wrong")

