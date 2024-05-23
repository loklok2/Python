from pathlib import Path
import json


path = Path('username.json')        
if path.exists():                       #josn에 데이터가 있으면
    contents = path.read_text()
    username = json.loads(contents)
    print(f"Welcome back, {username}!")
else:                                       #josn에 데이터가 없으면 새로 생성
    username = input("What is your name? ")   
    contents = json.dumps(username)
    path.write_text(contents)
    print(f"We'll remember you when you come back, {username}!")