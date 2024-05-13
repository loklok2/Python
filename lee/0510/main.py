print('hello, world!')

a = 5       
b = 3.14
c = 'hello, world'
d = [1, 2, 3]
e = 'everything' or 'object'
print(type(a), type(b), type(c), type(d), type(e))

def calc(a,b):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)
    print(a // b)
    print(a ** b)


# a = 2
# b = 4
# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a ** b)

# a = 3.14
# b = 1.2

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a**b)


# a = 3.14
# b = 1
# print(a, b)
# calc(a,b)

# a = 5
# b = 3
# print(a, b)

# b, a = a, b

# # swap
# temp = a
# a = b
# b = temp
# print(a,b)

# PI = 3.14
# PI = 3.15
# print(PI)

# msg = 'hello, world!'
# print(msg, type(msg))

# print(msg.find('l'))

msg = 'hello, world!'
print(msg[0])
print(msg[1])
# msg[0] = 'H'
# print(msg)

a = 'hello'
b = 'world'
def add(a,b):
    return a+b
print(f'{a},{b},{add(1,2)}!\nhahahaha!')

msg = '     hello     '
print(len(msg))
print(len(msg.lstrip().rstrip()))
msg = msg.lstrip().rstrip()
print(type(msg.lstrip()))
print(len(msg))

msg = "hello, hello', hello, world!"
print(msg.replace('hello', '').replace(',','').lstrip().rsplit())
print(msg)