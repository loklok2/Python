
import datetime
from pathlib import Path
import os
import csv
import plotly.express as px

print(f"현재경로={os.getcwd()}")

path = Path('world_fires_1_day.csv')
lines = path.read_text().splitlines()

reader = csv.reader(lines)
header_row = next(reader)

# 위도(latitude)와 경도(longitude)
# 화재가 발생한 날짜(acq_date)가 호버링할 때 나타나도록 설정

latitude, longitude, acq_date = [], [], []
for row in reader:
    try:
        lat = float(row[0])  
        lon = float(row[1])  
        acq = datetime.datetime.strptime(row[5], '%Y-%m-%d')  
    except ValueError:
        print(f"false data: {row}")
    else:
        latitude.append(lat)
        longitude.append(lon)
        acq_date.append(acq)

# plt.style.use('seaborn-v0_8')
# plt.figure(figsize=(10, 6))
# plt.scatter(longitude, latitude, color='red', alpha=0.5)
# plt.title('Worldwide Fire Incidents', fontsize=16)
# plt.xlabel('Longitude', fontsize=14)
# plt.ylabel('Latitude', fontsize=14)
# plt.grid(True)
# plt.show()

fig = px.scatter_geo(
    lat=latitude,
    lon=longitude,
    title='Worldwide Fire Incidents',
    projection='natural earth',
)
fig.show()