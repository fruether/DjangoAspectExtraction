__author__ = 'freddy'



"""

The file that will be tested is 'tests/functional/basket/manipulation_tests.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/tests/functional/basket/manipulation_tests.py

"""

from TAP.Simple   import *
from lib import help

plan(6)

filename = 'tests/functional/basket/manipulation_tests.py'
help.load_database()
"""
Test 1

Make sure that of that file different FileVersions exist. Some entries should be double per commit because if they are modified they maybe appear once
for  deleted and once for added content

"""

ok(len(help.get_files(filename)) > 0)


"""
The file was added by 5 commits and by two users. Lets check if that is true

"""

results = help.get_commits(filename)

eq_ok(len(results), 5 , "Do we have all five commits as expected")

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

eq_ok(values[0], 2, "Make sure that one use has the two commits")


"""
The file should have the skill Generel/test. And after we had a look to the commit with the message: Fix bug with variant AddToBasket forms
we were sure that it has the Skill Test/Generel and the count is 8. Because 8 not empty lines of code were added

    GiThub: https://github.com/django-oscar/django-oscar/commit/c5a60df61d38f0d2b6388960f26a8d4b2af56094#diff-553a1e1c8409fcbd007fd92f0dded167
"""
_, name, experiece, _ = help.get_skills(4678 , filename)[0]
eq_ok(name, "Test/Generell", "Did we assigned it right")
eq_ok(experiece, 8, "foud atoms")

