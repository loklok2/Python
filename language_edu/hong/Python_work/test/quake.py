import requests
import matplotlib.pyplot as plt
import plotly.express as px
import json


url = 'https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_hour.geojson'

response = requests.get(url)
# data = response.json()      #json 방식이면 바로 파싱이 가능한 코드
contents = response.text       #만약 text파일로 받게 된다면 추가변환을 하는 코드
data = json.loads(contents)

data = data['features']


mags, lons, lats, eq_titles = [], [], [], []
for data1 in data:
    mag = data1['properties']['mag']
    lon = data1['geometry']['coordinates'][0]
    lat = data1['geometry']['coordinates'][1]
    eq_title = data1['properties']['title']

    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)


title = 'Global Eearthquackes 30days'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                      color=mags, color_continuous_scale='Viridis',
                      labels={'color':'Magnitude (scaled)'}, 
                      projection='natural earth', hover_name=eq_titles)
fig.show()