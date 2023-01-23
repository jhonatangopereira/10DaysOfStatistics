# Day 1: Standard Deviantion

'''
Given an array, arr, of n integers, calculate and print the standard deviation.
Your answer should be in decimal form, rounded to a scale of 1 decimal place
(i.e., 12.3 format). An error margin of +-0.1 will be tolerated for the standard
deviation.
'''

#!/bin/python3

import math

def standard_deviation(arr:list) -> None:
  '''
  Calculate standard deviation of an array.

  Args:
    arr (list): Array used to calculate.
  Returns:
    standard_deviation (float): Standard deviation calculated.
  '''
  # mean of the array
  mean = sum(arr) / len(arr)

  # calculating the variance
  variance = 0
  for element in arr:
    variance += (element - mean) ** 2
  variance /= len(arr)

  # standard deviation is the square root of variance
  standard_deviation = math.sqrt(variance)
  print(f"{standard_deviation:.1f}")

if __name__ == '__main__':
  n = int(input().strip())

  vals = list(map(int, input().rstrip().split()))

  standard_deviation(vals)
