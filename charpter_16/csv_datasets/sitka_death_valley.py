import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_2018_simple.csv'
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_ind = header_row.index('DATE')
    high_ind = header_row.index('TMAX')
    low_ind = header_row.index('TMIN')
    name_ind = header_row.index('NAME')

    dates, highs, lows = [], [], []
    name = ''
    for row in reader:
        current_date = datetime.strptime(row[date_ind], '%Y-%m-%d')
        name = row[name_ind] 
        try:
            high = int(row[high_ind]) 
            low = int(row[low_ind])
        except ValueError:
            print(f"Missing data for {current_date}")   
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)     


plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f'Daily temperatures highs and lows - 2018\n{name}'
plt .title(title, fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()