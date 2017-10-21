import subprocess
from git import Repo
from gitdb.exc import BadObject
import os
import difflib
import git
import time
import logging
__author__ = 'freddy'
#https://gitpython.readthedocs.org/en/stable/tutorial.html


stack = []
"""
This function will calculate the diff of two contents
"""
def get_dif(content1, content2):
    diff = difflib.unified_diff(content1, content2)
    return '\n'.join(diff)

"""
This function takes the url to a repository and the path where it should be cloned to. If it was already  cloned it will be pulled otherwise the clone will be performed
"""
def clone_repo(url, output):
    parts = url.split("/")
    repo_name = parts[-1].replace(".git", "")
    path = os.path.join(output, repo_name)
    if not os.path.isdir(path):
        subprocess.call(["git", "clone", url], cwd=output)
        logging.info("I have cloned follow repo %s", url)
    else:
        subprocess.call(["git", "pull"], cwd=path)
        logging.info("I have updated follow repo %s", url)

#Saves the filepath and points to all the commitId's it was contained in. Hence it has just to be calculated once
dict = {}

"""
This file checks if a file is really part of a specific commit. WIthout that functions we got problems dealing with merge requests.
    return: True if the file really was in the commit otherwise False
"""
def check_file_in_commit(diff, commit, repo):
    global dict
     #Make sure that this file is in the commit
    if diff.a_path in dict.keys():
        fileCommits = dict[diff.a_path]
    else:
        fileCommits = dict[diff.a_path] = [y for y in git.Commit.iter_items(repo, "master", paths = diff.a_path)]
    if commit not in fileCommits:
                    #logging.warning(x.author.name + "was not in commit" + diff_edit.a_path + " I figured it was a merge? "  + x.message)
        return False
    return True


"""
This function saves all the commits in a specific repo in a stack. The stack has the form (ID, mode, GitObjectBlob, author, summary, time, diff)
    path: The local path to the repo
    return: The global stack variable is set with those values
"""
def retrieve_commits(path):
    global stack
    repo = Repo(path, odbt=git.GitCmdObjectDB)
    commits = list(repo.iter_commits('master'))
    global dict
    for i in range(0,len(commits) - 1):

        x = commits[i]
        logging.debug("I am dealing with commit %s" , x.message)
        try:
            for diff_edit in commits[i+1].diff(commits[i], create_patch=True).iter_change_type('M'):
                if diff_edit.new_file or diff_edit.deleted_file:
                    continue
                if not check_file_in_commit(diff_edit, x, repo):
                    continue
                stack.append((i+1, "M", diff_edit, x.author.name, x.summary,  time.asctime(time.gmtime((x.committed_date))), str(diff_edit)))
            #The deleted content
            for diff_edit in commits[i].diff(commits[i+1], create_patch=True).iter_change_type('M'):
                if diff_edit.new_file or diff_edit.deleted_file:
                    continue
                #We don't call the method to save time
                if diff_edit.a_path not in dict.keys():
                    continue
                if x not in dict[diff_edit.a_path]:
                    continue
                stack.append((i+1, "M", diff_edit, x.author.name, x.summary,  time.asctime(time.gmtime((x.committed_date))), str(diff_edit)))

            for diff_edit in commits[i+1].diff(commits[i], create_patch=True).iter_change_type('R'):
                stack.append((i+1, "R", diff_edit, x.author.name, x.summary,  time.asctime(time.gmtime((x.committed_date))), None))
            for diff_deleted in commits[i+1].diff(commits[i], create_patch=True).iter_change_type('D'):
                if not check_file_in_commit(diff_deleted, x, repo):
                    continue
                stack.append((i+1, "D", diff_deleted, x.author.name, x.message,  time.asctime(time.gmtime((x.committed_date))), str(diff_deleted)))

            for diff_added in commits[i+1].diff(commits[i], create_patch=True).iter_change_type('A'):
                if not check_file_in_commit(diff_added, x, repo):
                    continue

                stack.append((i+1, "A", diff_added, x.author.name, x.summary,  time.asctime(time.gmtime((x.committed_date))), str(diff_added)))


        except AssertionError as ae:
            logging.warning("There was an error reading commit number %i with follow metadate: ", i, x.summary, ae.message)

    #Add the just A files in the first commit becaus that way the diff does not work...Empty or DIff does not seem to work
    x = commits[-1]
    for file in x.tree.traverse():
                #    print file.abspath
        if isinstance(file, git.Blob):
            #logging.info("Adding the file %s of the commit %s with mode A ", file.abspath, x.summary)
            stack.append((len(commits), "A", file, x.author.name, x.summary,  time.asctime(time.gmtime((x.committed_date))), None))
    logging.info("There have been retrieved %s commits", len(commits))
    return len(commits)

"""
This function will return the next file of the stack and it's values
return: number, id, message, path, content date, diff
"""
def get_next_file():
    global stack
    if len(stack) == 0:
        print "Empty stack"
        return None
    i, mode, diff, author, message, date, difference = stack.pop()
    if isinstance(diff, git.Blob):
        blob = diff
    elif diff.b_blob:
        blob = diff.b_blob
    else:
        blob = diff.a_blob
    content = None

    try:
        if isinstance(blob, git.Blob) and  mode != "D":
            content = blob.data_stream.read()
            logging.debug("I am ine get_next_fle() function and got follow valued out of the stack:" + author + " " + mode + "=>" + blob.path + " " + message + " type " + blob.mime_type)
        elif mode == "D":
            logging.warning("One file seems to be broken:" + author + " " + mode + "=>" + message + " type ")
        else:
            return i, mode, author, message, None, None, date, difference
    except BadObject as bo:
        print "I am terrible sorry but there was an error if follow commit: " + str(i)
        print author + " " + mode + "=>" + diff.b_path + " " + message + " type " + diff.b_blob.mime_type + " With the sha: " + str(blob)
        print bo.message
        print difference
    except ValueError as ve:
        logging.warning("There was an error in the commit number %i follow commit: ", i)
        logging.warning(author + " " + mode + "=>" + diff.b_path + " " + message + " type " + diff.b_blob.mime_type + " With the sha: " + str(blob))
        logging.warning(ve.message)
    if not difference and mode == "A":
        difference = get_dif("", content)
        logging.debug("I am calculating the content for a just added file %s", blob.path)
    return i, mode, author, message, blob.path, content, date, difference


last_commit = None

"""
This function will return as a list all the files that were touched in the next commit and some other handy values
    return: List with the values (author, message, date, result)
"""
def get_next_commit():
    global last_commit
    result = []

    if last_commit is None:
        (i, mode, author, message, path, content, date, difference) = get_next_file()
    else:
        (i, mode, author, message, path, content, date, difference) = last_commit
    i2 = i
    while check_not_empty() and i == i2:
        result.append((mode, path, content, difference))
        (i2, mode, author2, message2, path, content, date2, difference) = get_next_file()

    last_commit = (i2, mode, author2, message2, path, content, date2, difference)

    logging.debug("I am in get_next_commit() and analyse the commit %i by the author %s with the message %s", i, author, message)
    logging.info("I have gotten the commit " + str(i))
    return author, message, date, result

"""
This function checks if there still exist commits in the stack
"""
def check_not_empty():
    global stack
    return len(stack) != 0

