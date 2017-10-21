__author__ = 'freddy'

import RawData
from File import File
import sys
import logging

#For method definition see the super class. This objects stores information about a Skill
class Skill(RawData.RawData):
    #ToDo Enums are better ? https://docs.python.org/3/library/enum.html
    #What skills are allowed
    possible_skills = ["Other/Templates","Forms/Model","Forms/Widget", "Forms/HTML", "Javascipt", "CSS", "Validation", "Other/Router", "Control", "Other/DjangoConfiguration", "Model/Data", "Other/Deployment", "Model/Admininterface", "Test/Django", "Test/Generell", "Database/Migration", "Database/Fixture", "Database/SQL", "Administration/VCS", "Other/KnowledgeManagement", "Administration/Buildmangament" ]


    def __init__(self, skill, loc, fileVersion = None):
        if skill not in Skill.possible_skills:
            logging.warning("The skills you are trying to add is not in the list of supported")
            return
        self.skill = skill
        self.experience = loc
        self.fileVersion = fileVersion
    def getColumsToInsert(self):
        return ["Name", "Experience", "FileVersionId"]

    def getValuesToInsert(self):
        return [self.skill, self.experience, self.fileVersion.id]
    def get_table(self):
        return "Skill"
    def get_primary_key_column(self):
        return "SkillId"
    def set_primary_key(self, key):
        self.id = key
    def set_fileVersion(self, fileVersion):
        if not isinstance(fileVersion, File):
            print >> sys.stderr, "The second parameter should be an instance of FileVersion"
        self.fileVersion = fileVersion
    def get_loc(self):
        return self.loc
    def get_primary_key(self):
        return "SkillId"