__author__ = 'freddy'
import ConfigParser
import os
import sys
from time import gmtime, strftime
import logging

from modules import RuleEngine, SqlClient, Git, CreateOutput
from library.datas import Commit, File
from library.datas.User import User
#from library.Rules.Filters.libs import ParseTree
import library


def get_lines(content):
    if not content:
        return 0
    return len(content.splitlines())

__metaclass__ = type

# Read the configuratione File
#https://docs.python.org/2/library/configparser.html#module-ConfigParser
config = ConfigParser.ConfigParser()
config.readfp(open('conf/config.cfg'))
#Setup path
path =  os.path.realpath(__file__)
file = os.path.basename(__file__)
path = path.replace(file, "")
#Read the values from the configuration file
if config.has_option("Main","projectPath"):
    path = config.get("Main","projectPath")
database = os.path.join(path, config.get("Main","database" ))
output_path  = os.path.join(path, config.get("Main", "outputPath"))
rule_path = os.path.join(path, config.get("Main", "rulePath"))
repo_url = config.get("Main", "repoUrl")
repo = config.get("Main", "repo")

if repo_url.find(repo) == -1:
    print >> sys.stderr, "The configuration file is invalid"
    exit()
library.setup(path)

time = strftime("%a, %d %b %Y %H:%M:%S", gmtime())
log_path = os.path.join(path, config.get("Main", "logPath"))
debug = True if config.get("Main", "logDebug") == "True" else False
log_path = os.path.join(log_path, time + ".log")
logging.basicConfig(filename=log_path, filemode='w+',format = '%(asctime)s  --%(levelname)s-- %(message)s ', level=logging.DEBUG if debug else logging.INFO)
logging.info("Message read")
#Connect to database
SqlClient.set_up(database)
#Get the Repo
Git.clone_repo(repo_url, output_path)
#Load Rules
RuleEngine.load_rules(rule_path)
#
CreateOutput.setOutputPath(output_path)

#Get Commits
commits = Git.retrieve_commits(os.path.join(output_path, repo))
logging.info("The program will analyse  %s commits", str(commits))
#print "Oh yeah there are : " + str(commits) + "commits"
#Map with Users
dict = {}

commits = []
skills = []
files = []

#Walk over commits
i = 0
while Git.check_not_empty():
    l = (author, message, date, r) = Git.get_next_commit()
    #Take care of the author also known as User
    if author in dict.keys():
        u = dict[author]
        u.number_of_commits += 1
        SqlClient.update_raw_data(u)
        dict[author] = u
        logging.debug("The program increased the count of  %s to %i commits", author, u.number_of_commits)
    else:
        u = User(author, 1)
        #print "We are adding " + author + " to the database"
        SqlClient.add_raw_data(u)
        dict[author] = u
        logging.info("The program added  %s to the database of contributors", author)
    #Now we are read to produce the commit object
    commit = Commit.Commit(date, u, message)
    SqlClient.add_raw_data(commit)
    commits.append(commit)

    print "The commit was on follow date: " + date + " from the author " + author + " with the message " + message + " : "
    logging.info("The commit was on follow date: " + date + " from the author " + author + " with the message " + message + " ")
    #Now we walk above all changed files:
    x = 0
    for (mode, path, content, dif) in r:
        library.setup_inheritance_tree(content)
        logging.debug("We have finished setting up the inheritance-tree")

    for (mode, path, content, dif) in r:
        logging.info("Executing all my rules with the mode %s on the file %s and the number of commits is %s", mode, path, str(i))
        #print "I am executing my rules now on: " + mode + " " + path + " " + str(i)
        if not path:
            logging.error("Error: The path is None in commit %i with message %s and diff %s", x, message, dif)
            continue

        file = File.File(path, get_lines(content), commit)
        files.append(file)
        SqlClient.add_raw_data(file)
        logging.debug("Added file object to the database: %s", file.name)
        results = RuleEngine.execute_rules(mode, path, dif, content)
        #Save all the skills obtained through that file and combine it with the current file
        for skill in results:
            if skill.experience == 0:
                continue
            skill.set_fileVersion(file)
            SqlClient.add_raw_data(skill)
            skills.append(skill)
        logging.debug("Program added all the skills to the database")
            #SqlClient.add_skill_file(file.id, skill.id)
        file.set_skills(results)
    i+=1

users = dict.values()
try:
    CreateOutput.create_output(users, commits, files, skills)
except:
     users, commits, files, skills = SqlClient.database_to_object()
     CreateOutput.create_output(users, commits, files, skills)