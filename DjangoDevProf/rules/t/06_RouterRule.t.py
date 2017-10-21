__author__ = 'freddy'

from TAP.Simple   import *
import sys
sys.path.append("../../")
from rules.RouterRule import RouterRule_

plan(2)

rule = RouterRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/url.py","", "").skill,"Other/Router", "Check filename")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check filename - wrong")
