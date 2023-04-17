lst = ['H', 'e', 'l', 'l', 'o', ',', ' ', 'I', 'o', 'T']

# A. 리스트 마지막에 '!'를 추가한 후 출력
lst.append('!')
print(lst)

# B. 다섯 번째 요소('o')를 제거한 후 출력
del lst[4]
print(lst)

# C. 인덱스 4에 'a'를 넣은 후 출력
lst[4] = 'a'
print(lst)

# D. 리스트를 문자열로 변환하여 출력
string = ''.join(lst)
print(string)

# E. 리스트를 오름차순으로 정렬하여 출력
lst.sort()
print(lst)
