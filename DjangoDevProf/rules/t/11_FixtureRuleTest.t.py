__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.FixtureRule import FixtureRule_


plan(4)

rule = FixtureRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/Settings.py","", "").skill,"Database/Fixture", "Check filename")
eq_ok(rule.match("A", "/a/b/c/c/e/initial_data.xml","", "").skill,"Database/Fixture", "Check filename")
eq_ok(rule.match("A", "/a/b/c/c/e/initial_data.yaml","", "").skill,"Database/Fixture", "Check filename")

eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check filename - wrong")
