__author__ = 'freddy'
from TAP.Simple   import *

import library.Rules.Filters.libs.Directory


plan(3)

eq_ok(library.Rules.Filters.libs.Directory.drop_filename("/a/b/c/d/e"), "/a/b/c/d/e", "Nothing to delete")
eq_ok(library.Rules.Filters.libs.Directory.drop_filename("/a/b/c/d/e.xml"), "/a/b/c/d", "File to delete")
eq_ok(library.Rules.Filters.libs.Directory.drop_filename("a/b/c/d/e.xml"), "a/b/c/d", "File to delete")
