__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/dashboard/partners/forms.py'

    URL: https://github.com/django-oscar/django-oscar/commits/master/src/oscar/apps/dashboard/partners/forms.py
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'src/oscar/apps/dashboard/partners/forms.py'
help.load_database()



"""
The file was was touched by 4 commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 2.
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
Three  users have committed to that file
"""
eq_ok(len(dict.keys()), 3 , "X users have committed to the file")

values = sorted(dict.values())

eq_ok(values[-1], 1, "Make sure that one use has the two commits")


"""
The file has the skill Forms/Model . And there was one line deleted and two lines addded so we can say that it should have 1 ea and 2 ea

    Github: https://github.com/django-oscar/django-oscar/commit/f6027ac37ff46a8b6e777ecc547523c9dab77685#diff-2bb37b6be7baec2e57dd74863cd773a8
"""


_, name, experiece, _ = help.get_skills(5665 , filename)[0]
eq_ok(experiece, 1 , "There should be  1 ea")
eq_ok(name, "Forms/Model" , "There should be  1 ea")



_, name, experiece, _ = help.get_skills(5665 , filename)[1]
eq_ok(experiece, 2 , "There should be  2 ea")
eq_ok(name, "Forms/Model" , "There should be  1 ea")
