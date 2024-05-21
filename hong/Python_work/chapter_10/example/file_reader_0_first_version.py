from pathlib import Path
import os

print("현재 작업 디렉토리:", os.getcwd)
new_path = 'chapter_10/example'
os.chdir(new_path)
print("변경 후 디렉토리:", os.getcwd())
path = Path('pi_digits.txt')   
contents = path.read_text()
contents = contents.rstrip().lstrip()
# print(contents)
lines = contents.splitlines()
# for line in lines:
#     print(f"각 줄은={line}")
pi_string = ''
for line in lines:
    line = line.lstrip()
    pi_string += line

print(f"각 줄은={pi_string}")
print(len(pi_string))

# path = Path('chapter_10/example/pi_digits.txt')   #함수가 아니라 클래스