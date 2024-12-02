import streamlit as st
import pymssql
import sys
import os
# 프로젝트 루트 경로 추가
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'Profile_BE')))

from select_from_UserProfile import get_user_profile
from insert_into_UserProfile import update_user_stack, update_user_bio

# DB 연결 함수 (예시)
def get_user_credentials(username):
    try:
        connection = pymssql.connect(
            server="localhost:1433",
            user="sa",
            password="123aaa!@#",
            database="rmc_user",
            charset="utf8"
        )
        cursor = connection.cursor(as_dict=True)
        query = "SELECT user_id, password FROM UserProfile WHERE user_id = %s"
        cursor.execute(query, (username,))
        user = cursor.fetchone()
        cursor.close()
        connection.close()
        return user
    except Exception as e:
        st.error(f"DB 연결 오류: {e}")
        return None

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# 로그인 페이지
if not st.session_state.logged_in:
    st.title("로그인")
    username = st.text_input("아이디")
    password = st.text_input("비밀번호", type="password")

    if st.button("로그인"):
        user = get_user_credentials(username)
        if user and user['password'] == password:
            # 비밀번호가 일치하면 로그인 상태로 설정
            st.session_state.logged_in = True
            st.session_state.user_id = username
        else:
            st.error("아이디나 비밀번호가 올바르지 않습니다.")
else:
    # 로그인 후 마이 페이지 UI
    user_id = st.session_state.user_id

    # 사이드바
    st.sidebar.header("내 정보")
    st.sidebar.write(f"**아이디**: {user_id}")
    
    # 로그아웃
    if st.sidebar.button("로그아웃"):
        st.session_state.logged_in = False
        st.session_state.user_id = None

    # 마이 페이지 UI
    st.title("마이 페이지")

    # 툴 리스트
    tools = [
        {"name": "Adobe Photoshop", "badge_url": "https://img.shields.io/badge/Adobe Photoshop-31A8FF?style=flat-square&logo=Adobe Photoshop&logoColor=white"},
        {"name": "Adobe Illustrator", "badge_url": "https://img.shields.io/badge/Adobe Illustrator-FF9A00?style=flat-square&logo=Adobe Illustrator&logoColor=white"},
        {"name": "Figma", "badge_url": "https://img.shields.io/badge/Figma-F24E1E?style=flat-square&logo=Figma&logoColor=white"},
        {"name": "Visual Studio Code", "badge_url": "https://img.shields.io/badge/Visual Studio Code-007ACC?style=flat-square&logo=Visual Studio Code&logoColor=white"},
    ]

    # 스택 선택 UI
    selected_stack = []
    for tool in tools:
        if st.checkbox(tool["name"], key=tool["name"]):
            selected_stack.append(f'<img src="{tool["badge_url"]}"/>')

    # 선택한 스택 저장
    if st.button("스택 추가"):
        if selected_stack:
            new_stack = " ".join(selected_stack)
            update_user_stack(user_id, new_stack)
            st.success("스택이 성공적으로 업데이트되었습니다.")
        else:
            st.warning("선택한 스택이 없습니다.")

    # 자기소개 수정
    user_profile = get_user_profile(user_id)
    if user_profile:
        new_bio = st.text_area("자기소개를 수정하세요:", value=user_profile['user_bio'])

        if st.button("자기소개 저장"):
            if new_bio.strip():
                update_user_bio(user_id, new_bio)
                st.success("자기소개가 성공적으로 업데이트되었습니다.")
            else:
                st.warning("자기소개가 비어 있습니다.")
    else:
        st.error("사용자 정보를 불러오지 못했습니다.")

    # 업데이트된 사용자 정보를 DB에서 가져오기
    user_profile = get_user_profile(user_id)
    if user_profile:
        st.write(f"**이름**: {user_profile['user_name']}")
        st.write(f"**자기소개**: {user_profile['user_bio']}")

        if not user_profile['user_stack']:
            st.write("사용 가능한 스택: 새로운 스택을 추가해주세요.")
        else:
            st.write("사용 가능한 스택: ")
            st.markdown(user_profile['user_stack'], unsafe_allow_html=True)
    else:
        st.error("사용자 정보를 불러오지 못했습니다.")