# Day 4: Binomial Distribution I

'''
Task:
  The ratio of boys to girls for babies born in Russia is 1.09:1. If there
  is 1 child born per birth, what proportion of Russian families with exactly
  6 children will have at least 3 boys?

  Write a program to compute the answer using the above parameters. Then print
  your result, rounded to a scale of 3 decimal places (i.e., 1.234 format).
'''

def fact(n):
  return 1 if n == 0 else n * fact(n - 1)

def comb(n, x):
  return fact(n) / (fact(x) * fact(n - x))

def b(x, n, p):
  return comb(n, x) * (p ** x) * ((1 - p) ** (n - x))

boys_ratio, girls_ratio = map(float, input().split())
odds = boys_ratio / girls_ratio
result = sum([b(i, 6, odds / (1 + odds)) for i in range(3, 7)])

print(f"{result:.3f}")
