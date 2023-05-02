url = 'https//search.daum.net/search?search?w=tot&q=bigdata'

# url에서 '?' 이후의 파라미터들을 추출하여 딕셔너리로 만듦
params = url.split('?')[2].split('&')
dict_params = {}

for param in params:
    key, value = param.split('=')
    dict_params[key] = value

print(dict_params)
dict_params['q'] = 'iot'
print(dict_params)
