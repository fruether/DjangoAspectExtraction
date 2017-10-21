__author__ = 'freddy'



"""

The file that will be tested is 'tests/integration/shipping/model_method_tests.py'

    URL: https://github.com/django-oscar/django-oscar/commits/master/tests/integration/shipping/model_method_tests.py

"""

from TAP.Simple   import *
from lib import help

plan(8)

filename = 'tests/integration/shipping/model_method_tests.py'
help.load_database()


"""
The file was touched by 15 commits and by four users. Lets check if that is true

"""

results = help.get_commits(filename)

eq_ok(len(results), 15 , "Do we have all five commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Five users have committed to that file
"""
eq_ok(len(dict.keys()), 4 , "Two users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 7, "Make sure that one use has the seven commits")


"""

"""
_, name, experiece, _ = help.get_skills(5324 , filename)[0]

eq_ok(name, "Test/Django", "Did we assigned it right")
eq_ok(experiece, 13, "foud atoms")



"""
Now lets have a look at a border case. In one commit there is a rename. The file should not be seen as any skills with that new name because no lines were added
    Commit: https://github.com/django-oscar/django-oscar/commit/bd77a9e6aaf17906575b1f76f3f93433d26650ba#diff-0729b70f422886127ac05f10a4154c19



"""

result = help.get_skills(3424  , filename)

eq_ok(len(result), 0 , "No skills should be found on that version")
"""
Before the file was renamed some lines were dropped. In fact in the class TestCase so we should find a specific Django test. The added lines are 56 in the class
"""
_,name, atoms,_ = help.get_skills(3424  , 'tests/unit/shipping_tests.py')[0]

eq_ok(name, "Test/Django", "It should be that skill")

eq_ok(atoms, 56, "It should have collected that experience")
