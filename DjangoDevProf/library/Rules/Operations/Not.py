__author__ = 'freddy'

from LogicalOperation import LogicalOperation


class Not(LogicalOperation):

    def __init__(self, filter1):
        super(Not, self).__init__(filter1, None)
    def __init__2(self, filter1):
        super(Not, self).__init__(filter1, None, -1)
    """
    First calls super function to get the values and then performs the NOT logic
    """
    def execute(self, *args):
        result1, _ = super(Not, self).execute(*args)
        if result1 == None:
            return 0
        return None


    def logical(self, a, b):
        if a == -1:
            return b
        if a == None:
            return 0
        return None


