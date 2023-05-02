# 주어진 문자열에서 각 문자의 등장 횟수를 딕셔너리 형태로 출력하는 함수를 작성하시오.
import string


def count_chars(string):
    char_counts = {}
    for char in string:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

# 주어진 리스트에서 중복되지 않은 요소들만을 가진 새로운 집합을 만들고, 해당 집합의 요소 개수를 출력하는 함수를 작성하시오.


def count_unique_elements(lst):
    unique_set = set(lst)
    return len(unique_set)

# 주어진 튜플에서 첫 번째 요소를 키(key)로, 두 번째 요소를 값(value)으로 갖는 딕셔너리를 생성하는 함수를 작성하시오.


def tuple_to_dict(tup):
    dict = {}
    for item in tup:
        dict[item[0]] = item[1]
    return dict


# 주어진 문자열에서 'a'부터 'z'까지의 알파벳이 각각 몇 번 등장하는지 튜플 형태로 출력하는 함수를 작성하시오.


def count_alphabets(string):
    alphabet_counts = {}
    for char in string.lower():
        if char in string.ascii_lowercase:
            if char in alphabet_counts:
                alphabet_counts[char] += 1
            else:
                alphabet_counts[char] = 1
    return tuple(alphabet_counts.items())

# 주어진 리스트에서 홀수와 짝수를 구분하여 각각의 요소를 가진 새로운 리스트를 생성하는 함수를 작성하시오.


def separate_oddeven(lst):
    odd_lst = []
    even_lst = []
    for num in lst:
        if num % 2 == 0:
            even_lst.append(num)
        else:
            odd_lst.append(num)
    return (odd_lst, even_lst)


# 리스트를 입력받아 해당 리스트의 각 요소를 3번 반복한 리스트를 반환하는 함수를 작성하라. (함수와 리스트 개념 활용)


def repeat_elements_in_list(lst):
    new_lst = []
    for element in lst:
        new_lst.append(element * 3)
    return new_lst

# 문자열을 입력받아 해당 문자열의 첫 3글자를 반환하는 함수를 작성하라. (함수와 문자열 개념 활용)


def get_first_three_characters(s):
    return s[:3]


# 문자열을 입력받아 해당 문자열을 뒤집은 문자열을 반환하는 함수를 작성하라. (함수와 문자열 개념 활용)


def reverse_string(s):
    return s[::-1]
