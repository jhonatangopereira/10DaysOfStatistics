# Day 4: Geometric Distribution I

'''
Task:
  The probability that a machine produces a defective product is 1/3. What is
  the probability that the first defect occurs the fifth item produced?
'''

def geometric_distribution(n:int, p:int) -> float:
  return ((1 - p) ** (n - 1)) * p

numerator, denominator = map(float, input().split())
items = int(input())

odds = numerator / denominator
result = geometric_distribution(items, odds)

print(f"{result:.3f}")
