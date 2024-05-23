from random import choice
import matplotlib.pyplot as plt

class RandomWalk:
    """A class to generate random walks."""

    def __init__(self, num_points=100, rows=10, cols=10):
        """Initialize attributes of a walk."""
        self.num_points = num_points            #총점의 갯수
        self.rows = rows                        #행
        self.cols = cols                        #열
        # All walks start at (0, 0).    
        self.x_values = [0]                     # 각점의 x좌표 값
        self.y_values = [0]                     # 각점의 y좌표 값
        self.board = [[0 for _ in range(cols)] for _ in range(rows)]

    def fill_walk(self, x_start=0, y_start=0):
        """Calculate all the points in the walk."""
        # Keep taking steps until the walk reaches the desired length.
        x = x_start 
        y = y_start  
        while len(self.x_values) < self.num_points:
            #x,y는 현재 좌표
            # Decide which direction to go, and how far to go.
            x_new = x + choice([1, 0, -1])     #랜덤으로 선택된 3개 중 값을 추가하여 새로운x좌표 생성
            y_new = choice([1, 0, -1])          #랜덤으로 선택된 3개 중 값을 추가하여 새로운y좌표 생성
            if x_new <= 0 or x_new >= self.rows or y_new <=0 or y_new >= self.cols:
                #새로운 좌료가 경계내에 있는지 확인, 그렇지 않으면 다음으로 반복
                continue                              
            x, y= x_new, y_new              #현재 좌표를 새로운 좌표로 업데이트
            self.board[x][y] += 1           #보에서 해당하는 셀의 값을 증가


        