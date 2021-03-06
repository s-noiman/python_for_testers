
"""
Return the "centered" average of an array of ints,
which we'll say is the mean average of the values,
except ignoring the largest and smallest values in the array.
If there are multiple copies of the smallest value, ignore just one copy,
and likewise for the largest value.
Use int division to produce the final average.
You may assume that the array is length 3 or more.
(https://codingbat.com/prob/p126968 - question link)
"""


def centered_average(nums):
    small = min(nums)
    big = max(nums)
    return (sum(nums) - small - big) / (len(nums) - 2)