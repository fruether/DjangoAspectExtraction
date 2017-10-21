__author__ = 'freddy'
from TAP.Simple   import *

import library.Rules.Filters.libs.Filename


plan(13)

#match_filename_somewhere
eq_ok(library.Rules.Filters.libs.Filename.match_filename_somewhere("Case", "/a/b/c/d/e/TestCase.java"), True , "Normal case - match_filename_somewhere - 1")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_somewhere("Test", "/a/b/c/d/e/TestCase.java"), True , "Normal case - match_filename_somewhere - 2")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_somewhere(".java", "a/b/c/d/e/TestCase.java"), True , "Normal case - match_filename_somewhere - 3")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_somewhere("d", "/a/b/c/d/e/TestCase.java"), False , "Normal case - match_filename_somewhere - 4")

#match_filename_middle
eq_ok(library.Rules.Filters.libs.Filename.match_filename_middle("Case", "/a/b/c/d/e/TestCase.java"), True, "Normal case - match_filename_middle -1")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_middle("Test", "/a/b/c/d/e/TestCase.java"), False, "Normal case - match_filename_middle - 2")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_middle(".java", "/a/b/c/d/e/TestCase.java"), False, "Normal case - match_filename_middle - 3")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_middle("Case", "/a/b/c/d/e/TestNormalCase.java"), True, "Normal case - match_filename_middle - 4")

#match_start
eq_ok(library.Rules.Filters.libs.Filename.match_filename_start("Case", "/a/b/c/d/e/TestCase.java"), False, "Normal case - match_start - 1")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_start("Test", "/a/b/c/d/e/TestCase.java"), True, "Normal case - match_start - 2")
eq_ok(library.Rules.Filters.libs.Filename.match_filename_start("d", "/a/b/c/d/e/TestCase.java"), False, "Normal case - match_start - 3")

#match_filename
ok(library.Rules.Filters.libs.Filename.match_filename("Admin.py", "a/b/c/d/e/f/Admin.py"))
ok(not library.Rules.Filters.libs.Filename.match_filename("Admin.py", "a/b/c/d/e/f/User.py"))