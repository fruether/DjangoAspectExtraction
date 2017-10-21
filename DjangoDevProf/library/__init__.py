from Rules.Filters.libs import Directory
from library.Rules.Filters.libs import ParseTree


def setup(path):
    Directory.setup_basepath(path)

def setup_inheritance_tree(content):
    ParseTree.setup_inheritance_tree(content)