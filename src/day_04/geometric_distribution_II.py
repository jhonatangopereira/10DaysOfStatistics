# Day 4: Geometric Distribution II

'''
Task:
  The probability that a machine produces a defective product is 1/3. What is
  the probability that the first defect is found during the first five inspections?
'''

def geometric_distribution(n:int, p:int) -> float:
  return ((1 - p) ** (n - 1)) * p

numerator, denominator = map(float, input().split())
items = int(input())

odds = numerator / denominator
result = sum([geometric_distribution(i, odds) for i in range(1, items + 1)])

print(f"{result:.3f}")
