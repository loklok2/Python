a = int(input())
numbers = []

for i in range(a):
    number = list(map(int, input().split()))
    numbers.append(number)

max_numbers = max(max(numbers))
min_numbers = min(min(numbers))

print(max_numbers, min_numbers)
