#Test

This folder contains all the test cases to verify the result of the analyze of the Djnango-Oscar project on Github


All of those test are of follow form:


```

__author__ = 'freddy'



"""

The file that will be tested is 'The path to the file'

    URL: The URL on Githhun
"""

from TAP.Simple   import *
from lib import help

plan(7)

filename = 'path to filename'
help.load_database()



"""
The file was was touched by (number of commits) commits and a four users. One of those commits was just moving the file and did not change any lines. Therefore that commit is not listed and we just check for 2.
Commits that just do a rename won't be touched.
"""

results = help.get_commits(filename)

eq_ok(len(results), 2 , "Did we got the commits as expected")

dict = {}

for (id, date, name, user) in results:
    if user in dict.keys():
        dict[user] += 1
    else:
        dict[user] = 1

"""
X users have committed to that file
"""
eq_ok(len(dict.keys()), X , "One users have commited")

values = sorted(dict.values())

eq_ok(values[-1], maxCommitsByAUser, "Make sure that one use has the two commits")


"""
The file has the skill Category/Skill . And there was X line(s) deleted and Y line(s) addded so we can say that it should have X ea and Y ea

    Github: URL to the commit and its diff on Github
"""


_, name, experiece, _ = help.get_skills(CommitID , filename)[0]
eq_ok(experiece, Y , "There should be  1 ea")
eq_ok(name, "Category/Skill" , "There should be  1 ea")



_, name, experiece, _ = help.get_skills(CommitID , filename)[1]
eq_ok(experiece, X , "There should be  2 ea")
eq_ok(name, "Category/Skill" , "There should be  1 ea")
```