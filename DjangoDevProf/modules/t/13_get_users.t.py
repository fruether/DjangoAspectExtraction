
__author__ = 'freddy'

from TAP.Simple   import *
import sys
import subprocess
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(2)

user = User("Tester", 1222)
user2 = User("Tester5", 2323)
path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup_database_and_datas.sh"], cwd=path)
database = path + "devprof_test.db"

SqlClient.set_up(database)
users = SqlClient.get_users();

eq_ok(len(users), 4, "number of users is correct")
eq_ok(users[0].name, "Peter", "name of first of users is correct")

