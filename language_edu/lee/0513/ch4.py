data = [1, 2, 3]      #list를 만드는 방법

for d in data:              #for문을 돌리는 방법 ':' 
    print(d, end='')        #end 하나씩 끊어서 나오게 해준다
data[1] = 5
string = 'hello'
print('-',data[1])
for s in string:
    print(s, end='')
# string[1] = 'E'      
# print('-',string[1])      #string은 만들어놓으면 못바꾼다
data = (1, 2, 3)             #tuple 중요 
print(data)
for i in data:
    print(i)


data2 = [i**2 for i in data if i**2 < 5]   #for문을 돌리면서 자료형을 생성할 수 있다
print(data2, type(data2))

data3 = []
for i in data:
    if i**2 < 5:
        data3.append(i**2)
    print(data3)


# for(i = 0; i <10 ; i++)
# for(item : array)
data = [1, 2, 3, 4, 5]        #대부분의 파이썬 코드는 이렇게 작성된다 꼭 알아두자
for d in data:
    print(d)
# [1, 5)
for i in range(10):             # : 콜론 잊지말자, 탭하여 들여쓰기 잊지말자
    print(i, end='')
    print(i, end='')
    for d in data:              # 이중for문 들여쓰기 콜론 잊지말자
        print(d)

for idx, d in enumerate(data):      
    print(idx, d)


#stirng, list, tuple 공부

data_2d = [[1,2,3], [4,5,6]]
for data in data_2d:
    for d in data:
        print(d, end='')
    print()


for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i} *{j} = {i*j}')
        print()

##range(1, 11) - 1부터 10까지
#sum min max average
# for k in range(1,11):
#     for n in range(1, 11):
#         print(f)

# a = everything or object
data = [1, 3.14, 'hello', max, range]
for d in data:
    print(d, type(d))
    print('next')


for i in range(len(data)):
    print(data[i], type(i))


data = list(range(1,11))
# [1, 5) 1은 포함되는데 5는 포함 안된다~~
print(data, data[1:5], sep='\n')
print(data, data[-1], sep='\n') #마지막꺼 출력하는방법
print(data, data[-2], sep='\n') #두번째 마지막꺼 출력 
print(data, data[1:-1], sep='\n') #잘안쓰긴함
print(data, data[1:5], sep='\n') 
print(data, data[:5], data[5:], sep='\n') #데이터를 적절한 비율로 자르고 싶을때 쓴다 알아두자
print(data, data[::-1],sep='\n') #뒤집어서 보여준다 
# print(data, data[::-1],sorted(data, reversed=True), sep='\n')

def swap(a, b):
    temp = a
    a = b
    b = temp
    #a , b = b, a

a, b = 1, 2
print(a, b)
swap(a, b)
print(a, b)

data = [1, 2, 3]   #tuple은 안바뀌기 때문에 디버그를 할때 []를 ()로 바꿔서 찾자
# data2 = data    list의 특징 때문에 사용이 안됨, 이렇게 작성하면 까다로우니 피하자
data2 = data[:]
data2[1] = 5
print(data, data2, sep='\n')  