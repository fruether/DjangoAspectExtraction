__author__ = 'freddy'

import sys

from TAP.Simple   import *

sys.path.append("../Filters")
import ParseTreeFilter
import library.Rules.Filters.libs.ParseTree
import os
plan(2)

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

library.Rules.Filters.libs.ParseTree.setup_inheritance_tree(content1)


with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample.diff", "r") as f:
    diff1 = f.read()

ptf1 = ParseTreeFilter.ParseTreeFilter("Base")
ptf2 = ParseTreeFilter.ParseTreeFilter("def __init__(self, name, number_of_commits)", True, False)

eq_ok(ptf1.apply_filter("","", diff1, content1) , 4, "Normal-case")
eq_ok(ptf2.apply_filter("A","", diff1, content1) , 5, "Normal-case")
