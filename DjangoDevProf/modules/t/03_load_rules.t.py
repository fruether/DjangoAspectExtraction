__author__ = 'freddy'


from TAP.Simple   import *
import modules.RuleEngine
import os

plan(2)
rulePath = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/rules/old"
rulePathNew = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/rules/other"
filePath = os.path.join(rulePath, "__init__.py")
filePathNew = os.path.join(rulePathNew, "__init__.py")

modules.RuleEngine.load_rules(rulePath)
modules.RuleEngine.load_rules(rulePathNew)

file = open(filePath, 'r')
content = file.read()
file.close()

file = open(filePathNew, 'r')
content2 = file.read()
file.close()


ok(content == "__all__ =['Test', 'Test2', 'Test3']", "test if modules are loaded")
ok(content2 == "__all__ =['Test2', 'Test3']", "test if modules are loaded")


