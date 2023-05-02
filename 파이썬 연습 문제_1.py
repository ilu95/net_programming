# 문자열 연습문제 변형:
# 주어진 문자열의 중간 문자를 출력하라. (단, 문자열 길이가 짝수일 경우 중간의 두 문자를 출력)
# 문자열의 마지막 5개 문자를 반대로 출력하라.
# 주어진 문자열에서 모음(a, e, i, o, u)의 개수를 세어 출력하라.
# 문자열에서 공백을 모두 제거한 후 출력하라.
# 주어진 문자열에서 첫 번째와 마지막 문자를 제외한 문자열을 출력하라.
# 주어진 문자열
string = "Hello, World!"

# 중간 문자 출력
middle_index = len(string) // 2
if len(string) % 2 == 0:
    print(string[middle_index-1:middle_index+1])
else:
    print(string[middle_index])

# 마지막 5개 문자 반대로 출력
print(string[-5:][::-1])

# 모음 개수 세기
vowel_count = 0
for char in string:
    if char in "aeiouAEIOU":
        vowel_count += 1
print(vowel_count)

# 공백 제거 후 출력
print(string.replace(" ", ""))

# 첫 번째와 마지막 문자를 제외한 문자열 출력
print(string[1:-1])


# 리스트 연습문제 변형:
# 리스트의 첫 번째와 마지막 요소를 출력하라.
# 리스트의 요소를 거꾸로 출력하라.
# 리스트에서 중복된 값을 제거한 후 출력하라.
# 리스트에서 짝수만 출력하라.
# 주어진 리스트에서 인덱스가 홀수인 요소만 제거한 새로운 리스트를 출력하라.
# 주어진 리스트
my_list = [1, 2, 3, 4, 5]

# 첫 번째와 마지막 요소 출력
print(my_list[0], my_list[-1])

# 요소 거꾸로 출력
print(my_list[::-1])

# 중복된 값 제거 후 출력
my_list = list(set(my_list))
print(my_list)

# 짝수만 출력
for num in my_list:
    if num % 2 == 0:
        print(num)

# 홀수 인덱스 제거한 새로운 리스트 출력
new_list = [elem for index, elem in enumerate(my_list) if index % 2 == 0]
print(new_list)


# 딕셔너리 연습문제:
# 딕셔너리의 모든 키를 출력하라.
# 딕셔너리의 모든 값을 출력하라.
# 딕셔너리의 값들 중 중복된 값만 출력하라.
# 딕셔너리에서 특정 키-값 쌍을 삭제한 후 출력하라.
# 딕셔너리에서 특정 키의 값만 변경한 후 출력하라.
# 주어진 딕셔너리
my_dict = {"apple": 1, "banana": 2, "orange": 3, "grape": 2}

# 모든 키 출력
print(my_dict.keys())

# 모든 값 출력
print(my_dict.values())

# 중복된 값 출력
duplicates = []
for value in my_dict.values():
    if list(my_dict.values()).count(value) > 1 and value not in duplicates:
        duplicates.append(value)
print(duplicates)

# 특정 키-값 쌍 삭제 후 출력
del my_dict["apple"]
print(my_dict)

# 특정 키의 값 변경 후 출력
my_dict["banana"] = 5
print(my_dict)


# 집합 연습문제:
# 두 개의 집합의 합집합을 출력하라.
# 두 개의 집합의 차집합을 출력하라.
# 두 개의 집합의 교집합을 출력하라.
# 두 개의 집합 중 하나의 집합에만 있는 요소를 출력하라.
# 두 개의 집합이 부분집합인지를 판별하는 함수를 작성하라.
# 두 개의 집합
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# 합집합 출력
print(set1.union(set2))

# 차집합 출력
print(set1.difference(set2))

# 교집합 출력
print(set1.intersection(set2))

# 하나의 집합에만 있는 요소 출력
print(set1.symmetric_difference(set2))

# 부분집합 판별 함수


def is_subset(set1, set2):
    return set1.issubset(set2)


# 함수 연습문제:
# 숫자를 입력받아 해당 숫자의 제곱을 출력하는 함수를 작성하라.
def square(num):
    return num ** 2
# 두 개의 숫자를 입력받아 더한 값을 출력하는 함수를 작성하라.


def add(num1, num2):
    return num1 + num2

# 문자열을 입력받아 각 문자의 개수를 사전 형태로 출력하는 함수를 작성하라.


def count_characters(string):
    char_count = {}
    for char in string:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

# 리스트를 입력받아 리스트의 요소 중 중복된 값만 출력하는 함수를 작성하라.


def print_duplicates(lst):
    duplicates = []
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] == lst[j] and lst[i] not in duplicates:
                duplicates.append(lst[i])
    return duplicates

# 두 개의 숫자를 입력받아 작은 수를 반환하는 함수를 작성하라.


def find_smaller(num1, num2):
    if num1 < num2:
        return num1
    else:
        return num2
