# Day 5: Normal Distribution I

'''
Task:
  In a certain plant, the time taken to assemble a car is a random variable, X, having a normal
  distribution with a mean of 20 hours and a standard deviation of 2 hours. What is the probability
  that a car can be assembled at this plant in:
    1. Less than 19.5 hours?
    2. Between 20 and 22 hours?
'''

from math import erf, sqrt


def normal_distribution(mean:float, standard_deviation:float, x:float) -> float:
  '''
  Calculate the normal distribution probability.

  Args:
    mean (float)
    standard_deviation (float)
    x (float)
  Returns:
    normal_distribution_probability (float)
  '''

  return (1 / 2) * (1 + erf((x - mean) / (standard_deviation * sqrt(2))))


mean, standard_deviation = map(int, input().split())

x_upper_boundary = float(input())
x_lower_boundary = float(input())

x_upper_boundary_result = 100 * (1 - normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_upper_boundary))
x_intermediate_boundary_result = 100 * (1 - normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_lower_boundary))
x_lower_boundary_result = 100 * (normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_lower_boundary))

print(f'{x_upper_boundary_result:.2f}')
print(f'{x_intermediate_boundary_result:.2f}')
print(f'{x_lower_boundary_result:.2f}')
