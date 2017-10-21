__author__ = 'freddy'

import logging

from LogicalOperation import LogicalOperation


class Or(LogicalOperation):

    def __init__(self, filter1, filter2):
        super(Or, self).__init__(filter1, filter2)

    def __init__2(self, filter1, filter2):
        super(Or, self).__init__(filter1, filter2, None)

    """
    First calls super function to get the values and then performs the OR logic
    """
    def execute(self, *args):
        result1, result2 = super(Or, self).execute(*args)
        logging.debug("I am in OR and got %s and  %s ", str(result2), str(result1))
        if result1 == None and result2 == None:
            return None

        if result1 == None:
            return (result2 / 2) if result2 > 1 else result2
        elif result2 == None:
            return (result1 / 2 ) if result1 > 1 else result1

        return (result2 + result1) / 2

"""
    def logical(self, a, b):
        if a == None:
            return b
        if b == None:
            return a
        if a > b:
            return b
        return a

"""