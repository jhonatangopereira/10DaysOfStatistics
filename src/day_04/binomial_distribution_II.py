# Day 4: Binomial Distribution II

'''
Task:
  A manufacturer of metal pistons finds that, on average, 12% of the pistons they manufacture are
  rejected because they are incorrectly sized. What is the probability that a batch of 10 pistons
  will contain:
    1. No more than 2 rejects?
    2. At least 2 rejects?
'''

def factorial(n:int) -> int:
  return 1 if n == 0 else n * factorial(n - 1)

def combination(n:int, k:int) -> float:
  return factorial(n) / (factorial(k) * factorial(n - k))

def binomial_distribution(n:int, k:int, p:int) -> float:
  return combination(n, k) * (p ** k) * ((1 - p) ** (n - k))

rejects_pistols_average, PISTOLS_QUANTITY = map(float, input().split())
odds = rejects_pistols_average / 100

no_more_than_two_rejects_result = sum([binomial_distribution(PISTOLS_QUANTITY, i, odds) for i in range(0, 3)])
at_least_two_rejects_result = sum([binomial_distribution(PISTOLS_QUANTITY, i, odds) for i in range(2, 11)])

print(f"{no_more_than_two_rejects_result:.3f}")
print(f"{at_least_two_rejects_result:.3f}")
