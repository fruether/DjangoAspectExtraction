__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/promotions/models.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/promotions/models.py
"""

from TAP.Simple   import *
from lib import help

plan(9)

filename = 'src/oscar/apps/promotions/models.py'
help.load_database()



"""
The file was was touched by 3 commits and a three users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed.
Commits that just do a rename won't be touched.
"""

results = help.get_commits(filename)

eq_ok(len(results), 3 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Two users have committed to that file
"""
eq_ok(len(dict.keys()), 3 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[0], 1, "Make sure that one use has the two commits")


"""
The file should have the skill Model/Data. In the class four lines were deleted and four lines of code were added. As a result the experience should be 4 and 4

    Github: https://github.com/django-oscar/django-oscar/commit/4a712c450cbaf80516d78738b3ad01489b140850#diff-6cbf3b21965c0caab5d7e47800375255

"""
_, name, experiece, _ = help.get_skills(5671 , filename)[0]

#Deleted
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 4, "found atoms")

_, name, experiece, _ = help.get_skills(5671 , filename)[1]
#Added
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 4, "found atoms")

"""
Lets have a look at the other commit to the file. That time there were 2 adds and 2 drops in the class. We, however, just look at one

"""
_, name, experiece, _ = help.get_skills(5519 , filename)[0]
#Added
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 2, "foud atoms")

