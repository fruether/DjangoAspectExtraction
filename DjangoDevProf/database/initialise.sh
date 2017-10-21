#!/bin/sh

rm -f devprof.db
cat CreateTables.sql | sqlite3 devprof.db