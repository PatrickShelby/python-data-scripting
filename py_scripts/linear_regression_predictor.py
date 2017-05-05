# # #
# With a pre determined alpha and beta, this will calculate an estimate of Y  # for a given X using simple linear regression
# # #
import statfunctions as stfnc
import helperfunctions as hlpr

import csv
from collections import Counter
from matplotlib import pyplot as plt

price_predictions = []
new_rows = []

# Calculate these two:
alpha = 369.338576
beta = 0.9523546

def guess_price(x):
  return beta * x + alpha

with open("myfile.csv", 'rb') as f:
  reader = csv.DictReader(f, delimiter=',')

  for row in reader:
    price_estimate = guess_price(int(row["independent_var"]))
    row["dependent_var"] = int(price_estimate)
    new_rows.append(row)

keys = ['','']
print keys
with open("file_to_write_to.csv", 'a+') as f:
    writer = csv.DictWriter(f, keys, delimiter=',')
    writer.writeheader()
    for row in new_rows:
      writer.writerow(row)
