__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/catalogue/admin.py'

    URL: https://github.com/django-oscar/django-oscar/commits/master/src/oscar/templates/oscar/checkout/shipping_address.html
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'src/oscar/templates/oscar/checkout/shipping_address.html'
help.load_database()



"""
The file was was touched by 4 commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 3.
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
eq_ok(len(dict.keys()), 2 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 2, "Make sure that one use has the two commits")


"""
The file should have the skill . In the class one time {%  %}  was deleted and one {%   %}was added. As a result the experience should be 1 and 1

    Github: https://github.com/django-oscar/django-oscar/commit/8484478065769193334d880f23cb103e52fff523#diff-ab1908dabe36662aa026cfa12cc4808d

"""
_, name, experiece, _ = help.get_skills(5555 , filename)[0]

#Deleted
eq_ok(name, "Other/Templates", "Did we assigned it right")
eq_ok(experiece, 1 , "foud atoms")

_, name, experiece, _ = help.get_skills(5555 , filename)[1]
#Added
eq_ok(name, "Other/Templates", "Did we assigned it right")
eq_ok(experiece, 1, "foud atoms")


