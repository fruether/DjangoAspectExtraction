__author__ = 'freddy'


"""

The file that will be tested is 'src/oscar/apps/offer/abstract_models.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/offer/abstract_models.py
"""

from TAP.Simple   import *
from lib import help

plan(13)

filename = 'src/oscar/apps/offer/abstract_models.py'
help.load_database()



"""
The file was was touched by 10 commits and a three users. One of those was just a move. That is the reason why just 9 are stored in the database
"""

results = help.get_commits(filename)
eq_ok(len(results), 10 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Three  users have committed to that file.
"""
eq_ok(len(dict.keys()), 5 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 5, "Make sure that one use has the three commits..the maximum")


"""
The file should have the skill Model/Data. In the class three lines were deleted, which were in a Mode class.

In generell  three classes of the size 236 + 128 + 81 were created. The spaces are included in that calculation and are up to 445. Due to the spaces sum is smaller. The 403 is the database seem reasonable

    Github: https://github.com/django-oscar/django-oscar/commit/9283145db10402e02a53cd032fc955428e38f46a#diff-a5e122ee393a84313536b15e6ba9fd34

"""
#Two skills. One time model/data for add and once for deleted lines
ok(len(help.get_skills(5537 , filename)) == 2)
_, name, experiece, _ = help.get_skills(5537 , filename)[0]

#Deleted
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 4, "foud atoms")

_, name, experiece, _ = help.get_skills(5537 , filename)[1]
#Added
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 403, "found experience atoms")

"""
Lets have a look at the other commit to the file. That time there were three lines added and six lines dropped in the relevant classes.

    GitHub: https://github.com/django-oscar/django-oscar/commit/5b2b50e112dc013a252dbfb672f9d01ffc3e5203#diff-a5e122ee393a84313536b15e6ba9fd34

"""
_, name, experiece, _ = help.get_skills(5592 , filename)[0]
#Added
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 6, "foud atoms")

_, name, experiece, _ = help.get_skills(5592 , filename)[1]
eq_ok(name, "Model/Data", "Did we assigned it right")
eq_ok(experiece, 3, "foud atoms")

#Just those two skils should be there
ok( len(help.get_skills(5592 , filename)) == 2)