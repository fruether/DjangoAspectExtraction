__author__ = 'freddy'


import sys
sys.path.append("../Filters")
import DirectoryFilter
from TAP.Simple   import *


plan(3)

df1 = DirectoryFilter.DirectoryFilter("/d/e")

ok(df1.apply_filter("","/a/b/c/d/e", "", "") == 0)
ok(df1.apply_filter("", "/f/g/h/i","", "") == None)
ok(df1.apply_filter("","/a/b/c/d/e/test.xml", "", "") == 0)
