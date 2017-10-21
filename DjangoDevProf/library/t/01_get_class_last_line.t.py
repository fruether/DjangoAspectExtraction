__author__ = 'freddy'

import os

from TAP.Simple   import *

import library.Rules.Filters.libs.ParseTree

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t"
file_path = os.path.join(project_path, "files/class_inheritance.py")
file_path2 = os.path.join(project_path, "files/class_inheritance_other_file.py")
file_path3 = os.path.join(project_path, "files/class_no_inheritance.py")
file_path4 = os.path.join(project_path, "files/class_combine_inheritance.py")
file_path5 = os.path.join(project_path, "files/test_class_oscar.py")
file_path6 = os.path.join(project_path, "files/test_class_oscar2.py")
file_path7 = os.path.join(project_path, "files/test_class_oscar3.py")

library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path)

plan(9)
x = library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path, "Base")[0]
#print >> sys.stderr, x
eq_ok((9, 27), x, "Test")
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path2)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path3)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path4)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path5)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path6)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree_from_path(file_path7)


eq_ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path2, "User")[0], (5, 23), "Classes in different files")
eq_ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path3, "User"), None, "Class with no inheritance at all")
eq_ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path4, "Base")[0], (9, 27), "Classes in same file and other file")
eq_ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path4, "Base")[0], (9, 27), "Classes in same file and other file")



z = library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path7, "ModelForm")[4]

eq_ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path2, "Base")[0], (5, 23), "Classes in same file and other file")
y = library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path5, "ModelForm")[0]
ok(y == (98,116))
ok(library.Rules.Filters.libs.ParseTree.get_class_scope_from_path(file_path6, "ModelForm")[0] == (58, 76))
eq_ok(z, (404, 415), "Another test motivated by a oscar file")