from pathlib import Path
import json


username = input("이름?")
path = Path('username.json')
contents = json.dumps(username)
path.write_text(contents)

print(f"Wellcome back, {username}!")