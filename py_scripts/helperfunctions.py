# # #
# More advanced stat functions and IO tools
# # #
import random
import math

def split_data_into_arrays(r):
  price_list = []
  date_list = []

  list_of_data_lists = [sale_price_list, msrp_list, year_list, make_list, model_list, engine_list, transaction_id_list]

  for row in r:
    row_price = row["price"]
    row_date = row["date"]

    sale_price_list.append(float(row_price))
    make_list.append(row_date)

  return list_of_data_lists

def split_data_fractionally(data, prob):
  results = [],[]
  for row in data:
    results[0 if random.random() < prob else 1].append(row)
  return results

def train_test_split(x, y, test_pct):
  data = zip(x, y)
  train, test = split_data_fractionally(data, 1 - test_pct)
  x_train, y_train = zip(*train)
  x_test, y_test = zip(*test)
  return x_train, x_test, y_train, y_test

def dot(v, w):
  # Compute dot product
  return sum(v_i * w_i for v_i, w_i in zip(v, w))

def sum_of_squares(v):
  return dot(v, v)

def mean(x):
  return sum(x) / len(x)

def de_mean(x):
  x_bar = mean(x)
  return [x_i - x_bar for x_i in x]

def variance(x):
  n = len(x)
  deviations = de_mean(x)
  return sum_of_squares(deviations) / (n - 1)

def standard_deviation(x):
  return math.sqrt(variance(x))

def covariance(x, y):
  n = len(x)
  return dot(de_mean(x), de_mean(y)) / (n - 1)

def correlation(x, y):
  stdev_x = standard_deviation(x)
  stdev_y = standard_deviation(y)
  if stdev_x > 0 and stdev_y > 0:
    return covariance(x, y) / stdev_x / stdev_y
  else:
    return 0

# # # This section defines least-squares model related functions  # # #
def predict_y(alpha, beta, x_i):
  return beta * x_i + alpha

def error(alpha, beta, x_i, y_i):
  return y_i - predict_y(alpha, beta, x_i)

def sum_of_squared_errors(alpha, beta, x, y):
  return sum(error(alpha, beta, x_i, y_i) ** 2 for x_i, y_i in zip(x,y))

def least_squares_fit(x, y):
  beta = correlation(x, y) * standard_deviation(y) / standard_deviation(x)
  alpha = mean(y) - beta * mean(x)
  return alpha, beta

def total_sum_of_squares(y):
  return sum(v ** 2 for v in de_mean(y))

def r_squared(alpha, beta, x, y):
  return 1.0 - (sum_of_squared_errors(alpha, beta, x, y) / total_sum_of_squares(y))