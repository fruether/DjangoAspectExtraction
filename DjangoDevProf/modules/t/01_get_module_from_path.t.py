__author__ = 'freddy'
from TAP.Simple   import *
import modules.RuleEngine
plan(4)

eq_ok(modules.RuleEngine.get_module_from_path("blah/test"),"test", "We got the last part of a path")
eq_ok(modules.RuleEngine.get_module_from_path("blah/test/"),"test", "We got the last part of a path that ends with /")
eq_ok(modules.RuleEngine.get_module_from_path("blah"),"blah", "grenzfall")
eq_ok(modules.RuleEngine.get_module_from_path("a/b/c/d/e/f/g/h/i/blah"),"blah", "long path")



