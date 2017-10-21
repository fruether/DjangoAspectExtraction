#!/usr/bin/env python

import subprocess
import os
import sys

if len(sys.argv) < 2:
    mode = "test"
else:
    mode = sys.argv[1]

makefiles =  [root
             for root, dirs, files in os.walk(os.getcwd())
             for name in files
             if name.endswith(("Makefile"))]

exit = 0
for makefile in makefiles:
    if makefile == os.getcwd() or makefile.find(os.path.join(os.getcwd(), "output")) != -1 or makefile.find(os.path.join(os.getcwd(), "modules/t/repo")) != -1:
        continue
    print "Execute: " + makefile
    exit += subprocess.call(["make", mode], cwd=makefile)


if exit != 0:
    print >> sys.stderr, "A lot test have failed....Make sure you have run make install before otherwise you got a problem: " + str(exit)
    sys.exit(1)