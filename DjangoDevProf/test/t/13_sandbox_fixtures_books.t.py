__author__ = 'freddy'



"""

The file that will be tested is 'sites/sandbox/fixtures/books.computers-in-fiction.csv'

    URL: https://github.com/django-oscar/django-oscar/blob/master/sites/sandbox/fixtures/books.computers-in-fiction.csv
"""

from TAP.Simple   import *
from lib import help

plan(5)

filename = 'sites/sandbox/fixtures/books.computers-in-fiction.csv'
help.load_database()



"""
The file was was touched by 1 commit and one user.
"""

results = help.get_commits(filename)

eq_ok(len(results), 1 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Two users have committed to that file
"""
eq_ok(len(dict.keys()), 1 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 1, "Make sure that one use has the two commits")


"""
The file has the skill Database/Fixture . But on the first commit just the imports were changed so there should be no skills at all

    Github: https://github.com/django-oscar/django-oscar/commits/master/sites/sandbox/fixtures/books.computers-in-fiction.csv

    The fixture rule also takes the average value as well. If just one filter returns true it will be cut into half
"""

_, name, experiece, _ = help.get_skills(2993 , filename)[0]


eq_ok(name, "Database/Fixture" , "There should be  1 ea")

eq_ok(experiece, 43 , "There should be  3 ea")