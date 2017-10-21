__author__ = 'freddy'

from TAP.Simple   import *
import library.Diff

plan(3)


with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample.diff", "r") as f:
    content = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample2.diff", "r") as f:
    content2 = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample3.diff", "r") as f:
    content3 = f.read()

with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample_just_add.diff", "r") as f:
    result = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample2_just_add.diff", "r") as f:
    result2 = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample3_just_add.diff", "r") as f:
    result3 = f.read()

eq_ok(library.Diff.filter_added_lines(content), result, "check if filter worked")
eq_ok(library.Diff.filter_added_lines(content2), result2, "check if filter worked")
eq_ok(library.Diff.filter_added_lines(content3), result3, "check if filter worked")


