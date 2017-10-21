__author__ = 'freddy'



"""

The file that will be tested is 'sites/_fixtures/comms.json'

    URL: https://github.com/django-oscar/django-oscar/blob/master/sites/_fixtures/comms.json

"""

from TAP.Simple   import *
from lib import help

plan(5)

filename = 'sites/_fixtures/comms.json'
help.load_database()


"""
The file was touched by 2 commits and by one users. Lets check if that is true

"""

results = help.get_commits(filename)

eq_ok(len(results), 2 , "Do we have all five commits as expected")

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

eq_ok(values[0], 2, "Make sure that one use has the two commits")



"""
Lets now check if the right skills were applied.

We can see that the foldername is fixture but with an underscore "_". Therefore our Rule of identfying a Fixture does not apply to it. We can change it though. But our approach is to be conservative that
 is why we did not add it yet?
However inside the fixture are template tags because they will be written to the database. That is the reason why those skills are found

Well in that context not but the question is do we want to be conservative or not?

"""

_,skill, experience,_ = help.get_skills(2257  , filename)[0]

eq_ok(experience, 8, "Template found")
eq_ok(skill, "Other/Templates", "Template found")
