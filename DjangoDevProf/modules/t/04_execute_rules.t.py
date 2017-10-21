__author__ = 'freddy'

from TAP.Simple   import *

import modules.RuleEngine
import library.datas.Skill
import library.Rules.Filters.libs.Directory


plan(5)
library.Rules.Filters.libs.Directory.setup_basepath("/c/g")
rulePath = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/rules/old"
modules.RuleEngine.load_rules(rulePath)
eq_ok(modules.RuleEngine.execute_rules("A", "", "", "")[0].experience, 2, "test if rules will be executes")
eq_ok(modules.RuleEngine.execute_rules("A", "", "", "")[1].experience, 15, "test if rules will be executes")
eq_ok(modules.RuleEngine.execute_rules("A", "", "", "")[2].experience, 12, "test if rules will be executes")

rulePath = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/rules/other"
modules.RuleEngine.reset()
modules.RuleEngine.load_rules(rulePath)

eq_ok(modules.RuleEngine.execute_rules("A", "t.xml", "", "")[0].experience, 6, "test if rules will be executes")
eq_ok(modules.RuleEngine.execute_rules("A", "t.xml", "", "")[1].experience, 0, "test if rules will be executes")


