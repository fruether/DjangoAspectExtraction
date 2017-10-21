__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/dashboard/catalogue/forms.py'

    URL: https://github.com/django-oscar/django-oscar/commits/master/src/oscar/apps/dashboard/catalogue/forms.py
"""

from TAP.Simple   import *
from lib import help

plan(8)

filename = 'src/oscar/apps/dashboard/catalogue/forms.py'
help.load_database()



"""
The file was was touched by 11 commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 10.
Commits that just do a rename won't be touched.
"""

results = help.get_commits(filename)

eq_ok(len(results), 12 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Two users have committed to that file
"""
eq_ok(len(dict.keys()), 5 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 4, "Make sure that one use has the two commits")


"""
The file has the skill Forms/Model . But on the first commit just the imports were changed so there should be no skills at all

    Github: https://github.com/django-oscar/django-oscar/commit/da6008d111315b2116913fe7893a9324dbcf06d5#diff-d780dd2c05435a8e91797f4ff1b333ae
"""


x= help.get_skills(5467 , filename)
eq_ok(len(x), 0 , "There should be  1 ea")



"""
The file has the skill Forms/Model . 4 lines were added to the class; one is empty, and hence there should be 3 adds

    Github: https://github.com/django-oscar/django-oscar/commit/c1ae543291f4fabe8f23e927b3d2837c430bd316#diff-d780dd2c05435a8e91797f4ff1b333ae

    and

    GitHub: https://github.com/django-oscar/django-oscar/commit/55fb961011736d75f7a1c4225e8948e096d7c9da#diff-d780dd2c05435a8e91797f4ff1b333ae

    Two lines were deleted. Furthermore  the beginning of the last expression will be taken into account. Therefore the class ends at line 116 and not line 120. Therefore we will count
    that long definition just as one ea.
"""


_, name, experiece, _ = help.get_skills(5646 , filename)[0]


eq_ok(experiece, 3 , "There should be  3 ea")
eq_ok(name, "Forms/Model" , "There should be  1 ea")

_, name, experiece, _ = help.get_skills(5457 , filename)[0]

eq_ok(name, "Forms/Model" , "There should be  1 ea")
eq_ok(experiece, 2 , "There should be  3 ea")