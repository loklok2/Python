from pathlib import Path
import os
print(f"현재경로={os.getcwd()}")

path = Path('guest.txt')
path.write_text("홍길동", encoding='utf-8')

with path.open('a', encoding='utf-8') as file:
    file.write("\n금수강산")

with path.open('a', encoding='utf-8') as file:
    file.write("\n백두산")