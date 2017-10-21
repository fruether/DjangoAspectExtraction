
__author__ = 'freddy'
import os

from TAP.Simple   import *

import library.Rules.Filters.libs.ParseTree

plan(5)

project_path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t"
file_path = os.path.join(project_path, "files/class_combine_inheritance.py")
file_path2 = os.path.join(project_path, "files/class_inheritance_other_file.py")

with open(file_path, "r") as f:
    content1 = f.read()

with open(file_path2, "r") as f:
    content2 = f.read()

with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample.diff", "r") as f:
    diff1 = f.read()


eq_ok(library.Rules.Filters.libs.ParseTree.get_function_scope(content1, "def __init__(self, name, number_of_commits)", False)[0], (11, 15), "test small normal case")
eq_ok(library.Rules.Filters.libs.ParseTree.get_function_scope(content2, r'def getValuesToInsert((.)*)', True)[0], (16, 17), "test small normal case")

#eq_ok(library.ParseTree.match_function("E", "def getColumsToInsert(self)", False, content1, diff1) , (), "Normal-case")


#Setup for test of not in same file class definitions
#print >> sys.stderr, library.ParseTree.match_function("A", r'def getValuesToInsert((.)*)', True, content2, diff1)
eq_ok(library.Rules.Filters.libs.ParseTree.match_function("E", "get_primary_key(self)", False, content2, diff1) , None, "Normal-case")
eq_ok(library.Rules.Filters.libs.ParseTree.match_function("E", r'def getValuesToInsert((.)*)', True, content2, diff1) , 1, "Normal-case")
eq_ok(library.Rules.Filters.libs.ParseTree.match_function("A", r'def getValuesToInsert((.)*)', True, content2, diff1) , 2, "Normal-case")
