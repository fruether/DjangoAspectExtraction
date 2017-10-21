__author__ = 'freddy'

from TAP.Simple   import *
import modules.SqlClient

plan(0)

#eq_ok(modules.SqlClient.create_insert("users",["UserID", "Name", "Number"], ["1", "2", "3"]), "INSERT INTO users(UserID,Name,Number) VALUES ('1','2','3')", "normalfall")

#eq_ok(modules.SqlClient.create_insert("users",["UserID", "Name", "Number"], [1, "2", 3]), "INSERT INTO users(UserID,Name,Number) VALUES (1,'2',3)", "normalfall")
