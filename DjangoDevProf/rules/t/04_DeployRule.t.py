__author__ = 'freddy'

from TAP.Simple   import *
import sys
sys.path.append("../../")
from rules.DeployRule import DeployRule_


plan(2)

rule = DeployRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/Wsgi.py","", "").skill,"Other/Deployment", "Check filename")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check filename - wrong")
