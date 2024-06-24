# p = ['피자1', '피자2', '피자3']
# for p1 in p:
#     # print(p1)
#     print(f' 나는 {p1.title()} 좋습니다' )
#     print(f"나는 피자를 정말 사랑합니다")


# a = ['강아지', '강아지2', '강아지3']
# for a1 in a:
#     print(a1)

# data =range(100) 
# print(data, type(data))
# for d in data:
#     print(d, end=' ')


#105page  꼭 기억하자

#20까지 세기
# data = range(1, 21)
# for d in data:
#     print(d, end=' ')


# 백만까지 리스트 만들기
# data = range(1, 1000001)
# for d in data:
#     print(d, end=' ')


# 백만까지 더하기
# data = range(1, 1000001)
# print(min(data))                or print(sum(range(1, 10)))
# print(max(data))
# print(sum(data))

# 홀수리스트 만들기
# data = range(1, 21, 2)
# for d in data:
#     print(d, end=' ')


# 3의 배수 만들기    
# data = range(3, 31, 3)
# for d in data:
#     print(d, end=' ')


# 세제곱 만들기
# data = []
# for value in range(1, 11):
#     data.append(value**3)
#     print(data)

#세제곱 내포문으로 만들기 
# data = [value**3 for value in range(1,11)]
# print(data)


#슬라이스

# gh = ['home', 'home1', 'hom2', 'home3']
# print('리스트의 첫 세항목은 출력하세요',gh[0:3])
# print('리스트의 중간 세항목은 출력하세요',gh[1:3])
# print('리스트의 중간 세항목은 출력하세요',gh[0:-3])


# 5-1 

# car = 'subaru'
# print("Is car' == 'subaru'? I predict Ture.")
# print(car == 'subaru')

# print("\nIs car == 'audi'? I predict Ture.")
# print(car == 'audi')


# lok2 = 'genious'
# print("Is lok2 == 'genious? I predict Ture")
# print(lok2 == 'genious')

# print("\nIs lok2 == 'crack'? I predict Ture.")
# print(lok2 == 'crack')



# # 5-3
# alien_color = 'green'
# if 'blue' in alien_color:
#     print('5점획득')
# elif alien_color != 'green':
#     print('10점획득')

# print("\n 점수확인하세요")



# score = int(input())
# if (90 <= score) and (score <= 100):
#     print('A')
# elif (80 <= score) and (score < 90):
#     print('B')
# else:
#     print('F')


#5-6

# age = int(input())
# if 2 < age:
#     print('baby')
# elif (age <)





#5-8

ad = ['admin', 'admin1', 'admin2','admin3', 'admin4']
for d in ad:
    print(d)
    if d == 'admin':
        print(d,'관리자님 안녕하세요. 상태보고서를 보시겠습니까')
    elif d != 'admin':
        print(d,'누구세요?' )

ad = []
for d in ad:
    print(d)
    for d in ad:
    if d == 'admin':
        print(d,'관리자님 안녕하세요. 상태보고서를 보시겠습니까')
    else:
        print("사용자가 있어야합니다")