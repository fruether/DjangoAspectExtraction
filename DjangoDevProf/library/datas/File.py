__author__ = 'freddy'

import RawData
import sys
from Commit import Commit
#For method defintion see the super class. This objects stores information about a FileVersion
class File(RawData.RawData):

    def __init__(self, name, loc, commit):
        #Path of File
        self.name = name
        #How many lines does the file have
        self.loc = loc
        if(not isinstance(commit, Commit)):
            print >> sys.stderr, "The third element should be a Commit object"
        self.commit = commit
        self.skills = None

    def getColumsToInsert(self):
        return [ "Name", "LOC", "CommitId"]

    def getValuesToInsert(self):
        return [self.name, self.loc, self.commit.id]
    def get_table(self):
        return "FileVersion"
    def get_primary_key(self):
        return "FileVersionId"
    def set_primary_key(self, key):
        self.id = key
    def set_skills(self, skills):
        self.skills = skills
