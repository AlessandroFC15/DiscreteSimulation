from random import randint

def get_rand_value_from_probability_table(probs):
  if not (0.999 <= sum(probs.values()) <= 1.00001):
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
  
tabela_vida_rolamento = {
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

tabela_tempo_espera = {
  5: 0.6,
  10: 0.3,
  15: 0.1
}

vida_acumulada = 0
num_sequencia = 1
tempo_espera_total = 0

while vida_acumulada < 20000:
  vida_rolamento = get_rand_value_from_probability_table(tabela_vida_rolamento)
  tempo_espera = get_rand_value_from_probability_table(tabela_tempo_espera)
  
  print(num_sequencia)
  print(vida_rolamento)
  print('--------------')
  
  vida_acumulada += vida_rolamento
  tempo_espera_total += tempo_espera
  num_sequencia += 1

print(tempo_espera_total)
  