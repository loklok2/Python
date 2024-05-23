from pathlib import Path
import csv
import os
import matplotlib.pyplot as plt
from datetime import datetime
print(f"현재경로={os.getcwd()}")

path = Path('the_csv_file_format/weather_data/death_valley_2021_simple.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

for index, column_header in enumerate(header_row):
    print(index, column_header)

dates, highs, lows =[], [], []

for row in reader:
    current_date = datetime.strptime(row[2], '%Y-%m-%d')
    try:
        high = int(row[4])
        low = int(row[5])
        # avg = int(row[3]) #결측치 없어서 오류발생 ValueError: invalid literal for int() with base 10: 
    except ValueError:
        continue
        # print(f"missing data for{current_date}")
    else:
        lows.append(low)    
        highs.append(high)
        dates.append(current_date)
        # avgs.append(avg)         
print(lows)


plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(dates, highs, color='red', alpha=0.5)
ax.plot(dates, lows, color='blue', alpha=0.5)
# ax.plot(dates, avgs, color='green', alpha=0.5)
ax.fill_between(dates, highs, lows, facecolor='yellow', alpha=0.5)

title = "Daily High and Low Temperatures, 2021\nDeath Valley, CA"
ax.set_title('High Temperatures', fontsize=24)
ax.set_xlabel('', fontsize=10)
fig.autofmt_xdate()
ax.set_ylabel("Temperature (F)", fontsize=10)
ax.tick_params(labelsize=8)

plt.show()