__author__ = 'freddy'



"""

The file that will be tested is 'tests/integration/catalogue/reviews/model_tests.pyy'

    URL: https://github.com/django-oscar/django-oscar/blob/master/tests/integration/catalogue/reviews/model_tests.py
"""

from TAP.Simple   import *
from lib import help

plan(10)

filename = 'tests/integration/catalogue/reviews/model_tests.py'
help.load_database()



"""
The file was was touched by five commits and three users.
"""

results = help.get_commits(filename)

eq_ok(len(results), 5 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Five users have committed to that file
"""
eq_ok(len(dict.keys()), 3 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 2, "Make sure that one use has the two commits")


"""
The file has the skill Test/Generell . Eight relevant lines were dropped and eight lines were added.

    Github: https://github.com/django-oscar/django-oscar/commit/0a1b4a60c7807e115ed98809e930b9505c7ba00c#diff-e541aeb2a07c43f22678cede1de25d6c
"""

_, name, experiece, _ = help.get_skills(4030 , filename)[0]

eq_ok(name, "Test/Django" , "There should be  1 ea")
eq_ok(experiece, 8 , "There should be  2 ea")

_, name, experiece, _ = help.get_skills(4030 , filename)[1]

eq_ok(name, "Test/Generell" , "There should be  1 ea")
eq_ok(experiece, 8 , "There should be one ea")

x = help.get_skills(3305 , filename)
_, name, experiece, _ = x[0]

#Just two skill found Generell and Django as expected?
ok(len(x) == 2)

#It is a "A" that means the file did not exist before. Therefore (51 - 7) will be calculated hence the class starts at line 8 and ends at line 51.
eq_ok(experiece, 44, "make sure ea are found as expected")
eq_ok(name, "Test/Django", "test generell")

