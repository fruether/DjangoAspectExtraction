__author__ = 'freddy'

import sys
sys.path.append("../")
import modules.SqlClient
from jinja2 import  Environment, PackageLoader
import os
import hashlib
import logging


env = None
outputPath = os.getcwd() + "/../output/"
"""
This function will write out all users that exist. In fact it will fill the index.html template
    users: A list of User objects that should be displayed or all users if it is None
"""
def list_users(users = None):
    global env
    if not users:
        users = retrieve_users_from_database()
    load_templates()
    template = env.get_template("index.html")
    str = template.render(users = users)
    with open(outputPath + "index.html", "w+") as f:
        f.write(str.encode('utf8'))
    logging.debug("I have written the index.html")

"""
Load the templates. The action is needed due to the jinja2 module
"""
def load_templates():
    global env
    if not env:
        env = Environment(loader=PackageLoader('modules', 'templates'))


"""
Return all the users from the database
"""
def retrieve_users_from_database():
     return modules.SqlClient.get_users()

"""
Create a summary for a specific user. Write the result in the form given by the user.html template
"""
def create_user_summary(user):
    template = env.get_template("user.html")
    skills = modules.SqlClient.get_skills_from_user_sum(user)
    max_skills = modules.SqlClient.get_all_ea_for_skills()
    str = template.render(commits = user.commits, user = user, skills = skills, complete = max_skills)

    output_directory = outputPath + "/users/"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    with open(output_directory+ user.name +".html", "w+") as f:
        f.write(str.encode('utf8'))
    logging.debug("I have created a user summary for %s", user.name)

"""
This function will write all Skills that are in a specific fileversion  to a template (file. html)
    file: A list of objects of the type Files whose skills should be displayed
"""
def create_file_summary(file):
    logging.debug("I am in create_file_summary read")
    template = env.get_template("file.html")
    #skills = file.skills
    skills = modules.SqlClient.get_skills_in_files(file.name)
    str = template.render(skills = skills, file = file.name)

    output_directory = outputPath + "/files/"
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)
    hash_s = hashlib.md5(file.name).hexdigest()
    with open(output_directory+ hash_s +".html", "w+") as f:
        f.write(str.encode('utf8'))
    logging.debug("I have executed create_file_summary for %s ", file )

"""
This function will write all the skills to a specific file (skill. html)
    skills: A list of objects of the type Skill that should be displayed
"""
def create_skills_to_users(skills):
    template = env.get_template("skills.html")
    #SkillName to User
    dict = {}
    for skill in skills:
        if skill.skill in dict.keys():
            values = dict[skill.skill]
            if skill.fileVersion.commit.user.name not in values:
                values.append(skill.fileVersion.commit.user.name)
                dict[skill.skill] = values
        else:
            values = []
            values.append(skill.fileVersion.commit.user.name)
            dict[skill.skill] = values
    str = template.render(_dict = dict)
    with open(outputPath + "skill.html", "w+") as f:
        f.write(str.encode('utf8'))
    logging.debug("I have executed create_skills_to_users")

"""
Main function that should be called to write all the values found to the the specific files.
    users: All the User objects that should be displayed in a HTML file ---> as list
    commits. All the Commit objects that should be displayed in a HTML file ---> as list
    files: All the File objects that should be displayed in a HTML file ---> as list
    skills: All the Skill objects that should be displayed in a HTML file ---> as list

    All fields are mandatory to decrease the dependency between SQL module and Output module
"""
def create_output(users, commits, files, skills ):
    if users == None or commits == None or files == None or skills == None:
       raise Exception("callmodules.SqlClient.database_to_object() if needed")
    list_users(users)
    for user in users:
        create_user_summary(user)

    #files = modules.SqlClient.get_file_names()
    for file in files:
       create_file_summary(file)
    create_skills_to_users(skills)
    logging.info("Output read")

"""
This function will set the path the output should be written to
"""
def setOutputPath(path):
    global outputPath
    outputPath = path
"""
path = os.getcwd() + "/../database/devProf.db"
print path
modules.SqlClient.set_up(path)
u, c, f, s = modules.SqlClient.database_to_object()
create_output(u, c, f, s)
"""