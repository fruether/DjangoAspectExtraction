__author__ = 'freddy'


import sys
sys.path.append("../Filters")
import ContentFilter
from TAP.Simple import *


plan(4)

string = "/* Single line comment*/ \\n CREATE TABLE test_user (name VARCHAR(25) NOT NULL, PRIMARY KEY(name));"
cf1 = ContentFilter.ContentFilter("TABLE", "string")
cf2 = ContentFilter.ContentFilter("TABLE", "string_kmp")
cf3 = ContentFilter.ContentFilter(r'((.*) (table|TABLE) (.*))', "regex")
cf4 = ContentFilter.ContentFilter(r'(table|TABLE)', "regex_anywhere")


import sys
#print >> sys.stderr, cf1.apply_filter("","", "", string)
ok(cf1.apply_filter("","", "", string) == 0)
ok(cf2.apply_filter("", "","", string) == 0)
ok(cf3.apply_filter("","", "", string) == 0)
ok(cf4.apply_filter("","", "", string) == 0)
