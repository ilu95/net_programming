# 새로운 문자열 연습문제:
# 문자열에서 'o'의 개수를 출력하라.
string = "Hello, world! This is a string with some o's in it"
count = string.count('o')
print(count)

# 문자열에서 인덱스가 짝수인 문자들만 출력하라.
string = "Hello, world!"
for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])

# 문자열을 거꾸로 출력하라.
string = "Hello, world!"
reversed_string = string[::-1]
print(reversed_string)

# 문자열에서 중복을 제거한 후 출력하라.
string = "Hello, world! This is a string with some o's in it"
unique_chars = set(string)
unique_string = ''.join(unique_chars)
print(unique_string)

# 문자열을 정렬한 후 출력하라.
string = "Hello, world! This is a string with some o's in it"
sorted_string = ''.join(sorted(string))
print(sorted_string)

# 딕셔너리에서 key값만 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 3}
keys = my_dict.keys()
print(keys)

# 집합에서 중복을 제거한 후 출력하라.
my_set = set([1, 2, 3, 4, 3, 2, 1])
unique_set = set(my_set)
print(unique_set)

# 튜플의 길이를 출력하라.
my_tuple = (1, 2, 3, 4, 5)
length = len(my_tuple)
print(length)

# 함수를 이용해 문자열의 모든 문자를 대문자로 변경하여 출력하라.


def to_uppercase(string):
    return string.upper()


my_string = "Hello, world! This is a string with some o's in it"
uppercase_string = to_uppercase(my_string)
print(uppercase_string)

# 함수를 이용해 문자열의 모든 문자를 소문자로 변경하여 출력하라.


def to_lowercase(string):
    return string.lower()


my_string = "Hello, world! This is a string with some o's in it"
lowercase_string = to_lowercase(my_string)
print(lowercase_string)


# 새로운 딕셔너리 연습문제:
# 딕셔너리의 모든 key값을 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 3}
keys = my_dict.keys()
print(keys)

# 딕셔너리의 모든 value값을 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 3}
values = my_dict.values()
print(values)

# 딕셔너리에서 key값이 'A'인 value를 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 3}
value = my_dict['A']
print(value)

# 딕셔너리에서 value값이 2인 key를 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 2, 'D': 3}

result = []
for key, value in my_dict.items():
    if value == 2:
        result.append(key)

print(result)  # ['B', 'C']

# 딕셔너리의 모든 값을 더한 값을 출력하라.
my_dict = {'A': 1, 'B': 2, 'C': 3}

sum = 0
for value in my_dict.values():
    sum += value

print(sum)  # 6


# 새로운 집합 연습문제:
# 두 개의 집합의 합집합을 출력하라.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.union(set2)

print(result)  # {1, 2, 3, 4, 5}

# 두 개의 집합의 교집합을 출력하라.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.intersection(set2)

print(result)  # {3}

# 한 개의 집합에서 다른 집합과 겹치는 요소만 출력하라.
set1 = {1, 2, 3}
set2 = {3, 4, 5}

result = set1.difference(set2)

print(result)  # {1, 2}

# 한 개의 집합에서 다른 집합과 겹치는 요소를 제거한 집합을 출력하라.


def add_numbers(num1, num2):
    return num1 + num2

# 한 개의 집합에서 홀수인 요소만 출력하라.


def string_length(my_string):
    return len(my_string)


# 새로운 튜플 연습문제:
# 두 개의 튜플을 입력받아 각 요소의 합으로 이루어진 튜플을 반환하는 함수를 만들어라.
def tuple_sum(t1, t2):
    return tuple(x + y for x, y in zip(t1, t2))

# 세 개의 숫자를 입력받아 오름차순으로 정렬한 후 이를 튜플로 반환하는 함수를 만들어라.


def sort_tuple(num1, num2, num3):
    return tuple(sorted([num1, num2, num3]))

# 튜플에서 중복을 제거한 후 오름차순으로 정렬한 튜플을 반환하는 함수를 만들어라.


def remove_duplicates(t):
    return tuple(sorted(set(t)))


# 튜플의 인덱스 2의 요소를 출력하라.
t = (1, 2, 3, 4, 5)
print(t[2])

# 튜플의 첫 번째 요소부터 세 번째 요소까지 출력하라.
t = (1, 2, 3, 4, 5)
print(t[:3])

# 튜플의 모든 요소를 반복문을 사용하여 출력하라.
t = (1, 2, 3, 4, 5)
for item in t:
    print(item)

# 튜플의 모든 요소 중 짝수만 출력하라.
t = (1, 2, 3, 4, 5)
for item in t:
    if item % 2 == 0:
        print(item)

# 튜플의 모든 요소를 합한 값을 출력하라.
t = (1, 2, 3, 4, 5)
print(sum(t))
