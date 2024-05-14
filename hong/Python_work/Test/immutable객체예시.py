def modify_string(s):  ##immutable 객체
    s = s+ "world"
    print(f"함수내 출력={s}")

st = "hello"    ##변경불가
modify_string(st) ##string을 전달하므로
print(st)

def modify_string(number):  ##immutable 객체
    number = number + 10
    print(f"함수내 출력={number}")

num = 10    ##변경불가
modify_string(num) ##num을 전달하므로
print(f"함수 종료후 출력={num}")
