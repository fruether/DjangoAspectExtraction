__author__ = 'freddy'

import logging

from LogicalOperation import LogicalOperation


class RightAnd(LogicalOperation):

    def __init__(self, filter1, filter2):
        super(RightAnd, self).__init__(filter1, filter2)
    def __init__2(self, filter1, filter2):
        super(RightAnd, self).__init__(filter1, filter2, -1)
    """
    First calls super function to get the values and then performs the AND logic
    """
    def execute(self, *args):
        result1, result2 = super(RightAnd, self).execute(*args)
        logging.debug("I am in AND and got %s and  %s ", str(result2), str(result1))
        if result1 == None or None == result2:
            return None
        return result2


    def logical(self, a, b):
        if a == None or b == None:
            return None
        if a == -1:
            return b
        if a < b:
            return a
        return b

