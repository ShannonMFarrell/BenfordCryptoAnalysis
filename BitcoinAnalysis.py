import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import log10, floor


def most_significant_digit(x):
    e = floor(log10(x))
    return int(x*10**-e)


def f(x):
    return most_significant_digit(abs(x))


# read in the BTC data
BTCPrices = pd.read_csv(r'/home/shannonfarrell/Documents/BTC-USD.csv')
BTCPrices = BTCPrices['Close']

BTCPrices_diff = BTCPrices.diff()

# count leading digits
data = BTCPrices_diff[BTCPrices_diff != 0]
counts = data.fillna(method='bfill').apply(f).value_counts()

total = counts.sum()

# expected number of each leading digit per Benford's law
benford = [total*log10(1 + 1./i) for i in range(1, 10)]


# plot actual vs expected
bins = np.arange(9)
error_config = {'ecolor': '0.5'}

r1 = plt.bar(bins, counts.values, 0.35, alpha=0.4, color='g',
             error_kw=error_config, label='actual')
r2 = plt.bar(bins + 0.35, benford, 0.35, alpha=0.4, color='r',
             error_kw=error_config, label='expected')
plt.xlabel('Most significant digit')
plt.ylabel('Occurence count')
plt.title('Leading digit in Bitcoin Open price')
plt.xticks(bins + 0.35, bins+1)
plt.legend()

plt.show()
