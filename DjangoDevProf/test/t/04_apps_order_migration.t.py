__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/order/migrations/0003_auto_20150113_1629.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/order/migrations/0003_auto_20150113_1629.py
"""

from TAP.Simple   import *
from lib import help

plan(6)

filename = 'src/oscar/apps/order/migrations/0003_auto_20150113_1629.py'
help.load_database()
"""
Test 1

Make sure that of that file different FileVersions exist. Some entries should be double per commit because if they are modified they maybe appear once
for  deleted and once for added content

"""

ok(len(help.get_files(filename)) > 0)


"""
The file was added by 1 commit and as expected by one user. Lets check if that is true

"""

results = help.get_commits(filename)

eq_ok(len(results), 1 , "Do we the commit as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Two users have committed to that file
"""
eq_ok(len(dict.keys()), 1 , "Two users have commited")

values = sorted(dict.values())

eq_ok(values[0], 1, "Make sure that one use has the two commits")


"""
The file should have the skill Migration and about 7 lines because the last exression will return it linenumber independent how long the subexpressions are
"""
_, name, experiece, _ = help.get_skills(5392 , filename)[0]

eq_ok(name, "Database/Migration", "Did we assigned it right")
eq_ok(experiece, 7, "foud atoms")

