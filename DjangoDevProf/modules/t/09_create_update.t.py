__author__ = 'freddy'

from TAP.Simple   import *
import modules.SqlClient

plan(2)

eq_ok(modules.SqlClient.create_update("users",["Name", "Number"], [ "1", "3"], "key", 2), "UPDATE users SET Name='1', Number='3' WHERE key=2", "normalfall")

eq_ok(modules.SqlClient.create_update("users",["Name", "Number"], [1, "2"], "id", 3), "UPDATE users SET Name=1, Number='2' WHERE id=3", "normalfall")
