__author__ = 'freddy'

import os
import sys
sys.path.append("../")
import library.Rules.BaseRule
import library.Rules.BaseRule2
import logging
#Sources: http://stackoverflow.com/questions/951124/dynamic-loading-of-python-modules
#         https://github.com/EvilzoneLabs/BeastBot/blob/master/src/BeastBot.py
#
#load_Rules
#A list of all the loaded modules
modules = []
#The handle to the module
handle = None
#module name to Object
dict = {}

"""
This function will load all the rules from a specific directory
    directory: A path that specifies fro where the rules should be imported
"""
def load_rules(direcorty):
    global modules, handle
    modules = create_init(direcorty)
    get_project_path(direcorty)
    sys.path.append(get_project_path(direcorty))
    handle = __import__(get_module_from_path(direcorty), globals(), locals(), modules, -1)
    logging.debug("The rules have been loaded")
    #handle.settingsRule.test()

"""
This function will return the module name from a path. In fact that is just the last folder in the string /a/b/c => c
    directory: A path as string
    return: The modulename or last part of the path
"""
def get_module_from_path(directory):
    if(directory[-1] == "/"):
        directory = directory[0:-1]
    folders = directory.split('/')
    return folders[-1]
"""
This function will get the project path. In fact that is just the path without the module name
    path : The path as string to the current rule
    return: The path without the module name
"""
def get_project_path(path):
    if(path[-1] == "/"):
        inc = 1
    else:
        inc = 0
    module = get_module_from_path(path)
    return path[0:-len(module) - inc]

"""
This function will create the init
"""
def create_init(path):
    files = os.listdir(path)
    imps = []
    for i in range(len(files)):
        name = files[i].split('.')
        if len(name) > 1:
            if name[1] == 'py' and name[0] != '__init__':
                name = name[0]
                imps.append(name)
    outputPath = os.path.join(path, '__init__.py')
    file = open(outputPath, 'w')
    toWrite = '__all__ =' + str(imps)
    file.write(toWrite)
    file.close()
    logging.info("The init file was created with %i modules", len(imps))
    return imps


"""
This function will execute all the loaded rules, of the type BaseRule, with the given arguments and return the found skills
    *args : All the arguments that should be parsed to the rules
    return: A list of all the results. Usually Skills
"""
def execute_rules(*args):
    results = []
    global dict
    for module in modules:
        #Avoid to instance every rule thousand of times
        if module in dict.keys():
            obj = dict[module]
        else:
            module_instance = getattr(handle, module)
            class_ = getattr(module_instance, module + "_")
            obj = class_()
            dict[module] = obj

        if isinstance(obj, library.Rules.BaseRule.Rule) or isinstance(obj,library.Rules.BaseRule2.Rule):
            try:
                logging.debug("I am excuting the rule %s", module)
                result = obj.match(*args)
                if result != None:
                    results.append(result)
            except Exception as e:
                logging.warning("There was an error while executing the rule -%s- with the arguments: %s, %s, %s, %s and the error message was: %s", module, args[0], args[1], args[2], args[3], e.message)
                print "There seemes to be an error while executing: " + module + " with follow arguments: "
        else:
                logging.error("The %s module can't be loaded", module)
            #print(result)
    return results

"""
This function will reset the global variables. Needed for a a test case
"""
def reset():
    global modules, dict
    modules = []
    dict = {}

#load_rules("/Users/freddy/Documents/Bachelor_Project/bsc.-developer-profiling/DjangoDevProf/modules/t/rules/other")
#print execute_rules("A","", "t.xml", "", "")[1].loc