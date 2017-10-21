__author__ = 'freddy'

from TAP.Simple   import *
import sys
import subprocess
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(4)


path = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup_database_and_datas.sh"], cwd=path)
database = path + "devprof_test.db"

SqlClient.set_up(database)
files = SqlClient.get_file_names()

eq_ok(len(files), 3, "check the length")
eq_ok(files[0], "/a/b/main.py", "Check content")
eq_ok(files[1], "/a/b/test.py", "Check content")
eq_ok(files[2], "/a/b/x.py", "Check content")
