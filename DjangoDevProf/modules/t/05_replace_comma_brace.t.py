__author__ = 'freddy'

from TAP.Simple   import *
import modules.SqlClient

plan(2)

eq_ok(modules.SqlClient.replace_comma_brace(","), ")" , "grenzfall")
eq_ok(modules.SqlClient.replace_comma_brace("INSERT Table (a,c,f,"), "INSERT Table (a,c,f)" , "normalfall")
