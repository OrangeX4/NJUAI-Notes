str = input()
num = sum([int(ch) ** 3 for ch in str])

print(num == int(str))