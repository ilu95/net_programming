str = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

str = str.split('?')
print(str)

str = str[1].split('&')
print(str)

for i in range(3):
    str[i] = str[i].split('=')

result = {str[0][0]: str[0][1], str[1][0]: str[1][1], str[2][0]: str[2][1]}

print(result)
