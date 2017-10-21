import subprocess

__author__ = 'freddy'

from TAP.Simple   import *
import sys
import sqlite3
from modules import SqlClient
sys.path.append('../../')
from library.datas.User import User

#SetUp
plan(2)

user = User("Tester", 1222)
user2 = User("Tester5", 2323)
database = "/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/database/"
subprocess.call(["./setup.sh"], cwd=database)
database += "devprof_test.db"
#IF
SqlClient.set_up(database)
SqlClient.add_raw_data(user)
SqlClient.add_raw_data(user2)
SqlClient.close_connection()

#Then
conn = sqlite3.connect(database)
cursor = conn.cursor()
cursor.execute("Select * from " + user.get_table() + " order by " + user.get_primary_key() + " ASC")
result = cursor.fetchall()
#print >> sys.stderr, result[0][1]

id1 = result[0][0]
id2 = result[1][0]


ok(len(result) == 2 and result[0][1] == "Tester" and  result[0][2] == "1222", "Test1")
ok(result[1][1] == "Tester5" and  result[1][2] == "2323", "Test2")


#Clean Up
conn.close()
conn = sqlite3.connect(database)
cursor = conn.cursor()

clean_up = "DELETE FROM " + user.get_table() + " WHERE "+user.get_primary_key()+"=" + str(id1)
cursor.execute(clean_up)
clean_up = "DELETE FROM " + user.get_table() + " WHERE "+user.get_primary_key()+"=" + str(id2)
cursor.execute(clean_up)
conn.commit()

