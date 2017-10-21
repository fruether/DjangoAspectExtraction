__author__ = 'freddy'

from TAP.Simple   import *
import library.Diff

plan(4)

eq_ok(library.Diff.read_hunk("@@ -1,3 +1,9 @@"), (1,9), "Size of digit is 1")
eq_ok(library.Diff.read_hunk("@@ -5,16 +11,10 @@"), (11,10), "Size of digit is 2")

eq_ok(library.Diff.read_hunk("@@ -410,6 +410,10 @@ class Meta:"), (410,10), "Header has line at the end")
eq_ok(library.Diff.read_hunk("@@ -9,28 +9,28 @@ from mailer import Message"), (9,28), "Header has line at the end")


#eq_ok(library.Diff.read_hunk(" -5,16 +11,10 @@"), None, "Size of digit is 2")
