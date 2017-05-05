# # #
# This file is used to generate a list of outliers or just the next greatest   # values, and return information about those outliers such as price.

import csv
import statfunctions as stfnc
import helperfunctions as hlpr
import math

from collections import Counter
from matplotlib import pyplot as plt

with open("stock_data_file.csv", 'rb') as f:
  reader = csv.DictReader(f, delimiter=',')

  list_of_data_lists = hlpr.split_data_into_arrays(reader)
  indices_of_outliers_to_remove = []


  for data_list in list_of_data_lists:
    for outlier_index in indices_of_outliers_to_remove:
      del data_list[outlier_index]

  price_list = list_of_data_lists[0]

  sorted_prices = sorted(price_list)

  outlier_index = price_list.index(max(sorted_prices))
  print "Next Greatest price index in data set:"
  print outlier_index

  qrt_1 = stfnc.quantile(sorted_sale_prices, 0.25)

  # Many values in the data were above the 75th percentile,
  # checking for values at the top 99.9th percent
  qrt_3 = stfnc.quantile(sorted_sale_prices, 0.999)
  interqrt_range = stfnc.interquartile_range(sorted_sale_prices)
  scaled_intrqrt_range = 1.5 * interqrt_range

  lower_bound = qrt_1 - scaled_intrqrt_range
  upper_bound = qrt_3 + scaled_intrqrt_range

  upper_outliers = [x for x in sale_price_list if x > upper_bound]
  print upper_outliers

  def bucketize(point, bucket_size):
    return bucket_size * math.floor(point / bucket_size)

  def make_histogram(points, bucket_size):
    return Counter(bucketize(point, bucket_size) for point in points)

  def plot_histogram(points, bucket_size, title=""):
    histogram = make_histogram(points, bucket_size)
    plt.bar(histogram.keys(), histogram.values(), width=bucket_size)
    plt.title(title)
    plt.show()


  plot_histogram(msrp_list, 1000, "Sale Prices")

  # print scaled_sale_price_counts
  # price_counts = Counter(scaled_sale_price_counts)
  # xs = range(0,120000,100)
  # ys = [price_counts[x] for x in xs]
  # plt.bar(xs, ys)
  # plt.axis([0,120000,0,1000])
  # plt.xlabel("Date")
  # plt.ylabel("Sale Price")
  # plt.show()