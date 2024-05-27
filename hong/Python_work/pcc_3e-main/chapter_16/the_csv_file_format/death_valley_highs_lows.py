import csv
import matplotlib.pyplot as plt
from datetime import datetime
import os

# CSV 파일 경로
file_paths = [
    'the_csv_file_format/weather_data/sitka_weather_2021_simple.csv', 
    'the_csv_file_format/weather_data/death_valley_2021_simple.csv', 
    'the_csv_file_format/weather_data/san.csv'
]

# 데이터를 저장할 리스트
data = []

# 각 CSV 파일을 읽어서 데이터 리스트에 저장
for file_path in file_paths:
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        temp_data = []
        for row in reader:
            date = datetime.strptime(row['DATE'], '%Y-%m-%d')
            tmax = float(row['TMAX']) if row['TMAX'] else None
            tmin = float(row['TMIN']) if row['TMIN'] else None
            temp_data.append((date, tmax, tmin))
        data.append((file_name, temp_data))

plt.figure(figsize=(10, 6))

for name, temp_data in data:
    dates = [date for date, _, _ in temp_data]
    tmax_values = [tmax for _, tmax, _ in temp_data]
    tmin_values = [tmin for _, _, tmin in temp_data]
    plt.plot(dates, tmax_values, label=f'{name}_TMAX')
    plt.plot(dates, tmin_values, label=f'{name}_TMIN')

plt.xlabel('Date')
plt.ylabel('Temperature (°F)')
plt.title('Temperature Comparison')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()