__author__ = 'freddy'

import RawData

#For method definition see the super class. This objects stores information about a User of Git
class User(RawData.RawData):

    def __init__(self, name, number_of_commits):

        self.name = name
        self.number_of_commits = number_of_commits
        self.commits = None

    def getColumsToInsert(self):
        return [ "Name", "NumberOfCommits"]

    def getValuesToInsert(self):
        return [self.name, self.number_of_commits]
    def get_table(self):
        return "Contributor"
    def get_primary_key(self):
        return "UserID"
    def set_primary_key(self, key):
        self.id = key

    def set_commits(self, commits):
        self.commits = commits


