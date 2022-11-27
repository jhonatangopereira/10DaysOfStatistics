# Day 1: Quartiles

'''
Given an array, arr, of n integers, calculate the respective first quartile
(Q1), second quartile (Q2), and third quartile (Q3). It is guaranteed that Q1,
Q2, and Q3 are integers.
'''

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'quartiles' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def quartiles(arr):
  arr.sort()

  if len(arr) % 2:
    middle = int(len(arr) / 2 - 0.5)
    q2 = arr[middle]
    lower_half = arr[:middle]
    upper_half = arr[middle + 1:]
  else:
    middle = int(len(arr) / 2)
    q2 = (arr[middle - 1] + arr[middle]) / 2
    lower_half = arr[:middle]
    upper_half = arr[middle:]

  if len(lower_half) % 2:
    half_middle = int(len(lower_half) / 2 - 0.5)
    q1 = lower_half[half_middle]
    q3 = upper_half[half_middle]
  else:
    half_middle = int(len(lower_half) / 2)
    q1 = (lower_half[half_middle - 1] + lower_half[half_middle]) / 2
    q3 = (upper_half[half_middle - 1] + upper_half[half_middle]) / 2
  
  return [int(q1), int(q2), int(q3)]

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  n = int(input().strip())

  data = list(map(int, input().rstrip().split()))

  res = quartiles(data)

  fptr.write('\n'.join(map(str, res)))
  fptr.write('\n')

  fptr.close()
