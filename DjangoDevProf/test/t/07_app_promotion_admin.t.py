__author__ = 'freddy'



"""

The file that will be tested is 'src/oscar/apps/catalogue/admin.py'

    URL: https://github.com/django-oscar/django-oscar/blob/master/src/oscar/apps/catalogue/admin.py
"""

from TAP.Simple   import *
from lib import help

plan(9)

filename = 'src/oscar/apps/catalogue/admin.py'
help.load_database()



"""
The file was was touched by 7 commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 6.
Commits that just do a rename won't be touched.
"""

results = help.get_commits(filename)

eq_ok(len(results), 7 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
Six users have committed to that file
"""
eq_ok(len(dict.keys()), 5 , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], 3, "Make sure that one user has  two commits")


"""
The file should have the skill Model/Admininterface. In the class one line was deleted and one line was added. As a result the experience should be 1 and 1

    Github: https://github.com/django-oscar/django-oscar/commit/6867f6cb687045852b9d8b1679875e8cde9e5414#diff-9841d386bc1886216450c8088acdd5af

"""
_, name, experiece, _ = help.get_skills(5596 , filename)[0]

#Deleted
eq_ok(name, "Model/Admininterface", "Did we assigned it right")
eq_ok(experiece, 1 , "foud atoms")

_, name, experiece, _ = help.get_skills(5596 , filename)[1]
#Added
eq_ok(name, "Model/Admininterface", "Did we assigned it right")
eq_ok(experiece, 1, "foud atoms")

"""
Lets have a look at the other commit to the file. That time there were 11 lines (12 with empty) added. However the code is looking to the location of the last statement which is the return at line 52. Thus we will just count
the lines till that (Postion of last expression on the left side on right side is counted to be conservative). So we got a 6. Due to the fact that we merge with a average on that rule we get:
11 + 6 = 17 / 2 = 8.5 = 8 in int

    Github: https://github.com/django-oscar/django-oscar/commit/2d87b74dffb9b1a05f84b2a6d0bcc7235ef55fa7#diff-9841d386bc1886216450c8088acdd5af

"""
_, name, experiece, _ = help.get_skills(5423 , filename)[1]
#Added
eq_ok(name, "Model/Admininterface", "Did we assigned it right")

eq_ok(experiece, 8, "found atoms")

