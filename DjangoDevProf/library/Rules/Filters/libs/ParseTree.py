__author__ = 'freddy'


# https://docs.python.org/2/library/ast.html#abstract-grammar
# https://greentreesna kes.readthedocs.org/en/latest/examples.html
import ast
from library import InheritanceTree
import logging
from library import Diff
import re
#Maybe a bug
"""
This function return the last line of a class. This is however not always 100% exact
 value: The expression that is  the last one in a class.
 return last line of a class as int
"""
def get_class_last_line(expr):
   if isinstance(expr, ast.FunctionDef):
      return expr.body[-1].lineno
   if isinstance(expr, ast.ClassDef):
        last_expr = expr.body[-1]
        if isinstance(last_expr, ast.Assign):
            return last_expr.value.lineno
        return last_expr.lineno
   return expr.lineno

"""
    Extract the base clases out of a ast.ClassDef object
    base: Object of type ast.ClassDed
    return: The base classes as list of strings
"""
def get_base_class(base):
    if isinstance(base, ast.Name):
        #print base.ctx
        return base.id
    if isinstance(base, ast.Attribute):
        return base.attr
    return "object"
"""
Takes a path; Reads it and executes get_class_scope
"""
def get_class_scope_from_path(file_path, searched_base_classes):
    with open(file_path) as file:
        code = file.read()

    return get_class_scope(code, searched_base_classes)

"""
Takes a path; Reads it and executes get_function_scope_from
"""
def get_function_scope_from_path(file_path, funcname, regex):
    with open(file_path) as file:
        code = file.read()

    return get_function_scope(code, funcname, regex)

"""
Takes a path; Reads it and executes setup_inheritance_tree
"""
def setup_inheritance_tree_from_path(file_path):
    with open(file_path) as file:
        code = file.read()

    return setup_inheritance_tree(code)

"""
    This tree will read a python code and adds the classes to the InheritanceTree
    code : Valid Python code as string or Excpetion
    return: The Inheritance tree was changed. But it is global so it won't be returned
"""
def setup_inheritance_tree(code):
    try:
        tree = ast.parse(code)
    except:
        logging.debug("There was a file that could not be parsed")
        return

    for stmt in ast.walk(tree):
        # Ignore non-classes #https://greentreesnmakes.readthedocs.org/en/latest/examples.html
        if isinstance(stmt, ast.ClassDef):
            if(len(stmt.bases) == 0):
                InheritanceTree.add_class([], stmt.name)
                continue
            base_classes = [get_base_class(base) for base in stmt.bases]
            InheritanceTree.add_class(base_classes, stmt.name)
"""
    Return the start and end lines of all the classes in a file.....if they inherit from a specific base class
    code: The python code...if invalid None
    searched_base_classes: The class to search for as string

    return: A list of tuples of the form (start, end) where start and end are the first and last line of a class that inherits from base_class
"""
def get_class_scope(code, searched_base_classes):
    results = []
    if type(searched_base_classes) is not list:
        if type(searched_base_classes) is str:
            searched_base_classes = [searched_base_classes]
        else:
            logging.error("Type error...sth has to be wrong for code: %s", code)
            raise RuntimeError("Please let base_classe be a string or list")
    try:
        tree = ast.parse(code)
    except:
        logging.debug("There was a file that could not be parsed")
        return None

    # https://julien.danjou.info/blog/2015/python-ast-checking-method-declaration
    for stmt in ast.walk(tree):
        # Ignore non-classes #https://greentreesnakes.readthedocs.org/en/latest/examples.html
        if isinstance(stmt, ast.ClassDef):
            if(len(stmt.bases) == 0):
                continue

            start = stmt.lineno
            if InheritanceTree.check_base_of(stmt.name, searched_base_classes):
                end = get_class_last_line(stmt.body[-1])
                results.append((start, end))
    return results if len(results) != 0 else None

"""
    Return the start and end lines of all the functions in a file.....if they match a specific function
    code: The python code...if invalid None
    searched_base_classes: The function that should be searched. As string or regex
    regex: True if searched_base_classes is a regex otherwise false

    return: A list of tuples of the form (start, end) where start and end are the first and last line of a function that fits the schema
"""
def get_function_scope(code, searched_base_func, regex):
    results = []

    try:
        tree = ast.parse(code)
    except:
        logging.debug("There was a file that could not be parsed")
        return None
    # https://julien.danjou.info/blog/2015/python-ast-checking-method-declaration
    for stmt in ast.walk(tree):
        # Ignore non-classes #https://greentreesnakes.readthedocs.org/en/latest/examples.html
        if isinstance(stmt, ast.FunctionDef):
            funcname = "def " + stmt.name + "("
            for arg in stmt.args.args:
                funcname += arg.id + ", "

            if stmt.args >= 1:
                funcname = funcname[0:-2] + ")"
            else:
                funcname += ")"
            if regex:
                if not re.search(searched_base_func, funcname):
                    continue
            else:
                if funcname != searched_base_func:
                    continue

            start = stmt.lineno
            end = stmt.body[-1].lineno
            results.append((start, end))

    return None if len(results) == 0 else results
"""

    This function checks if a user in a commit added lines to a class that inherits from a specific class. If so it return how many lines that would be
    type: type of git modification. A - added, M - modified, D- deleted
    content: The content of the file
    diff: The diff of the file

    return: Lines added in a class of inheritance tpye of the content and the diff. If no finds we return None
"""
def match_baseclass(type, base_class, content, diff):
    x  = get_class_scope(content, base_class)
    if x == None:
        return None
    count = 0
    for (start, end) in x:
        if type == "A":
            count += end-start +1
            continue
        lines = Diff.get_modified_lines(diff)

        for line in lines:
            if start <= line and end >= line:
                count += 1
    return count if count != 0 else None

"""

    This function checks if a user in a commit added lines to a function that matches our filter. If so it returns how many lines that would be
    type: type of git modification. A - added, M - modified, D- deleted
    content: The content of the file
    diff: The diff of the file

    return: Lines added in a function with a signature for a file with the content and the diff. If no finds we return None
"""
def match_function(type, function, regex, content, diff):
    x  = get_function_scope(content, function, regex)
    if x == None:
        return None
    count = 0
    for (start, end) in x:
        if type == "A":
            count += end - start + 1
            continue

        lines = Diff.get_modified_lines(diff)
        for line in lines:
            if start <= line and end >= line:
                count += 1
    return count if count != 0 else None



