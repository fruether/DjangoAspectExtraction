__author__ = 'freddy'

from TAP.Simple   import *
import sys
import subprocess
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(3)


path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup_database_and_datas.sh"], cwd=path)
database = path + "devprof_test.db"

SqlClient.set_up(database)
results = SqlClient.get_skills_in_files("/a/b/main.py")

eq_ok(len(results), 3, "check the length")
skill1, loc = results[0]
eq_ok(skill1, "Other/Deployment", "Check content")

results = SqlClient.get_skills_in_files("/a/b/x.py")
skill1, loc = results[2]
eq_ok(skill1, "Forms/HTML", "Check content")

