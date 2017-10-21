__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../../")
from rules.KnowledgeManagementRule import KnowledgeManagementRule_


plan(3)


rule = KnowledgeManagementRule_()

#filepath, diff, content
eq_ok(rule.match("A", "/a/b/c/fixtures/e/ReadMe.mb","", "").skill,"Other/KnowledgeManagement", "Check rule correct")
eq_ok(rule.match("A", "/a/b/c/docs/e/SomeShit.mb","", "").skill,"Other/KnowledgeManagement", "Check rule correct")

eq_ok(rule.match("A", "/a/b/c/d/e/test.py","", ""), None, "Check rule - wrong")

