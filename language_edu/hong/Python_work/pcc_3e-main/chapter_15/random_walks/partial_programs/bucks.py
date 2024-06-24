import matplotlib.pyplot as plt
import numpy as np
import random

# 4x4 격자 생성
grid_size = 4
grid = np.zeros((grid_size, grid_size))

# 벌레의 랜덤 경로 생성 함수 (대각선 포함)
def generate_random_path(grid_size, steps):
    path = []
    current_position = (random.randint(0, grid_size-1), random.randint(0, grid_size-1))
    path.append(current_position)

    for _ in range(steps - 1):
        possible_moves = [
            (current_position[0] + dx, current_position[1] + dy)
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
            if 0 <= current_position[0] + dx < grid_size and 0 <= current_position[1] + dy < grid_size
        ]
        current_position = random.choice(possible_moves)
        path.append(current_position)

    return path

# 벌레의 경로 생성 (랜덤, 100 스텝)
steps = 100
path = generate_random_path(grid_size, steps)

# 경로를 따라가며 grid 값을 증가시킴
for position in path:
    grid[position] += 1

# 색상맵 설정 및 그래디언트 적용
plt.figure(figsize=(6, 6))
plt.xlim(-0.5, grid_size - 0.5)
plt.ylim(-0.5, grid_size - 0.5)

# 포인트 그리기
for i in range(grid_size):
    for j in range(grid_size):
        if grid[i, j] > 0:
            plt.scatter(j, i, color='black', s=100, alpha=min(1, grid[i, j] / max(grid.flatten())))

# 경로 그리기
x_coords, y_coords = zip(*path)
plt.plot(y_coords, x_coords, linestyle='-', color='red', marker='o', markersize=5)

# 격자 표시
plt.xticks(range(grid_size))
plt.yticks(range(grid_size))
plt.grid(True)

# 출력
plt.show()
