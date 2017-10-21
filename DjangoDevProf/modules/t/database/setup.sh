#!/bin/sh

rm -f devprof_test.db

cat $(pwd)/../../../database/CreateTables.sql | sqlite3 devprof_test.db