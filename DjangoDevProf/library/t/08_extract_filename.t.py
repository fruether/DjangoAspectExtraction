__author__ = 'freddy'
from TAP.Simple   import *

import library.Rules.Filters.libs.Filename


plan(2)


eq_ok(library.Rules.Filters.libs.Filename.extract_filename("/a/b/c/d/e/x.html"), "x.html", "Check one of the many normal cases")
eq_ok(library.Rules.Filters.libs.Filename.extract_filename("x.html"), "x.html", "Check one of the many border cases")
