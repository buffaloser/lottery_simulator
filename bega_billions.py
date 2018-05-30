#!/usr/bin/env python

import random

#cash stats

player_dosh = 1000

#bb_drawing

winning_bega = []

for i in range (0,6):
  number = random.randint(1,59)
  while number in winning_bega:
    number = random.randint(1,59)
  winning_bega.append(number)

winning_bega.sort()

winning_powerbega = random.randint(1,59)

#quick pick variables

qp_bega = []

for i in range (0,6):
  number = random.randint(1,59)
  while number in qp_bega:
    number = random.randint(1,59)
  qp_bega.append(number)

qp_bega.sort()

qp_powerbega = random.randint(1,59)

#results

print("Today's winning numbers are: ")
print(winning_bega)
print(winning_powerbega)
