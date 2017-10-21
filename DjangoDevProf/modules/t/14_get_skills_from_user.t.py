__author__ = 'freddy'

from TAP.Simple   import *
import sys
import subprocess
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(5)

user = User("Tester", 1222)
user2 = User("Tester5", 2323)
path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup_database_and_datas.sh"], cwd=path)
database = path + "devprof_test.db"

SqlClient.set_up(database)
user = User("Peter", 2323)
user.set_primary_key(22)
skills = SqlClient.get_skills_from_user_sum(user)

eq_ok(len(skills), 4, "number of skills is correct")
eq_ok(skills[0].skill, "Other/Deployment", "name of first skill is correct")
eq_ok(skills[0].experience, 23, "name of first of users is correct")
eq_ok(skills[3].skill, "Model/Admininterface", "name of first of users is correct")
eq_ok(skills[3].experience, 30, "Check if the sum up works")

