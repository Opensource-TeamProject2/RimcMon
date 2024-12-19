import streamlit as st
import sys
import os

# 현재 파일 위치 기준으로 상위 경로를 추가하여 모듈 불러오기
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from Python_Script_Profile.insert_to_db import insert_user_data
from Python_Script_Profile.select_from_db import get_user_data
from Python_Script_Profile.update_user_data import update_user_data

# 세션 초기화 함수
def initialize_session():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False #로그인 여부
    if "user_data" not in st.session_state:
        st.session_state.user_data = None #현재 로그인한 사용자 정보
    if "current_page" not in st.session_state:
        st.session_state.current_page = "login"  # 기본 페이지는 로그인

# 로그인 페이지
def login_page():
    st.title("로그인")
    username = st.text_input("이름", placeholder="사용자의 이름을 입력해주세요")
    password = st.text_input("비밀번호", placeholder="비밀번호를 입력해주세요", type="password")

    if st.button("로그인", key="login_button"):
        if not username or not password:
            st.error("이름과 비밀번호가 입력되지 않았습니다.")
            return

        user_data = get_user_data(username, password)
        if user_data:
            st.session_state.user_data = user_data 
            st.session_state.logged_in = True
            st.session_state.current_page = "profile"
            st.success(f"환영합니다, {user_data['name']}님!")

        else:
            st.error("이름 또는 비밀번호가 일치하지 않습니다.")

    st.write("---")
    st.write("등록된 사용자가 아니신가요?")
    if st.button("신규 사용자 등록",key="signup_button"):
        st.session_state.current_page = "register"
#기술 목록 조회
def get_skills():
    return {
        "개발": {
            "Java": "https://img.shields.io/badge/Java-007396?style=flat-square&logo=Java&logoColor=white",
            "C": "https://img.shields.io/badge/C-A8B9CC?style=flat-square&logo=C&logoColor=white",
            "Python": "https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=Python&logoColor=white",
            "Spring": "https://img.shields.io/badge/Spring-6DB33F?style=flat-square&logo=Spring&logoColor=white",
        },
        "인공지능": {
            "TensorFlow": "https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=TensorFlow&logoColor=white",
            "PyTorch": "https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=PyTorch&logoColor=white",
            "Scikit-Learn": "https://img.shields.io/badge/Scikit%20Learn-F7931E?style=flat-square&logo=Scikit-Learn&logoColor=white",
        },
        "디자인 / 그래픽": {
            "Adobe Photoshop": "https://img.shields.io/badge/Adobe%20Photoshop-31A8FF?style=flat-square&logo=Adobe%20Photoshop&logoColor=white",
            "Adobe Illustrator": "https://img.shields.io/badge/Adobe%20Illustrator-FF9A00?style=flat-square&logo=Adobe%20Illustrator&logoColor=black",
        },
        "커뮤니티 / 영상 편집": {
            "Adobe Premiere": "https://img.shields.io/badge/Adobe%20Premiere-9999FF?style=flat-square&logo=Adobe%20Premiere%20Pro&logoColor=white",
            "Final Cut Pro": "https://img.shields.io/badge/Final%20Cut%20Pro-999999?style=flat-square&logo=Apple&logoColor=white",
        },
    }

# 신규 사용자 등록 페이지
def register_page():
    st.title("신규 사용자 등록")
    name = st.text_input("이름")
    password = st.text_input("비밀번호", type="password")
    bio = st.text_area("자기소개")

    skills = get_skills()  # 기술 목록 가져오기
    selected_skills = []

    st.markdown("### 기술 선택")
    for category, tools in skills.items():
        st.markdown(f"#### {category}")
        for tool, url in tools.items():
            if st.checkbox(tool, key=tool):
                selected_skills.append({"name": tool, "url": url})

    # 선택한 기술 표시
    if selected_skills:
        st.markdown("### 선택된 기술")
        for skill in selected_skills:
            st.markdown(f"![{skill['name']}]({skill['url']})")

    if st.button("등록"):
        if not name or not password or not bio or not selected_skills:
            st.error("모든 필드를 입력해야 합니다.")
            return

        # 특정 name과 password에 해당하는 사용자 확인
        user = get_user_data(name, password)  # 특정 사용자 검색
        if user:
            st.error("중복된 이름과 비밀번호로 인해 등록할 수 없습니다.")
            return

        # 선택한 기술의 이미지 URL을 저장
        selected_tools = [f'<img src="{skill["url"]}" alt="{skill["name"]}" />' for skill in selected_skills]

        new_user_data = {
            "name": name,
            "password": password,
            "bio": bio,
            "tool": selected_tools
        }

        # 사용자 데이터 삽입
        insert_user_data(new_user_data)
        
        st.session_state.user_data = new_user_data  # 새 사용자 데이터 저장
        st.success(f"{name} 사용자가 등록되었습니다!")

        # 등록 후 로그인 페이지로 이동
        st.session_state.current_page = "profile"

    if st.button("로그인 페이지"):
        st.session_state.current_page = "login"

# profile_page 함수 수정
def profile_page(user_data):
    st.title(f"{user_data['name']} 프로필")
    st.sidebar.button("로그아웃", on_click=logout)
    
    # 사용자 정보 출력
    st.text_input("이름", value=user_data["name"], disabled=True)
    st.text_input("비밀번호", value=user_data["password"], disabled=True)  
    st.text_area("자기소개", value=user_data["bio"], disabled=True)
    
    # 사용 기술 출력
    st.markdown("### 사용 기술")
    if user_data["tool"]:
        tools_html = "".join(user_data["tool"])  # 리스트를 문자열로 결합
        st.markdown(tools_html, unsafe_allow_html=True)  # HTML 렌더링
    else:
        st.info("선택된 기술이 없습니다.")
    # 수정하기 버튼
    if st.button("수정하기"):
        st.session_state.current_page = "edit_profile"



# edit_profile_page 함수 수정
def edit_profile_page(user_data):
    st.title(f"{user_data['name']} 프로필 수정")
    bio = st.text_area("자기소개", value=user_data["bio"])
    skills = get_skills()
    selected_skills = []

    # 기술 선택 UI
    st.markdown("### 기술 선택")
    for category, tools in skills.items():
        st.markdown(f"#### {category}")
        for tool, url in tools.items():
            is_checked = any(f'alt="{tool}"' in t for t in user_data["tool"])  # 기존 선택 여부 확인
            if st.checkbox(tool, value=is_checked, key=f"edit_{tool}"):
                selected_skills.append({"name": tool, "url": url})

    # 선택한 기술 미리보기
    if selected_skills:
        st.markdown("### 선택된 기술")
        for skill in selected_skills:
            st.markdown(f"![{skill['name']}]({skill['url']})")

    # 수정 완료 버튼
    if st.button("수정 완료"):
        updated_tools = [f'<img src="{skill["url"]}" alt="{skill["name"]}" />' for skill in selected_skills]
        
        updated_data = {
            "name": user_data["name"],  # 사용자 이름 추가
            "password": user_data["password"],  # 사용자 비밀번호 추가
            "bio": bio,
            "tool": updated_tools  # 수정된 기술 업데이트
        }

        # DB에 데이터 업데이트
        update_user_data(updated_data)

        # 수정 후 상태 갱신
        st.session_state.user_data["bio"] = bio
        st.session_state.user_data["tool"] = updated_tools
        st.session_state.current_page = "profile"

# 로그아웃 함수
def logout():
    st.session_state.clear()
    st.session_state.current_page = "login"

def main():
    # 세션 상태 초기화
    initialize_session()

    # 현재 로그인 상태에 따라 페이지 처리
    if st.session_state.logged_in:
        if st.session_state.current_page == "login":
            st.session_state.current_page = "profile"  # 로그인 상태면 기본 페이지는 프로필

    # 페이지 전환 처리
    if st.session_state.current_page == "login":
        login_page()
    elif st.session_state.current_page == "register":
        register_page()
    elif st.session_state.current_page == "profile":
        profile_page(st.session_state.user_data)
    elif st.session_state.current_page == "edit_profile":
        edit_profile_page(st.session_state.user_data)  # 수정 페이지 처리

# 메인 함수 실행
if __name__ == "__main__":
    main()
