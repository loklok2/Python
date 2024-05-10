name = ['lok', 'loklok', 'lokloklok']
print(name)
print(name[0])
print(name[1])
print(name[2])
msg = 'hello'
print(name[0], msg)
print(name[1], msg)
print(name[2], msg)
ride = ['benz', 'audi', 'rangelover']
msg1 = 'I must have'
msg2 = 'got it'
print(msg1, ride[0], msg2)
print(msg1, ride[1], msg2)
print(msg1, ride[2], msg2)

name = ['d', 'dd', 'ddd', 'dddd']
msg3 = 'invite dinner'
print(msg3, name[0])
print(msg3, name[1])
print(msg3, name[2])
print(msg3, name[3])
print(name[0])
name.remove('d')
name.append('d2')
print(name)
print(msg3, name[0])
print(msg3, name[1])
print(msg3, name[2])
print(msg3, name[3])
msg4 = 'find a big table' #3-6
name.insert(4,'d3')
name.insert(3,'d4')
name.append('d5')
print(name)
print(msg3, name[0])
print(msg3, name[1])
print(msg3, name[2])
print(msg3, name[3])
print(msg3, name[4])
print(msg3, name[5])
print(msg3, name[6])
msg5 = 'sorry dinner impassible count 2 people'
popped_name = name.pop()
print(name)
popped_name = name.pop()
print(name)
popped_name = name.pop()
print(name)
popped_name = name.pop()
print(name)
popped_name = name.pop()
print(name)
msg6 = 'wait people do not cancle dinner'
print(msg6, name)
del name[1]
print(name)
del name[0]
print(name)