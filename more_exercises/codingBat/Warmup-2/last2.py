
"""
Given a string, return the count of the number of times that a substring length 2 appears
in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).
(https://codingbat.com/prob/p145834 - question link)
"""


def last2(str):
    last_2 = str[-2:]
    return sum(1 for i in range(len(str)-2) if str[i:i+2] == last_2)