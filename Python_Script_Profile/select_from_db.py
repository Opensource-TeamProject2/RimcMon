import requests

def get_user_data(name, password):
    url = "http://opsw4.dothome.co.kr/select_from_user_data.php"  # PHP API URL

    try:
        # GET 요청 시 이름과 비밀번호를 쿼리 매개변수로 전달
        params = {
            'name': name,
            'password': str(password)  # 비밀번호를 문자열로 변환
        }
        response = requests.get(url, params=params)

        # 응답 상태 확인
        if response.status_code == 200:
            try:
                data = response.json()  # JSON 응답을 파싱

                # 데이터 확인 후 적절한 사용자 찾기
                if data and len(data) > 0:
                    for user_info in data:  # 배열을 순회하며 사용자 정보 확인
                        if user_info.get('name') == name and str(user_info.get('password')) == str(password):
                            return {
                                "name": user_info['name'],
                                "password": user_info['password'],
                                "bio": user_info['bio'],
                                "tool": user_info['tool']  # JSON 필드 이름 맞추기
                            }
                    return None  # 일치하는 사용자가 없는 경우
                else:
                    return None  # 데이터 없음
            except ValueError:
                raise ValueError("JSON 응답 파싱 실패")
        else:
            raise Exception(f"요청 실패: {response.status_code}")
    except requests.exceptions.RequestException as e:
        raise Exception(f"요청 중 오류 발생: {e}")