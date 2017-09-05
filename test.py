import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
print s

s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'], index=['A', 'Z', 'C', 'Y', 'E'])
print s

d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100, 'Austin': 450, 'Boston': None}
cities = pd.Series(d)
print cities
print cities['Chicago']
print cities[['Chicago', 'Portland', 'San Francisco']]

print cities[cities < 1000]
less_than_1000 = cities < 1000
print less_than_1000
print "\n"
print cities[less_than_1000]

print 'Old value:', cities['Chicago']
cities['Chicago'] = 1400
print 'New value:', cities['Chicago']

print cities[cities < 1000]
print '\n'
cities[cities < 1000] = 750

print cities[cities < 1000]

print 'Seattle' in cities
print 'San Francisco' in cities

print cities / 3

print np.square(cities)

print cities[['Chicago', 'New York', 'Portland']]
print '\n'
print cities[['Austin', 'New York']]
print '\n'
print cities[['Chicago', 'New York', 'Portland']] + cities[['Austin', 'New York']]

print cities.notnull()

print cities.isnull()
print '\n'
print cities[cities.isnull()]

data = {'year': [2010, 2011, 2012, 2011, 2012, 2010, 2011, 2012],
        'team': ['Bears', 'Bears', 'Bears', 'Packers', 'Packers', 'Lions', 'Lions', 'Lions'],
        'wins': [11, 8, 10, 15, 11, 6, 10, 4],
        'losses': [5, 8, 6, 1, 5, 10, 6, 12]}
football = pd.DataFrame(data, columns=['year', 'team', 'wins', 'losses'])
print football
