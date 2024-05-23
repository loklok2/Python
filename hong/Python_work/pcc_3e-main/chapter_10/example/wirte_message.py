from pathlib import Path
import os

print(f"현재경로={os.getcwd()}")

path = Path('chapter_10/example/programming.txt')
path.write_text("I love programming")