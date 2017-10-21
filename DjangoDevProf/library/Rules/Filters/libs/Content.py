__author__ = 'freddy'
import re
import Kmpstringmatcher
"""
Matches in a text a specific regex and returns the result
    text: Where should I search
    regex: For what shall I search

    return: Did I find it
"""
def match_content_regex(text, regex):
    if re.match(regex, text, re.DOTALL):
        return True
    return False
"""
Counts how often a regx appears in a text
    text: Where should I search
    regex: For what shall I search

    return: How often did I found it or None if I did not
"""
def match_content_regex_count(text, regex):
    if re.search(regex, text, re.DOTALL):
        num = re.findall(regex, text)
        return len(num)
    return None
"""
Matches in a text a specific regex and returns the result. However the text or line does not have to start with that regex
    text: Where should I search
    regex: For what shall I search

    return: Did I find it
"""
def match_content_regex_anywhere(text, regex):
    if re.search(regex, text, re.DOTALL):
        return True
    return False

"""
Counts how often a regex appears in a text.
    text: Where should I search
    regex: For what shall I search

    return: How often did I found it or None if I did not
"""
def match_content_regex_anywhere_count(text, regex):
    return match_content_regex_count(text, regex)

"""
Return how often it was found if I search for a plain string
"""
def match_content_string(text, string):
    return string in text

"""
Count how often a simple string was found in a text and return it
"""

def match_content_string_count(text, string):
    count = text.count(string)
    return count if count > 0 else None

#https://de.wikipedia.org/wiki/Knuth-Morris-Pratt-Algorithmus
#https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
def match_content_string_kmp(text, string):
    if Kmpstringmatcher.kmp_search(string, text):
        return True
    return False
