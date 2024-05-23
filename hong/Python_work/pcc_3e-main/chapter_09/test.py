from random import randint
from random import choice

print(randint(1,6))


players = ['a', 'b', 'c', 'd', 'e', 'f']
print(choice(players))

##class 변수##
class Student:
    count = 0   ##count가 class변수
    def __init__(self):
        Student.count+= 1  ##class 변수값 변경
## 클래스 메소드 사용
    @classmethod
    def printing(self):
        print(f"클래스 메소드 출력={Student.count}")
print(f"{Student.count}") ##클래스변수를 접근
s = Student()
print(f"{Student.count}")
Student.printing() # class 메소드의 호출


def initialize():  #여러개의 함수를 리턴
    return 1,2,3

_,a,b = initialize() #여러개의 함수중 하나를 쓰지 않을려면 언더라인 사용하여 표현

a = [1,2,3]
b = [4,5,6]
mergeList = [*a, *b] # * 기호의 의미는 iterable 객체를 나타내고, unpacking역할을 한다 
print(mergeList)




### class instance에 대한 인덱싱과 슬라이싱 처리
class MyList:
    def __init__(self, data):
        self.data = data

    def __getitem__(self, index): #자주 사용된다
        return self.data[index]
    
mlist = MyList([1,2,3,4])
print(mlist[1:3])

##zip을 사용하여 딕셔너리 사용
s = ['s1', 's2', 's3']
num  = [5, 3, 7]
score = zip(s,num)
for a, b in score:
    print(f"[{a},{b}]")