__author__ = 'freddy'

from TAP.Simple   import *
import library.InheritanceTree


plan(4)

library.InheritanceTree.add_class("Base", "Model")
library.InheritanceTree.add_class("Model", "Class")
library.InheritanceTree.add_class("Class", "Class2")
#test -> Class2 -> Model
library.InheritanceTree.add_class("Test", "Class4")
library.InheritanceTree.add_class(["Class3", "Class4", "Class5"], "Model2")






ok(library.InheritanceTree.check_base_of("Class", "Base"))
ok(library.InheritanceTree.check_base_of("Model", "Base"))

ok(library.InheritanceTree.check_base_of("Model2", "Class5"))
ok(library.InheritanceTree.check_base_of("Model2", "Test"))