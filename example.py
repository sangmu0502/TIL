# 변수 사용법
# 파이썬

# 서버로부터 데이터를 가져와
# https://fakestoreapi.com/carts

import requests
from pprint import pprint as print

api_key = '373d7366cf3bdc4517c181a0844a363b'
# api_key = '87246d75elce26e1392a087b3dld88c5'
# 서울의 위도
lat = 37.56
# 서울의 경도
lon = 126.97

fake_url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

response = requests.get(fake_url).json()

# print(response)

# print(response['weather'])

print(response['weather'][0]['description'])

# 추가 공부 과제
# response['weather']
# response.get('weather') 
# .get 의 차이는 뭘까?
print(response.get['weather'][0]['description'])
