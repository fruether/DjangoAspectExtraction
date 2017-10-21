__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.ConfRule import ConfRule_


plan(2)

rule = ConfRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/d/e/Settings.py","", "").skill,"Other/DjangoConfiguration", "Check filename")
eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check filename - wrong")
