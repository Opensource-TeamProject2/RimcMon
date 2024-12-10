import logging
import requests

# 로깅 설정
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/insert_into_user_data.php"

# 프론트에서 넘어오는 실제 사용자 데이터 예시
# data = {
#     'name': '김진범',
#     'password': '1234',
#     'bio': '안녕하세요',
#     'tools': [
#         '<img src="https://img.shields.io/badge/Adobe Photoshop-31A8FF?style=flat-square&logo=Adobe Photoshop&logoColor=white"/>',
#         '<img src="https://img.shields.io/badge/Adobe Premiere-FF9B00?style=flat-square&logo=Adobe Photoshop&logoColor=white"/>'
#     ]
# }

def insert_user_data(data):
    params = {
        "name": data['name'],
        "password": data['password'],
        "bio": data['bio'],
        "tool": ', '.join([item.strip('"') for item in data['tool']]),  # 각 항목의 따옴표 제거
    }

    # 서버에 GET 요청 보내기
    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("응답 성공:", response.text)
    else:
        print("요청 실패:", response.status_code)