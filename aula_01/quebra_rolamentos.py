from random import randint

probabilities = {
  1000: 0.10,
  1100: 0.13,
  1200: 0.25,
  1300: 0.13,
  1400: 0.09,
  1500: 0.12,
  1600: 0.02,
  1700: 0.06,
  1800: 0.05,
  1900: 0.05
}

def get_rand_value_from_probabilities(probs):
  if sum(probs.values()) != 1:
    print('Invalid table')
    return
  
  last_value = 0
  
  upper_limits = {}
  
  for key in probs:
    upper_limits[key] = last_value + (probs[key] * 100)
    last_value = upper_limits[key]

  rand = randint(1, 100)
  
  for key in upper_limits:
    if rand <= upper_limits[key]:
      return key
  
vida = 0
n = 0
  
for i in range(0, 100000):
  vida += get_rand_value_from_probabilities(probabilities)
  n += 1
  
print(vida / n)
  
  
