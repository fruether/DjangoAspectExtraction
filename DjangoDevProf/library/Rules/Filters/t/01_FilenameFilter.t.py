__author__ = 'freddy'
from TAP.Simple   import *
import sys
sys.path.append("../Filters")
import FilenameFilter

#import library.Rules.Filter.FilenameFilter


#The diffs to test:
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample2.diff", "r") as f:
    content2 = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample3.diff", "r") as f:
    content3 = f.read()

##The Filters to test
ff1 = FilenameFilter.FilenameFilter("t.xml", "")
ff2 = FilenameFilter.FilenameFilter("Case", "middle")
ff3 = FilenameFilter.FilenameFilter("Test", "start")
plan(6)

#match_filename_somewhere
x = ff1.apply_filter("", "/a/b/c/t.xml", "", "")
eq_ok(x , 0 , "Normal case - match_filename_filter - 1")
eq_ok(ff1.apply_filter("", "/a/b/c/t.", "", ""), None, "Error case in match filename")

eq_ok(ff2.apply_filter("", "/a/b/c/d/e/TestCase.java", content2, ""), 2, "Normal case - match_filename_middle with filter and diff -1")
eq_ok(ff2.apply_filter("", "/a/b/c/d/e/TestCase.java", content3, ""), 7, "Normal case - match_filename_middle - 2")

#match_start
eq_ok(ff3.apply_filter("", "/a/b/c/d/e/TestCase.java", "", ""), 0, "Normal case - match_start - 1")
eq_ok(ff3.apply_filter("", "/a/b/c/d/e/BlahCase.java", "", ""), None, "error case - match_start - 2")
