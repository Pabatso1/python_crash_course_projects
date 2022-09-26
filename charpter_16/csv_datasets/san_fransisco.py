import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'bloem.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    date_ind = header_row.index('DATE')
    high_ind = header_row.index('TMAX')
    low_ind = header_row.index('TMIN')
    name_ind = header_row.index('NAME')
    rain_ind = header_row.index('PRCP')

    dates, highs, lows, rains = [], [], [], []
    name = ''
    for row in reader:
        current_date = datetime.strptime(row[date_ind], '%Y-%m-%d')
        name = row[name_ind] 
        try: 
            high = int(row[high_ind])
            low = int(row[low_ind])
            rain = float(row[rain_ind])
        except ValueError:
            print(f"Missing data for {current_date}")   
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)
            rains.append(rain)

plt.style.use('seaborn')
fig, ax = plt.subplots()
#ax.plot(dates, highs, c='red', alpha=0.6)
#ax.plot(dates, lows, c='blue', alpha=0.6)
ax.plot(dates, rains, c='green', alpha=0.6)
ax.fill_between(dates, rains, facecolor='blue', alpha=0.1)
#ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

title = f'Daily rainfall from 2022\n{name}'
plt .title(title, fontsize=20)
plt.xlabel('', fontsize=12)
fig.autofmt_xdate()
plt.ylabel("Rainfall (in)", fontsize=12)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()