from random import uniform
from math import sqrt

def get_y(x):
  return 2 + sqrt(4 * x)

number_runs = 1000000
count = 0

for i in range(0, number_runs):
    if get_y(uniform(0, 1)) >= 3:
      count += 1
      
print(count / (number_runs * 1.0))