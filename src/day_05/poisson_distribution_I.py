# Day 5: Poisson Distribution I

'''
Task:
  A random variable, X, follows Poisson distribution with mean of 2.5. Find the
  probability with which the random variable X is equal to 5.
'''

def factorial(n:int) -> int:
  '''
  Calculate factorial of a number.

  Args:
    n (int): Argument used on factorial calculation.
  Returns:
    Factorial of a number.
  '''

  return 1 if n == 0 else n * factorial(n - 1)


def poisson_distribution(lambda_value:float, k:int) -> float:
  '''
  Calculate possion distribution probability.

  Args:
    lambda_value (float): The average number of successes.
    k (int): Actual number of successes.
  Returns:
    The Poisson distribution probability calculated.
  '''

  # E is a constant used in the poisson distribution formula
  E = 2.71828
  return ((lambda_value ** k) * (E ** -lambda_value)) / factorial(k)


# X's mean
average = float(input())
# number of successes
value = int(input())

result = poisson_distribution(k=value, lambda_value=average)

print(f"{result:.3f}")
