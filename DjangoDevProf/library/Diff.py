import sys

__author__ = 'freddy'
import re

"""
This function will read a hunk. And return the linenumber where the add started and how long the  section is. Example for a hunk: @@ -1,4 +1,5 @@
    line: The line that contaisn the hunk
    return: Start line as how long it is (1,5)
"""
def read_hunk(line):
    end = line.rfind(" @@")
    line = line[3:end]
    parts = line.split(" ")
    t = re.match(r'(\+)?(\d+),(\d+)', parts[1])
    if t:
        return int(t.group(2)), int(t.group(3))

"""
This function returns a list with all the added line numbers
    diff_output: The diff
    return: list of added linenumbers

"""
def get_modified_lines(diff_output):

    lines = diff_output.replace(" @@ ", " @@").split("\n")
    #lines = diff_output.split("\n")
    changed_lines = []
    start,end = (0,0)

    for line in lines:
        if line.startswith("---") or line.startswith("+++"):
            continue
        if re.match(r'@@ (.)+ @@(.)*', line):
        #if line.startswith("@@ ") and line.endswith(" @@"):
            (start, end) = read_hunk(line)
            continue
        else:
            if line.startswith("+") and line != "+":
                changed_lines.append(start)
        if not line.startswith("-"):
            start += 1

    return changed_lines

"""
This function will take the diff content and removed all the lines excpeted for the added once
    diff: The string which represents a diff output
    return: Just the lines that were added as string
"""
def filter_added_lines(diff):
    lines = diff.split("\n")
    result = ""
    for line in lines:
        if line.startswith("+"):
            result += line + "\n"
    result = result[0:-1]
    return result
