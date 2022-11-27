# Day 0: Mean, Median, and Mode

'''
Given an array, X, of N integers, calculate and print the respective mean,
median, and mode on separate lines. If your array contains more than one
modal value, choose the numerically smallest one.
'''

def calculate_mean(X:list):
  return sum(X) / len(X)

def calculate_median(X:list):
  middle = len(X) / 2
  if middle % 1 == 0: # even length
    median = (X[int(middle - 1)] + X[int(middle)]) / 2
  else: # odd length
    median = X[int(middle - 0.5)]
  return median

def calculate_mode(X:list):
  most_commom_element = actual_element = 0
  most_commom_counter = actual_counter = 0
  for element in X:
    if actual_element != element:
      actual_element = element
      actual_counter = 1
    else:
      actual_counter += 1
    if actual_counter > most_commom_counter:
      most_commom_element = element
      most_commom_counter = actual_counter
    actual_element = element
  return most_commom_element


N = int(input())
X = sorted(list(map(int, input().split())))

print(f"{calculate_mean(X):.1f}")
print(f"{calculate_median(X):.1f}")
print(f"{calculate_mode(X)}")
