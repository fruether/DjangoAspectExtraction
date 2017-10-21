__author__ = 'freddy'

"""
Saves the tree structure in a dictonary
"""
tree = {}

"""
This function deleted the tree
"""
def clean_up():
    global tree
    tree.clear()

"""
This function adds a class to the tree
    base: The base class
    class_name. The name of the class
"""
def add_class(base, class_name):
    global tree
    #if class_name not in tree:
    if not isinstance(base, list):
        base = [base]

    tree[class_name] = base
"""
This function checks if a specific element is in a list
    l1: List of elements or string
    l2: List of elements

    return: true if it was in False otherwise
"""
def check_elements_in(l1, l2):
    if not isinstance(l1, list):
        return l1 in l2
    for x in l1:
        if x in l2:
            return True
    return False
"""

This function checks if based on the setup Inheritance Tree a class has as parent class the baseclass...somewhere in the chain ;)
    class_name: The name of the class
    base: The name of the super class to check for
    return: True if isinstance(class_name, base) would be true in Python
"""
def check_base_of(class_name, base):
    global tree
    if class_name not in tree:
        return False
    #Migration [Migration]
    base_classes = tree[class_name]
    if check_elements_in(base, base_classes):
        return True
    for x in base_classes:
        if class_name == x:
            continue
        if check_base_of(x, base):
            return True
    return False




#add_class("Test", "Class4")
#add_class(["Class3", "Class4", "Class5"], "Model2")
#print check_base_of("Model2", "Test")