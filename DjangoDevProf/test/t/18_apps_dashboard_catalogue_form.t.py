__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/dashboard/partners/forms.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/dashboard/partners/forms.py
"""

from TAP.Simple   import *
from lib import help

plan(11)

filename = 'src/oscar/apps/dashboard/partners/forms.py'
help.load_database()



"""
The file was was touched by 3 commits and a three users. One of those was just a move. That is the reason why just 2 are stored in the database
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
Twp  users have committed to that file.
"""
eq_ok(len(dict.keys()), 3 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 1, "Make sure that one use has the three commits..the maximum")


"""
The file should have the skill Model/Forms. In the class six lines were added so ea should be 6.

    Github: https://github.com/django-oscar/django-oscar/commit/4b72a16cc8f735f518513812699eaf5592c5b9d2#diff-2bb37b6be7baec2e57dd74863cd773a8

"""
#One skill because no lines were deleted. One time model/data for add so 1 has to be the length
ok(len(help.get_skills(5638 , filename)) == 1)
_, name, experiece, _ = help.get_skills(5638 , filename)[0]

#Deleted
eq_ok(name, "Forms/Model", "Did we assigned it right")
eq_ok(experiece, 6, "foud atoms")

"""
Lets have a look at the other commit to the file. That time there were three two added and one line dropped in the relevant classes.

    GitHub: hhttps://github.com/django-oscar/django-oscar/commit/f6027ac37ff46a8b6e777ecc547523c9dab77685#diff-2bb37b6be7baec2e57dd74863cd773a8

"""
_, name, experiece, _ = help.get_skills(5665 , filename)[0]
#Added
eq_ok(name, "Forms/Model", "Did we assigned it right")
eq_ok(experiece, 1, "foud atoms")

_, name, experiece, _ = help.get_skills(5665 , filename)[1]
eq_ok(name, "Forms/Model", "Did we assigned it right")
eq_ok(experiece, 2, "found atoms")

#Just those two skils should be there (two times Model/form once for add and one for drop=
ok( len(help.get_skills(5665 , filename)) == 2)