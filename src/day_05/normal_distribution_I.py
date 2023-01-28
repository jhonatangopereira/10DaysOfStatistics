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

x_hours = float(input())
x_lower_boundary, x_upper_boundary = map(float, input().split())

less_than_19_5_hours_result = normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_hours)

lower_boundary_result = normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_lower_boundary)
upper_boundary_result = normal_distribution(mean=mean, standard_deviation=standard_deviation, x=x_upper_boundary)
between_20_and_22_hours_result = upper_boundary_result - lower_boundary_result

print(f'{less_than_19_5_hours_result:.3f}')
print(f'{between_20_and_22_hours_result:.3f}')
