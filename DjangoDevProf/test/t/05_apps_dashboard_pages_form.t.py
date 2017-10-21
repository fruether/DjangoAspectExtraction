__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/dashboard/reports/forms.py'

    URL: https://github.com/django-oscar/django-oscar/commits/master/src/oscar/apps/dashboard/reports/forms.py
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'src/oscar/apps/dashboard/reports/forms.py'
help.load_database()



"""
The file was was touched by 1 commit and as expected by one user. Lets check if that is true
Indeed it was moved once but our code does not count a plain move because that is irrelevant for the assignment of a skill

"""

results = help.get_commits(filename)

eq_ok(len(results), 2 , "Do we the commit as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Two users have committed to that file
"""
eq_ok(len(dict.keys()), 2 , "Two users have commited")

values = sorted(dict.values())

eq_ok(values[0], 1, "Make sure that one use has the one commits")


"""
The file should have the skill Forms/Html. In the class two lines were deleted and three lines were added. As a result the experience should be 2 and 3

    Github: https://github.com/django-oscar/django-oscar/commit/9dd9bc1f253a83ab646214c524b5a9f1de361af9#diff-1a8914e6002de4cc97999ac2acb5ef95

"""
_, name, experiece, _ = help.get_skills(5394 , filename)[0]

#Deleted
eq_ok(name, "Forms/HTML", "Did we assigned it right")
eq_ok(experiece, 2, "foud atoms")

_, name, experiece, _ = help.get_skills(5394 , filename)[1]
#Added
eq_ok(name, "Forms/HTML", "Did we assigned it right")
eq_ok(experiece, 3, "foud atoms")
