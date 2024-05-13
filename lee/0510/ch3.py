data = [1, 2, 3, 3, 3]
print(data, type(data))

# data = list()               #파이썬의 객체생성 자바의 객체생성문법과 다름 # 잘안씀 
# print(data, type(data))

print(data[0])
print(data[1])
print(data[2])
# print(data[3])  #IndexError: list index out of range
print(len(data))

data.append(6)
data.append(7)
data.append(8)
data.append(9)
data.append(10)
print(data, len(data))

data[3] = 4
data[4] = 5
print(data, len(data))
print(data, len(data), sum(data), min(data), max(data))

data = list(range(10,0,-1))
print(data,type(data),sorted(data))


# 20
# 10 9 8 7 6 5 4 3 2 1 
# 합계를 구하시오, 정렬하시오, 최댓값을 찾으시고, 최소값을 찾으시오

data = list(map(int, input().split()))    #input type은 무조건 String, type을 바꿔줘야함 # 이러한 형식 자주 사용함 값을 받을때
print(data,type(data), type(data[0]))
print(sum(data))


number = int('56')
print(number, type(number))


data = [1, 2, 3]
del data[1]
print(data)

data = [1,2,3.14, 'hello', len, range(5)]           #파이썬은 모든것을 object로 본다 즉, 객체로 본다
# print(data, type(data))
for d in data:
    print(d, type(d))


data = [1,2,3,4,5]
print(data[len(data)-1])
print(data[::-1])

data = data[::-1]
# data.reverse()
data.append(1)
print(data)

msg = 'age'
msg == (msg ==msg[::-1])


data.append(1)
print(data)
data.pop()
print(data)

data.insert(1, 1)
print(data)

del data[1]
print(data)

data.remove(1)
print(data)

print(sorted(data)) 
print(data)

sorted_data = sorted(data) #원래 것을 쓰겠다
print(sorted_data)          

data.sort()
print(data)