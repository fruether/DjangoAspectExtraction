__author__ = 'freddy'


from TAP.Simple   import *
import library.InheritanceTree


plan(2)
library.InheritanceTree.add_class("Base", "Model")
library.InheritanceTree.add_class("Model", "Class")


eq_ok(library.InheritanceTree.tree["Model"], ["Base"], "Basic case")
eq_ok(library.InheritanceTree.tree["Class"], ["Model"], "Basic case 2")
