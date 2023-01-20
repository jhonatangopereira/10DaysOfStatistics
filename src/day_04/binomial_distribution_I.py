# Day 4: Binomial Distribution I

'''
Task:
  The ratio of boys to girls for babies born in Russia is 1.09:1. If there
  is 1 child born per birth, what proportion of Russian families with exactly
  6 children will have at least 3 boys?

  Write a program to compute the answer using the above parameters. Then print
  your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''

def factorial(n:int) -> int:
  return 1 if n == 0 else n * factorial(n - 1)

def combination(n:int, k:int) -> float:
  return factorial(n) / (factorial(k) * factorial(n - k))

def binomial_distribution(n:int, k:int, p:int) -> float:
  return combination(n, k) * (p ** k) * ((1 - p) ** (n - k))

NUMBER_OF_SAMPLES = 6
boys_ratio, girls_ratio = map(float, input().split())
odds = boys_ratio / girls_ratio
result = sum([binomial_distribution(NUMBER_OF_SAMPLES, i, odds / (1 + odds)) for i in range(3, NUMBER_OF_SAMPLES + 1)])

print(f"{result:.3f}")
