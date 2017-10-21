__author__ = 'freddy'


from abc import ABCMeta, abstractmethod


class RawData():

    metaclass=ABCMeta
    def __init__(self):
        self.id = -1 #Dummy value

    #The Columns names that should be inserted. As list
    @abstractmethod
    def getColumsToInsert(self) : pass

    #The values that should be written to the database. readMe.mb
    @abstractmethod
    def getValuesToInsert(self) : pass

    #The Table the datas should be stored in
    @abstractmethod
    def get_table(self) : pass

    #The Primary key field in the database
    @abstractmethod
    def get_primary_key(self)   : pass

    #Save the primary key. Usually just known after the actuall insert
    @abstractmethod
    def set_primary_key(self, key)   : pass