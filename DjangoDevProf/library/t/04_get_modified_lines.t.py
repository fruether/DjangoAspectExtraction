__author__ = 'freddy'


from TAP.Simple   import *
import library.Diff

import sys
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample.diff", "r") as f:
    content = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample2.diff", "r") as f:
    content2 = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample3.diff", "r") as f:
    content3 = f.read()
with open("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/library/t/files/diff_sample4.diff", "r") as f:
    content4 = f.read()


plan(4)

eq_ok(library.Diff.get_modified_lines(content4), [413, 414, 415], "")

eq_ok(library.Diff.get_modified_lines(content), [1, 2, 3, 4, 5, 14, 17, 26, 27, 28], "Basic case with example from wikipedia")
eq_ok(library.Diff.get_modified_lines(content2), [77, 78], "Basic case with example without a newline")
eq_ok(library.Diff.get_modified_lines(content3), [13, 20, 21, 22, 28, 34, 46], "Basic case with example without a newline in lomger")


#[13, 20, 21, 22, 28, 34, 46]