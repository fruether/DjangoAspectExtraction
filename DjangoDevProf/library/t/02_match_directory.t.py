__author__ = 'freddy'
from TAP.Simple   import *

import library.Rules.Filters.libs.Directory


plan(5)

ok(library.Rules.Filters.libs.Directory.match_directory("/a/b/c/d/e", "/d/e"))
ok(not library.Rules.Filters.libs.Directory.match_directory("/a/b/c/d/e", "/f/g/h/i"))
ok(library.Rules.Filters.libs.Directory.match_directory("/a/b/c/d/e/f/g", "/d/e"))
library.Rules.Filters.libs.Directory.setup_basepath("/c/g")
ok(library.Rules.Filters.libs.Directory.match_directory("/c/g/a/b/c/d/e", "d/e"))
ok(not library.Rules.Filters.libs.Directory.match_directory("/a/b/c/d/e", "/f/g/h/i"))