__author__ = 'freddy'

from TAP.Simple   import *

import library.Rules.Filters.libs.Filename


plan(2)

eq_ok(library.Rules.Filters.libs.Filename.match_filename_suffix(".xml", "/a/b/c/d/e/test.xml"), True, "Check if the suffix will be recognized")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_suffix(".php", "/a/b/c/d/e/test.xml"), False, "Check if the suffix will be recognized")


