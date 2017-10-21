__author__ = 'freddy'

from library.datas import RawData

class Base:
    pass


class User(RawData.RawData, Base):

    def __init__(self, name, number_of_commits):

        self.name = name
        self.number_of_commits = number_of_commits
        self.user_id = -1

    def getColumsToInsert(self):
        return [ "Name", "NumberOfCommits"]

    def getValuesToInsert(self):
        return [self.name, self.number_of_commits]
    def get_table(self):
        return "Contributor"
    def get_primary_key(self):
        return "UserID"
    def set_primary_key(self, key):
        self.user_id = key
