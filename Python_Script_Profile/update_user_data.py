import requests

# 요청을 보낼 URL
url = "http://opsw4.dothome.co.kr/update_user_data.php"

# 데이터 전송 함수
def update_user_data(data):
    params = {
        "name": data['name'],
        "password": data['password'],
        "bio": data['bio'],
        "tool": ', '.join([item.strip('"') for item in data['tool']]),  # 각 항목의 따옴표 제거
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        print("응답 성공:", response.text)
    else:
        print("요청 실패:", response.status_code)