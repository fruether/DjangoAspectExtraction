#!/bin/sh

rm -f devprof_test.db

echo $(cat $(pwd)/../../../database/CreateTables.sql)  $(cat Users.sql) $(cat Commits.sql) $(cat File.sql) $(cat Skill.sql)|  sqlite3 devprof_test.db


