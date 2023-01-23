# Day 5: Poisson Distribution II

'''
Task:
  The manager of a industrial plant is planning to buy a machine of either type A or type B.
  For each day"s operation:
    - The number of repairs, X, that machine A needs is a Poisson random variable with mean 0.88.
    The daily cost of operating A is CA = 160 + 40X^2.
    - The number of repairs, Y, that machine B needs is a Poisson random variable with mean 1.55.
    The daily cost of operating B is CB = 128 + 40Y^2.
  
  Assume that the repairs take a negligible amount of time and the machines are maintained nightly
  to ensure that they operate like new at the start of each day. Find and print the expected daily
  cost for each machine.
'''

# X and Y means
x_average, y_average = map(float, input().split())

# calculating daily cost for each product
x_daily_cost = 160 + 40 * (x_average + x_average ** 2)
y_daily_cost = 128 + 40 * (y_average + y_average ** 2)

print(f"{x_daily_cost:.3f}")
print(f"{y_daily_cost:.3f}")
