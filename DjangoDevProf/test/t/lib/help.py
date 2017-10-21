__author__ = 'freddy'

import sqlite3
import sys

cursor = None
conn = None



def load_database(database = "../database/devprof.db"):
    global cursor, conn
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    print("Connected to database")


def get_commits(filename):
    global cursor
    result = []

    if cursor == None:
        print >> sys.stderr, ("Make sure you are connected to database")
        return
    query = "Select * from GitCommit where CommitId IN (Select CommitId from FileVersion where name=?);"
    cursor.execute(query, [filename])
    for row in cursor:
        result.append((row[0], row[1], row[2], row[3]))
    return result

def get_files(filename):
    global cursor
    result = []

    if cursor == None:
        print >> sys.stderr, ("Make sure you are connected to database")
        return
    query = " Select * from FileVersion where name= ?;"
    cursor.execute(query, [filename])
    for row in cursor:
        result.append((row[0], row[1], row[2], row[3]))
    return result



def get_skills(commitId, filename):

    global cursor
    results = []

    if cursor==None:
        print >> sys.stderr, ("Make sure you are connected to database")
        return

    query = "Select * from Skill where FileVersionId IN (Select FileVersionId from FileVersion where CommitId=? and name=?);"
    cursor.execute(query, [commitId, filename])
    for row in cursor:
        results.append((row[0], row[1], row[2], row[3]))
    return results

def get_skills_by_name(filename):

    global cursor
    results = []

    if cursor==None:
        print >> sys.stderr, ("Make sure you are connected to database")
        return

    query = "Select * from Skill where FileVersionId IN (Select FileVersionId from FileVersion where name=?);"
    cursor.execute(query, [filename])
    for row in cursor:
        results.append((row[0], row[1], row[2], row[3]))
    return results

