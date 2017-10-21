__author__ = 'freddy'
from TAP.Simple   import *
import modules.RuleEngine

plan(2)

eq_ok(modules.RuleEngine.get_project_path("blah/test"),"blah/", "We got the first part of a path")
eq_ok(modules.RuleEngine.get_project_path("a/b/c/d/e/f/blah/test/"),"a/b/c/d/e/f/blah/", "We got the last part of a path that ends with /")