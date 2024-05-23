from pathlib import Path
import os
print("현재 작업 디렉토리:", os.getcwd)
new_path = 'chapter_10/example'
os.chdir(new_path)

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
print(f"줄 수= {len(lines)}")
for line in lines[:5]:
    print(f"각줄={line}")
    pi_string += line.lstrip()

# print(f"{pi_string[:52]}...")
# print(len(pi_string))
birthday = input("Enter your birthday, in the form mmddyy:")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi")
else:
    print("Your birthday does not appear in the first million digits of pi")