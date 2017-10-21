__author__ = 'freddy'

from TAP.Simple   import *
import sys
import subprocess
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(8)


path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup_database_and_datas.sh"], cwd=path)
database = path + "devprof_test.db"

SqlClient.set_up(database)

users, commits, files, skills = SqlClient.database_to_object()


eq_ok(len(skills), 8, "Check all values there for skills, files, users ")
eq_ok(len(users), 4, "Check all values there for skills, files, users")
eq_ok(len(commits), 4, "Check all values there for skills, files, users")
eq_ok(len(files), 4, "Check all values there for skills, files, users")



eq_ok(skills[0].skill, "Other/Deployment", "name of first skill is correct")
eq_ok(users[1].name, "Wolfgang", "name of first of users is correct")

eq_ok(commits[2].message, "ADDED Y", "name of first of users is correct")
eq_ok(files[3].commit.message, "Updated Y and X", "Check if the link works")

