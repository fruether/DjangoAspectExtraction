
__author__ = 'freddy'
import os

from TAP.Simple   import *

import library.Rules.Filters.libs.ParseTree

plan(5)

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t"
file_path = os.path.join(project_path, "files/class_combine_inheritance.py")
file_path2 = os.path.join(project_path, "files/class_inheritance_other_file.py")
file_path3 = os.path.join(project_path, "files/class_inheritance.py")

with open(file_path, "r") as f:
    content1 = f.read()

with open(file_path2, "r") as f:
    content2 = f.read()
with open(file_path3, "r") as f:
    content3 = f.read()

with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample.diff", "r") as f:
    diff1 = f.read()


library.Rules.Filters.libs.ParseTree.setup_inheritance_tree(content1)
eq_ok(library.Rules.Filters.libs.ParseTree.match_baseclass("E", "Base", content1, diff1) , 4, "Normal-case")
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree(content3)
library.Rules.Filters.libs.ParseTree.setup_inheritance_tree(content2)

#Setup for test of not in same file class definitions
eq_ok(library.Rules.Filters.libs.ParseTree.match_baseclass("E", "User", content2, diff1) , 3, "Normal-case")
eq_ok(library.Rules.Filters.libs.ParseTree.match_baseclass("E","Base", content2, diff1) , 3, "Normal-case")
eq_ok(library.Rules.Filters.libs.ParseTree.match_baseclass("E","WrongClass", content2, diff1) , None, "Error-case")
#print >> sys.stderr, library.ParseTree.match_baseclass("A","Base", content2, diff1)
eq_ok(library.Rules.Filters.libs.ParseTree.match_baseclass("A","Base", content2, diff1) , 19, "Error-case")
