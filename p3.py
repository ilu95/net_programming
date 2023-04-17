url = 'https://search.naver.com/search.naver?where=nexearch&ie=utf8&query=iot'

# url에서 '?' 이후의 파라미터들을 추출하여 딕셔너리로 만듦
params = url.split('?')[1].split('&')
dict_params = {}

for param in params:
    key, value = param.split('=')
    dict_params[key] = value

print(dict_params)
