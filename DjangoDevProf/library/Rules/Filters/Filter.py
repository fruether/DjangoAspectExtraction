__author__ = 'freddy'
from abc import ABCMeta, abstractmethod


class Filter:
      __metaclass__ = ABCMeta
      """
      All functions have to setup the logic for the execution of the underlying library
      """
      @abstractmethod
      def apply_filter(selftype, type, filepath, diff, content): pass
      def __init__(self): pass

