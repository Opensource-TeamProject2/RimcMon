import streamlit as st
import sys
import os
import importlib

# 프로젝트 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/..")
st.snow()
# 초기 상태 설정
if "page" not in st.session_state:
    st.session_state["page"] = "main"

# 동적으로 모듈 불러오는 함수
def load_module(module_name, func_name):
    try:
        module = importlib.import_module(module_name)
        func = getattr(module, func_name)
        return func
    except (ImportError, AttributeError) as e:
        st.error(f"모듈 {module_name} 또는 함수 {func_name}을(를) 불러오는 데 실패했습니다: {e}")
        return None

# 사이드바 메뉴
with st.sidebar:
    if st.button("로그인", key="go_to_login"):
        st.session_state["page"] = "user_login"
    if st.button("회원가입", key="go_to_register"):
        st.session_state["page"] = "user_register"
    if st.button("공모전", key="go_to_competition"):
        st.session_state["page"] = "competition"
    if st.button("게시판 바로가기", key="go_to_post"):
        st.session_state["page"] = "post"

# 현재 페이지 가져오기
page = st.session_state["page"]

# 메인 페이지
if page == "main":
    st.image("../img/림크몬.png", use_container_width=True)
    _, exp_col, _ = st.columns([1, 5, 1])
    with exp_col:
        with st.expander("📖 림크몬 소개"):
            st.markdown("""
                대학생을 위한 리크루팅 서비스 림크몬
            """)
            st.info("""
                대학생을 위한 프로젝트 / 공모전 등의 매칭 서비스를 제공하는 림크몬 👾 개발 저장소입니다.
                림크몬은 대학생이 자신의 관심사와 전공 등 역량에 맞는 활동에 참여할 수 있도록 돕는 매칭 서비스입니다.
                다양한 활동을 통해 자신의 역량을 성장시키고, 새로운 기회를 발견하는 것을 목표로 합니다.
            """)

# 사용자 로그인 페이지
elif page == "user_login":
    login_page_func = load_module("profilepage.user", "login_page")
    if login_page_func:
        login_page_func()

# 사용자 회원가입 페이지
elif page == "user_register":
    register_page_func = load_module("profilepage.user", "register_page")
    if register_page_func:
        register_page_func()

# 공모전 페이지
elif page == "competition":
    competition_page_func = load_module("mainpage.competition", "show_competition_page")
    if competition_page_func:
        competition_page_func()

# 게시판 메인 페이지
elif page == "post":
    post_main_func = load_module("mainpage.post", "show_main_page")
    if post_main_func:
        post_main_func()

# 게시판 상세 페이지
elif page == "상세 페이지":
    post_detail_func = load_module("mainpage.post", "show_detail_page")
    if post_detail_func:
        post_detail_func()
        if st.button("전체 게시판으로 돌아가기"):
            st.session_state["page"] = "post"
            st.rerun()

# 게시글 등록 페이지
elif page == "게시글 등록":
    post_register_func = load_module("mainpage.post", "show_register_page")
    if post_register_func:
        post_register_func()
        if st.button("전체 게시판으로 돌아가기", key="go_to_main2"):
            st.session_state["page"] = "post"
            st.rerun()