from pathlib import Path
import json
import os

print(f"현재경로={os.getcwd()}")


# Read data as a string and convert to a Python object.
path = Path('mapping_global_datasets/eq_data/eq_data_1_day_m1.geojson')
contents = path.read_text(encoding='utf-8')             #데이터파일을 문자열로
all_eq_data = json.loads(contents)                      #문자열을 json 객체로
print(all_eq_data)

# Create a more readable version of the data file.
path = Path('mapping_global_datasets/eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents)