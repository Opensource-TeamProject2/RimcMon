import streamlit as st

# 스타일 적용
st.markdown(
    """
    <style>
    body {
        background-color: #f8f9fa; /* 배경 색 */
    }
    .title {
        color: #007BFF; /* 제목 색상 */
        font-size: 2.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
    }
    .stButton>button {
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 10px;
        font-size: 16px;
        width: 200px; /* 고정 너비 */
        height: 50px; /* 고정 높이 */
        margin: 10px auto; /* 버튼 간격 및 중앙 정렬 */
        display: block; /* 중앙 정렬 */
    }
    .stButton>button:hover {
        background-color: #0056b3; /* 호버 색상 */
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 페이지 제목 및 설명
st.markdown('<div class="title">팀원 모집</div>', unsafe_allow_html=True)


# 팀 정보 섹션
st.write("### 팀 정보")
team_name = st.text_input("팀 이름", placeholder="예: 람크몬 개발자")
project_description = st.text_area("공모전 주제 및 설명", placeholder="팀의 목표와 공모전 주제를 입력하세요.")
requirements = st.text_area("팀원 모집 조건", placeholder="필요 기술, 역할 등 상세 조건을 적어주세요.")

# 모집 역할 섹션
st.write("### 모집 역할")
roles = st.multiselect(
    "필요한 역할 선택",
    ["디자이너", "개발자", "기획자", "마케터", "데이터 분석가", "기타"],
    default=None
)
additional_role = st.text_input("기타 필요한 역할", placeholder="기타 역할을 적어주세요.")

# 팀원 신청 양식 섹션
st.write("### 팀원 신청")
st.text_input("이름", placeholder="지원자의 이름을 입력하세요.")
st.text_input("이메일", placeholder="연락 가능한 이메일을 입력하세요.")
st.text_area("자기소개 및 지원 동기", placeholder="자신의 강점과 참여 의지를 적어주세요.")

# 제출 버튼
if st.button("제출"):
    st.success("신청이 성공적으로 제출되었습니다!")

if st.button("메인으로 돌아가기"):
    st.session_state["page"] = "main"
    st.rerun()
