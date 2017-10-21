__author__ = 'freddy'

from abc import ABCMeta, abstractmethod
from library.Rules.results.Monoid import Monoid
from library.Rules.results.ExperienceAtomCollector import ExperienceAtomCollector
"""
All the logical Operations have to inherit from that class
"""
class LogicalOperation:
    __metaclass__ = ABCMeta
    #These functions return the line of code, that is applicable to that skill
    def __init__(self, filter1, filter2):
        self.filter_left = filter1
        self.filter_right = filter2

    def __init__2(self, filter1, filter2, zero):
        self.filter_left = filter1
        self.filter_right = filter2
        self.monoid = Monoid(zero, lambda x: x(), lambda a, b : self.logical(a,b))

    """
    This function executes the filters and returns the result. If it is not a Filter but another LogicalExpression it will first evaluate that one
    """
    @abstractmethod
    def execute(self, *args):
        if isinstance(self.filter_left, LogicalOperation):
            result1 = self.filter_left.execute(*args)
        elif not self.filter_left:
            result1 =  None
        else:
            result1 = self.filter_left.apply_filter(*args)

        if isinstance(self.filter_right, LogicalOperation):
            result2 = self.filter_right.execute(*args)
        elif not self.filter_right:
            result2 = None
        else:
            result2 = self.filter_right.apply_filter(*args)
        return result1, result2

    """
    This function executes the filters and returns the result. If it is not a Filter but another LogicalExpression it will first evaluate that one
    """
    def execute2(self, *args):
        if isinstance(self.filter_left, LogicalOperation):
            result1 = self.filter_left.execute(*args)
        elif not self.filter_left:
            result1 =  ExperienceAtomCollector(None)
        else:
            result1 = self.filter_left.apply_filter(*args)

        if isinstance(self.filter_right, LogicalOperation):
            result2 = self.filter_right.execute(*args)
        elif not self.filter_right:
            result2 = ExperienceAtomCollector(None)
        else:
            result2 = self.filter_right.apply_filter(*args)
        x = ExperienceAtomCollector(self.monoid(result1, result2))
        return x

    def logical(self, a, b): pass


