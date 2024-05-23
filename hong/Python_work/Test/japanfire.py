from pathlib import Path
import plotly.express as px
import json
import os

print(f"현재경로={os.getcwd()}")

path = Path('test/modis_2022_japan.csv')
contents = path.read_text(encoding='utf-8')
data = json.loads(contents)


