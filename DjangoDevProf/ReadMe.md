#DjangoDevProf

That program is written in Python and will analyse a repository that contains Django specific files for skills of developers

##Folders
* Conf/ -> In that folder the conf file is stored
* database/ -> In that folder the database file is stored and the scrip to setup the table schema
* docs/ -> some interesint documentations
* library/ -> All the libraries the code uses (see thesis)
* modules/ -> All the modules that tool used
* ouput/ -> all the output will be written to that file e.g. the logs
* rules/ -> here all the rules are stored
* test/ -> That code will verify the result of the Django-oscar project with test cases

##Files
* devProf.py -> That file is the main code : python devProf.py for executing
* test.py -> executes all make files with a specific label e.g. test
* Makefile -> Make install for installing; make test for tesing; make reset for deleteing