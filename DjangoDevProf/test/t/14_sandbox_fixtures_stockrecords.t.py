__author__ = 'freddy'



"""

The file that will be tested is 'sites/sandbox/fixtures/multi-stockrecord-product.json'

    URL: https://github.com/django-oscar/django-oscar/blob/master/sites/sandbox/fixtures/multi-stockrecord-product.json
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'sites/sandbox/fixtures/multi-stockrecord-product.json'
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
Three users have committed to that file
"""
eq_ok(len(dict.keys()), 3 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 3, "Make sure that one use has the two commits")


"""
The file has the skill Database/Fixture .Two lines were dropped and one was added. Node that the filter will return the average

    Github: https://github.com/django-oscar/django-oscar/commit/1d008d608572d7f74be2ef5beb2de7b0d038486e#diff-6eee9e4ee97e3dfd96b43240fc62a98d
"""

_, name, experiece, _ = help.get_skills(4212 , filename)[0]

eq_ok(name, "Database/Fixture" , "There should be  1 ea")
eq_ok(experiece, 2/2 , "There should be  2 ea")

_, name, experiece, _ = help.get_skills(4212 , filename)[1]

eq_ok(name, "Database/Fixture" , "There should be  1 ea")
eq_ok(experiece, 1 , "There should be one ea")

