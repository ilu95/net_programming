import random


temp = int(random.randrange(1, 50))
temp = temp.to_bytes(4, 'big')
str(temp)

print(temp, type(temp))

# temp = int.from_bytes(temp, 'big')
int(temp)

print(temp, type(temp))
