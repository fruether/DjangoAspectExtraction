__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/core/compat.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/core/compat.py
"""

from TAP.Simple   import *
from lib import help

plan(4)

filename = 'src/oscar/core/compat.py'
help.load_database()



"""
The file was was touched by 7 commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 5.
Commits that just do a rename won't be touched.
"""

results = help.get_commits(filename)

eq_ok(len(results), 6 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Four users have committed to that file
"""
eq_ok(len(dict.keys()), 4 , "Four users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 3, "Make sure that one use has the two commits")


"""
The file is not specific to a Django skill

    Github: https://github.com/django-oscar/django-oscar/commits/master/src/oscar/core/compat.py

"""
x = help.get_skills_by_name(filename)
eq_ok(len(x), 0 , "There should be no skill")



