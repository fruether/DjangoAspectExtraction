__author__ = 'freddy'



"""

The file that will be tested is 'tests/functional/customer/auth_tests.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/tests/functional/customer/auth_tests.py
"""

from TAP.Simple   import *
from lib import help

plan(10)

filename = 'tests/functional/customer/auth_tests.py'
help.load_database()



"""
The file was was touched by fifteen commits and six (five) users. The difference is because one user just authored whereas the other commited. We will count the author though because he has the skills
"""

results = help.get_commits(filename)

eq_ok(len(results), 15 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Five users have committed to that file
"""
eq_ok(len(dict.keys()), 6 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 7, "Make sure that one use has the two commits")


"""
The file has the skill Test/Generell . Three relevant lines were dropped and twelve lines were added. In fact all functions that start with test_ were taken into account

    Github: https://github.com/django-oscar/django-oscar/commit/8e02c1e48717f9836d7aaec55ed7cc4ed6139c31#diff-eec4ec10e12d175e715db747cd5bd2e2
"""

_, name, experiece, _ = help.get_skills(2517 , filename)[0]

eq_ok(name, "Test/Generell" , "There should be  1 ea")
eq_ok(experiece, 3 , "There should be  2 ea")

_, name, experiece, _ = help.get_skills(2517 , filename)[1]

eq_ok(name, "Test/Generell" , "There should be  1 ea")
eq_ok(experiece, 12 , "There should be one ea")

x = help.get_skills(5033 , filename)
_, name, experiece, _ = x[0]

ok(len(x) == 2)
eq_ok(experiece, 1, "make sure ea are found as expected")
eq_ok(name, "Test/Generell", "test generell")

