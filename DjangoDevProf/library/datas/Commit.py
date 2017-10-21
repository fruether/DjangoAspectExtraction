__author__ = 'freddy'



import RawData
from User import User
import sys

#For method definition see the super class. This objects stores information about a Commit
class Commit(RawData.RawData):

    def __init__(self, timestemp, user, message):
        self.timestemp = timestemp
        if not isinstance(user, User):
            print >> sys.stderr, "The second parameter should be an instance of User"
        self.user = user
        self.message = message
        self.files = None

    def getColumsToInsert(self):
        return [ "timestemp", "UserId", "Message"]

    def getValuesToInsert(self):
        return [self.timestemp, self.user.id ,self.message]
    def get_table(self):
        return "Gitcommit"
    def get_primary_key(self):
        return "CommitId"
    def set_primary_key(self, key):
        self.id = key
    def set_files(self, files):
        self.files = files