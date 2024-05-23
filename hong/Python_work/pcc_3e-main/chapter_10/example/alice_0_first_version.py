from pathlib import Path


path = Path('alice2.txt') #No such file or directory
contents = path.read_text(encoding='utf-8')