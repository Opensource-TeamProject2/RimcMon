import streamlit as st
import sys
import os
import json

# 필요한 모듈 경로 추가
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + "/../..")

from Python_Script_Profile.select_from_db import get_user_data  # 사용자 데이터 가져오기
from Python_Script_Posts.insert_to_db import insert_post_data
from Python_Script_Posts.select_from_db import get_post_by_id, get_posts_by_category

# 게시글 가져오는 함수
def fetch_posts_by_category(category=None):
    try:
        result = get_posts_by_category(category) if category else get_posts_by_category("전체")
        if isinstance(result, str):
            result = json.loads(result)
        return result
    except Exception as e:
        st.error(f"게시글 불러오기 실패: {e}")
        return []

# 특정 ID로 게시글 조회
def fetch_post_by_id(post_id):
    try:
        result = get_post_by_id(post_id)
        return json.loads(result) if isinstance(result, str) else result
    except Exception as e:
        st.error(f"게시글 조회 실패: {e}")
        return None

# 게시글 등록 함수
def register_post(title, content, author, category):
    try:
        data = {"title": title, "content": content, "author": author, "category": category}
        insert_post_data(data)  # Python 딕셔너리 전달
        return True
    except Exception as e:
        st.error(f"게시글 등록 중 오류 발생: {e}")
        return False

def display_posts_as_cards(posts):
    st.markdown("""
        <style>
            .post-card {
                border: 1px solid #ddd;
                border-radius: 1px;
                margin: 10px 0;
                padding: 10px;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
                display: flex;
                justify-content: space-between;
                align-items: center;
            }
            .post-title {
                font-size: 1.2em;
                font-weight: bold;
                color: #333;
            }
            .post-info {
                font-size: 0.9em;
                color: #666;
            }
        </style>
    """, unsafe_allow_html=True)

    if not posts:
        st.info("등록된 게시물이 없습니다.")
        return

    for post in posts:
        st.markdown(
            f"""
            <div class="post-card">
                <div>
                    <div class="post-title">[{post['id']}] {post['title']}</div>
                    <div class="post-info">작성자: {post['author']}</div>
                </div>
            </div>
            """, unsafe_allow_html=True
        )

        if st.button("상세 보기", key=f"view-{post['id']}"):
            st.session_state.selected_post_id = post['id']
            st.session_state.page = "상세 페이지"
            st.rerun()

# 게시글 등록 페이지
def show_register_page():
    st.title("📝 게시글 등록")

    with st.form("post_form"):
        title = st.text_input("제목")
        content = st.text_area("내용")
        author = st.text_input("작성자")
        category = st.selectbox("카테고리 선택", ["study", "recruit"])
        submitted = st.form_submit_button("등록")

        if submitted:
            if title and content and author:
                success = register_post(title=title, content=content, author=author, category=category)
                if success:
                    st.success("게시글이 등록되었습니다!")
                    st.session_state.page = "메인"
                    st.rerun()
            else:
                st.warning("제목, 내용, 작성자를 모두 입력해주세요.")



# 상세 페이지
def show_detail_page():
    post_id = st.session_state.get("selected_post_id", None)
    if not post_id:
        st.warning("잘못된 접근입니다. 메인 페이지로 돌아갑니다.")
        st.session_state.page = "메인"
        st.rerun()

    post_detail = fetch_post_by_id(post_id)
    if post_detail:
        with st.form("detail_form"):
            st.title(f"📝 {post_detail['title']}")
            st.write(f"**작성자:** {post_detail['author']}")
            st.write("**내용:**")
            st.write(post_detail["content"])
            submitted = st.form_submit_button("전체 게시판으로 돌아가기")

            if submitted:
                st.session_state.page = "메인"
                st.rerun()
    else:
        st.error("해당 게시글을 찾을 수 없습니다.")
        st.session_state.page = "메인"
        st.rerun()

# 메인 페이지
def show_main_page():
    st.title("📋 자유 게시판")
    category = st.selectbox("카테고리", ["study", "recruit"])
    posts = fetch_posts_by_category(category)

    if not posts:
        st.info("선택한 카테고리에 등록된 게시물이 없습니다.")
        return

    search_query = st.text_input(" 🔍 검색창", "")

    filtered_posts = [
        post for post in posts if search_query.lower() in post['title'].lower()
    ] if search_query.strip() else posts

    if filtered_posts:
        display_posts_as_cards(filtered_posts)
    else:
        st.info("검색 결과가 없습니다.")

    if st.button("📝 게시글 등록"):
        st.session_state.page = "게시글 등록"
        st.rerun()

# 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "메인"
if "selected_post_id" not in st.session_state:
    st.session_state.selected_post_id = None

# 메인 로직
if st.session_state.page == "메인":
    show_main_page()
elif st.session_state.page == "게시글 등록":
    show_register_page()
elif st.session_state.page == "상세 페이지":
    show_detail_page()