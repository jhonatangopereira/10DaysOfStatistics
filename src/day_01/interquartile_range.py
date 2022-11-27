# Day 1: Interquartile Range

'''
The interquartile range of an array is the difference between its first (Q1)
and third (Q3) quartiles (i.e., Q3 - Q1).

Given an array, values, of n integers and an array, freqs, representing the
respective frequencies of values's elements, construct a data set, S, where
each values[i] occurs at frequency freqs[i]. Then calculate and print S's
interquartile range, rounded to a scale of 1 decimal place (i.e., 12.3 format).
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'interQuartile' function below.
#
# The function accepts following parameters:
#  1. INTEGER_ARRAY values
#  2. INTEGER_ARRAY freqs
#

def interQuartile(values, freqs):
  S = []
  for i in range(len(values)):
    S.extend([values[i]] * freqs[i])
  S.sort()
  
  if len(S) % 2:
    middle = int(len(S) / 2 - 0.5)
    lower_half = S[:middle]
    upper_half = S[middle + 1:]
  else:
    middle = int(len(S) / 2)
    lower_half = S[:middle]
    upper_half = S[middle:]

  if len(lower_half) % 2:
    half_middle = int(len(lower_half) / 2 - 0.5)
    q1 = lower_half[half_middle]
    q3 = upper_half[half_middle]
  else:
    half_middle = int(len(lower_half) / 2)
    q1 = (lower_half[half_middle - 1] + lower_half[half_middle]) / 2
    q3 = (upper_half[half_middle - 1] + upper_half[half_middle]) / 2
  
  print(f"{(q3 - q1):.1f}")

if __name__ == '__main__':
  n = int(input().strip())

  val = list(map(int, input().rstrip().split()))

  freq = list(map(int, input().rstrip().split()))

  interQuartile(val, freq)
