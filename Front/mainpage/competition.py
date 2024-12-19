import streamlit as st
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__) + '/../..')))
from Python_Script.select_from_db import get_mysql_data

# 데이터 초기화
data = get_mysql_data()

# CSS 스타일 정의
def apply_custom_css():
    st.markdown(
        """
        <style>
        /* 전체 페이지 중앙 정렬 */
        .main {
            display: flex;
            justify-content: center;
        }
        /* 포스터 이미지를 중앙 정렬 */
        .center-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
        }
        /* 제목 글씨 크기 조정 */
        .small-title {
            font-size: 18px;  /* 글씨 크기 설정 */
            font-weight: bold;
            margin-bottom: 10px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

# 페이지 세그먼트 함수 정의
def display_posters(data):
    if data:
        # 두 개의 열 생성
        col1, col2 = st.columns(2)

        for idx, row in enumerate(data):
            # 짝수 인덱스는 왼쪽 열(col1), 홀수 인덱스는 오른쪽 열(col2)에 배치
            with col1 if idx % 2 == 0 else col2:
                # 제목 표시 (글씨 크기 작게 조정)
                st.markdown(f"<div class='small-title'>{row['title']}</div>", unsafe_allow_html=True)

                # 탭 생성
                create_tab, alter_tab, drop_tab = st.tabs(["포스터", "날짜", "댓글"])

                # 포스터 탭
                with create_tab:
                    st.image(
                        row["image"],
                        caption=row["title"],
                        use_container_width=True  # 이미지 컨테이너 너비에 맞춤
                    )

                # 날짜 탭
                with alter_tab:
                    st.write(f"날짜: {row['date']}")

                # 댓글 탭
                with drop_tab:
                    st.write("댓글 기능 준비 중...")

                st.divider()  # 포스터 간 구분선
    else:
        st.write("데이터가 없습니다.")

# Streamlit 앱 실행
if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
    st.rerun()
apply_custom_css()
display_posters(data)