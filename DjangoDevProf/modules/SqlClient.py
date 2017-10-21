__author__ = 'freddy'
import sqlite3
import sys
sys.path.append('library')
sys.path.append('../')

#from library.datas.User import User
#from library.datas.RawData import RawData
from library.datas.User import User
from library.datas.RawData import RawData
from library.datas.Skill import Skill
from library.datas.Commit import Commit
from library.datas.File import File
import logging
cursor = None
conn = None

"""
This function will add an object of the type RawData into the database. What database that is will be specified in set_up function
    data : Object of type RawData that should be added
    raise: RuntimeError when database is not connected
"""
def add_raw_data(data):
    global cursor
    if cursor == None:
        logging.error("The database is not connected")
        raise RuntimeError("Database is not connected")
    if isinstance(data, RawData):
        try:
            id = execute_insert(data.get_table(), data.getColumsToInsert(), data.getValuesToInsert())
            #execute_statement(sql_query)
            data.set_primary_key(id)
            logging.debug("I am writing raw data to the database %s", data.get_table())
        except sqlite3.OperationalError as x:
            logging.error("The was an error %s while writing ", x.message)
            exit(1)
    else:
        logging.error("Library can just handle instances of RawData but we found %s" , str(type(data)))
        raise RuntimeError("Library can just handle instances of RawData")
    return

"""

Take the path to a sqlite3 file as argument and setups the database
    database: The path to the file as string

"""
def set_up(database) :
    global cursor, conn
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    logging.info("Connected to database")

"""
This function will execute the sql statement that was given as argument (as sting)
"""
def execute_statement(sql):
    cursor.execute(sql)
    conn.commit()

"""
This function will execute a Insert statement. The table and column names as well as the values will be given as argument to the function
    table: A string that describes the tablename
    columns: A list of strings which are the name of the columns
    values: A list of strings that contain the values

    Return: This function returns the id of the added row
"""
def execute_insert(table, columns, values):

    statement = "INSERT INTO " + table +"("
    for column in columns:
        statement += column + ","
    statement = replace_comma_brace(statement)
    statement += " VALUES ("

    for _ in values:
        statement += "?,"

    statement = replace_comma_brace(statement)
    statement += ";"
    cursor.execute(statement, values)
    conn.commit()
    return cursor.lastrowid

"""
This function will update a column in the database. In fact the column that saves the data object which is of type RawData
    data:  The object of type RawData that should be updated
    raise: Exception if the database is not connected
"""
def update_raw_data(data):
    if cursor == None:
        raise RuntimeError("Database is not connected")
    if isinstance(data, RawData):
        sql_query = create_update(data.get_table(), data.getColumsToInsert(), data.getValuesToInsert(), data.get_primary_key(), data.id)
        execute_statement(sql_query)
    else:
        raise RuntimeError("Library can just handle instances of RawData")

"""
    This function will create the update statement as a string. It takes the table, column, names and id as values
    table: A string of the tablename
    columns: A list of strings that describes the column names
    values: A list that contains the values that should be added
    id: An Integer that contains the key

    return: The resulting SQL query as a string
"""
def create_update(table, columns, values, column, id):
    statement = "UPDATE " + table +" SET "
    for i in range(0, len(columns)):
        value = values[i]
        if isinstance(value, int):
            statement += columns[i] + "=" + str(value) + ", "
        else:
            statement += columns[i] + "='" + value + "', "

    statement = statement[:-2]
    statement += " WHERE " + column + "=" + str(id)
    return statement

"""
This function will take a string and replace the last , with a ). This is in fact needed because e.g. the for loops of create_update will always add a , even in the last query
  str = A string which ends with  a ","
  return A string where the last , is replaced with a )
"""
def replace_comma_brace(str):
    new = list(str)
    new[-1] = ')'
    return ''.join(new)
"""
This function will close the connection to the database
"""
def close_connection():
    global conn
    conn.close()
"""
This function will get all users (or the user specified in the first parameter) in the database as object of the type User
    id : The id of the user that should be returned. None will return all
    return: A list of all the requested users as list
"""
def get_users(id = None):
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    if not id:
        statement = "Select * from Contributor;"
    else:
        statement = "Select * from Contributor where id = " + id + ";"

    cursor.execute(statement)
    for row in cursor:
        user = User(row[1], row[2])
        user.set_primary_key(row[0])
        results.append(user)
    return results
"""
This function will return all the skills that a specifc user has collected
    user: Object of the type user of which the skills should be returned (The id field should be set and valid)
    return: A list of Skill objects that represent all the skills a user has

"""
def get_skills_from_user_sum(user):
    statement = """ Select
                        Skill.SkillId, Skill.Name, sum(Skill.Experience)
                    from Gitcommit, FileVersion, Skill
                    where
                        Gitcommit.UserId = %i and
                        FileVersion.CommitId = Gitcommit.CommitId and
                        Skill.FileVersionId = FileVersion.FileVersionId
                        group by Skill.Name
                        order by Skill.SkillId;
                        """
    global cursor
    results = []
    if cursor == None:
        logging.error("Database is not connected")
        raise RuntimeError("Database is not connected")
    cursor.execute(statement % user.id)
    for row in cursor:
        skill = Skill(row[1], row[2])
        skill.set_primary_key(row[0])
        results.append(skill)
    return results

"""
This functions takes the complete database and fits them into the representing objects
    return: Four lists that contain Users, Commits, Files, or Skill objects with the values of the database
"""
def database_to_object():
    users = get_user_objects()
    result_commits = []
    result_files = []
    result_skills = []

    for user in users:
        commits = get_commit_objects(user)
        result_commits += commits
        for commit in commits:
            files = get_file_objects(commit)
            result_files += files
            for file in files:
                skills = get_skills_from_file(file)
                file.set_skills(skills)
                result_skills += skills
            commit.set_files(files)
        user.set_commits(commits)
    logging.info("Converted the database into object oriented form")
    return users, result_commits, result_files, result_skills

"""
This function will return all the users as User objects which are in the database

    return: A list of User objects that contain the values of the database
"""
def get_user_objects():
    # Contributor(UserID INTEGER PRIMARY KEY ASC, Name STRING, NumberOfCommits TEXT)
    statement = "Select UserId, Name, NumberOfCommits from Contributor order by UserId"
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement)
    for row in cursor:
        user = User(row[1], row[2])
        user.set_primary_key(row[0])
        results.append(user)
    return results

"""
This function will return all the commits in the database as Commit objects which were done by a specific user
    return: A list of Commit objects that represent the commits in the database
"""
def get_commit_objects(user):
    #CREATE TABLE Gitcommit(CommitId INTEGER PRIMARY KEY ASC, timestemp Date, Message VARCHAR(200), UserId INTEGER,  FOREIGN KEY(UserId) REFERENCES Contributor(UserID));
    statement = "Select CommitId, timestemp, Message from Gitcommit where UserId = %i order by CommitId"
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement % user.id)
    for row in cursor:
        commit = Commit(row[1], user, row[2])
        commit.set_primary_key(row[0])
        results.append(commit)
    return results

"""
This function will return all the File objects that are stored in the database and were part of a specific commit
    commit : An object of the Commit type that has a valid id in the database
    return: A list of File objects that all were touched by the specified commit
"""
def get_file_objects(commit):
#CREATE TABLE FileVersion(FileVersionId INTEGER PRIMARY KEY ASC, Name TEXT, LOC INTEGER, CommitId INTEGER, FOREIGN KEY(CommitId) REFERENCES Gitcommit(CommitId));
    statement = "Select FileVersionId, Name, LOC from FileVersion where CommitId = %i order by FileVersionId"
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement % commit.id)
    for row in cursor:
        file = File(row[1], row[2], commit)
        file.set_primary_key(row[0])
        results.append(file)
    return results

"""
This function will return all the skills (as Skill objects) that were in a specific file
    file: A file object with a valid database id. ALl matching Skills to that file will be returned (node FileVersion)
    return: A list of skills
"""
def get_skills_from_file(file):
    statement = "Select SkillId, Name, Experience from Skill where FileVersionId = %i order by SkillId"
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement % file.id)
    for row in cursor:
        skill = Skill(row[1], row[2], file)
        skill.set_primary_key(row[0])
        results.append(skill)
    return results

"""
THis function will get all skills for a particular filename
    name : The name of a file to search for
    :return: A list of Skills that were related to a file with that name
"""
def get_skills_in_files(name):
    statement = """
                SELECT Name, sum(Skill.Experience)

                FROM Skill
                WHERE
                    Skill.FileVersionId IN (Select FileVersion.FileVersionId from FileVersion where FileVersion.Name = ? )
                GROUP by Name
                Order by SkillId


                """
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement, [name])
    for row in cursor:
        results.append((row[0], row[1]))
    return results
"""
This function will return all the File objects which are in the database as a list
"""
def get_file_names():
    statement = """
                SELECT NAME
                FROM FileVersion
                GROUP by Name
                Order By FileVersionId
                """
    global cursor
    results = []
    if cursor == None:
        raise RuntimeError("Database is not connected")
    cursor.execute(statement)
    for row in cursor:
        results.append(row[0])
    return results
"""
This function will return the absolute values for the skills
"""
def get_all_ea_for_skills():
    statement = """ Select
                        Skill.name, sum(Skill.Experience)
                    from Skill
                        group by Skill.Name
                        order by Skill.SkillId;
                        """
    global cursor
    dict = {}
    if cursor == None:
        logging.error("Database is not connected")
        raise RuntimeError("Database is not connected")
    cursor.execute(statement)
    for row in cursor:
        dict[row[0]] = row[1]
    return dict