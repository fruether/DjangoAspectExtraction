__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/shipping/abstract_models.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/shipping/abstract_models.py
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'src/oscar/apps/shipping/abstract_models.py'
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
Three users have committed to that file
"""
eq_ok(len(dict.keys()), 3 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 1, "Make sure that one use has the two commits")


"""
The file has the skill Database/Model . And there was one line added and one line dropped so we can say that it should have 1 ea

    Github: https://github.com/django-oscar/django-oscar/commit/033b967168501b778155babfcfdde7e9afda037e#diff-708d1503bf58b65e606189d3a5a4722e
"""


_, name, experiece, _ = help.get_skills(5519 , filename)[0]
eq_ok(experiece, 1 , "There should be  1 ea")
eq_ok(name, "Model/Data" , "There should be  1 ea")



_, name, experiece, _ = help.get_skills(5519 , filename)[1]
eq_ok(experiece, 1 , "There should be  1 ea")
eq_ok(name, "Model/Data" , "There should be  1 ea")
