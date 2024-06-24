from pathlib import Path
import json
import os
import plotly.express as px


print(f"현재경로={os.getcwd()}")


# Read data as a string and convert to a Python object.
path = Path('mapping_global_datasets/eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')             #데이터파일을 문자열로
all_eq_data = json.loads(contents)                      #문자열을 json 객체로
# print(all_eq_data)
# Examine all earthquakes in the dataset.
all_eq_dicts = all_eq_data['features']  #key를 features로하는 value를 가져오는 것
# print(len(all_eq_dicts))
# path = Path('mapping_global_datasets/eq_data/readable_eq_data.geojson')
# readable_contents = json.dumps(all_eq_data, indent=4)
# path.write_text(readable_contents)

mags, lons, lats, eq_titles = [], [], [], []   # 빈 리스트 생성
for eq_dict in all_eq_dicts: 
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]  
    lat = eq_dict['geometry']['coordinates'][1]  
    eq_title = eq_dict['properties']['title']

    mags.append(mag)  # 생성된 빈 리스트에 삽입
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)

print(f"mag={mags[:10]}")
print(f"longgitude={lons[:5]}")
print(f"latitude={lats[:5]}")


title = "Global Earthquakes"
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title,
                      color=mags, color_continuous_scale='Viridis',
                      labels={'color':'Magnitude'}, 
                      projection='natural earth', hover_name=eq_titles)
fig.show()