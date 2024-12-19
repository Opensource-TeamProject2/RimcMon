# 🏫 대학생을 위한 리크루팅 서비스 , 림크몬 👾
대학생을 위한 프로젝트 / 공모전 등의 매칭 서비스를 제공하는 림크몬 👾 개발 저장소입니다. <br> 
림크몬은 대학생이 자신의 관심사와 전공 등 역량에 맞는 활동에 참여할 수 있도록 돕는 매칭 서비스입니다.<br> 
다양한 활동을 통해 자신의 역량을 성장시키고, 새로운 기회를 발견하는 것을 목표로 합니다.<br>
## 👋🏻 Introduction
### 🧑🏻‍💻 Developers 

| [<img src="https://avatars.githubusercontent.com/bum0w0" width="100px;" alt="bum0w0"/>](https://github.com/bum0w0) | [<img src="https://avatars.githubusercontent.com/chanyoung1256" width="100px;" alt="chanyoung1256"/>](https://github.com/chanyoung1256) | [<img src="https://avatars.githubusercontent.com/sanchaehwa" width="100px;" alt="sanchaehwa"/>](https://github.com/sanchaehwa) | [<img src="https://avatars.githubusercontent.com/krdevdory" width="100px;" alt="krdevdory"/>](https://github.com/krdevdory) |
|:---------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|:------------------------------------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------------------------:|
| **김진범**                                                                                                      | **김찬영**                                                                                                       | **양화영**                                                                                                         | **안봉근**                                                                                                       |


 ### 👾 림크몬 기능 소개
 #### 1️⃣ **정보 공유 기능** <br><br>
<img src="https://github.com/user-attachments/assets/78839362-d0f8-402f-9f42-509c02a42147" width="70%"> <br>

현재 신청 및 모집이 진행 중인 공모전, 스터디, 동아리 모집 정보를 각 게시판을 통해 확인할 수 있으며, 이를 통해 관련 정보를 손쉽게 
얻을 수 있다는 장점이 있습니다. <br>
또한, 이러한 기능을 활용해 다양한 정보를 공유해 나갈 수 있습니다.

 #### 2️⃣ **프로필 등록 기능** <br><br>
![프로필](https://github.com/user-attachments/assets/3d667dab-0a2e-4f87-81c7-19a9c41e6ff7)<br>
자신을 PR할 수 있는 프로필을 등록할 수 있는 기능으로, 대학생이 자주 사용하는 기술 목록을 제공하여 <br>
자신이 사용 가능한 기술을 프로필에 등록해 나갈 수 있습니다.

 #### 3️⃣ **네트워킹 기능** <br><br>
<img src="https://github.com/user-attachments/assets/686d9a0b-1f0e-4cf0-80ff-52f780976b77" width="70%"> <br>
자유게시판을 통해,  동아리 모집 , 프로젝트 팀원 모집과 같이 네트워킹이 가능합니다. 이러한 기능을 통해 프로젝트 또는 동아리에 
참여할 수도 모집할 수도 있습니다


 #### 3️⃣ **관리자 페이지** <br><br>
![관리자페이지](https://github.com/user-attachments/assets/d3141ebc-f555-472f-b030-6d005d259c15)<br>

관리자는 관리자 페이지를 통해 데이터베이스에 등록된 정보를 효율적으로 조회, 수정, 삭제할 수 있습니다.

## 👥 Cooperation
###  💭 Message Format
 | Message Type      | Description          | Example               |
|:----------------:|:--------------------:|:---------------------:|
| Issue          | 이슈 작성시,이슈 메시지에 <수정사항> 작성후, 수정사항에 대해 간단히 작성 | `<수정사항> README.md 수정` |
| Commit        | 이슈번호 + [키워드] + 수정사항| `#1 [Docs] README.md 수정`   |
| PullRequest  | 이슈번호 + [키워드] + 수정사항   | `#1 [Docs] README.md 수정`|

### 🔑 Keyword Type
|태그 이름|태그 설명|
|:---:|:---:|
|✨ Feat|새로운 기능 추가|
|🐛 Fix|버그 수정|
|🚑 HOTFIX|치명적 버그 수정|
|📁 Build|빌드 관련 파일 수정|
|🎨 Design|CSS를 포함 UI 디자인 변경|
|📄 Docs|문서(문서 추가, 수정, 삭제)|
|📝 Test|테스트(테스트 코드 추가, 수정, 삭제: 비즈니스 로직에 변경 없는 경우)|
|♻️ Rename|파일, 폴더명 이름 수정|
|🔥 Remove|파일, 폴더 삭제|

### 🎋 Branch Convention
#### Branch Structure 
- **main**: 배포용 브랜치 (항상 안정적인 상태 유지)
- **develop**: 통합 개발 브랜치 (다음 배포를 준비)
- **feature/**: 기능 개발 및 이슈 해결 브랜치 (작업 단위)
#### Branch Flow
 ```
Main Branch
  ▲
  └── Develop Branch ── 테스트 완료 후 병합 
                              ▲
                              └── Feature Branch ── 작업 완료 후 병합 
                                          └── 새로운 기능 추가

 ```
#### RuleSet
1. Reviewer가(2명 이상) PR을 승인할 시에, PR Merge 가능
2. PR에 새로운 commit 추가 시, 이전의 PR 승인을 무효화하고 재검토

## ✨ Development
 
### ⚒️ Project Tech Stack 
| **Category**          | **Technologies**                                                                                                                                                                |
|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Backend**           | ![php](https://img.shields.io/badge/php-777BB4?style=flat-square&logo=php&logoColor=white) ![mysql](https://img.shields.io/badge/mysql-4479A1?style=flat-square&logo=mysql&logoColor=white) ![python](https://img.shields.io/badge/python-3776AB?style=flat-square&logo=python&logoColor=white)|
| **Frontend & Communication** | ![streamlit](https://img.shields.io/badge/streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white) ![Figma](https://img.shields.io/badge/figma-F24E1E?style=flat-square&logo=figma&logoColor=white)|

### 📁 File Structure
 ```
RIMCMON
├── Crawling/ #데이터 크롤링 관련
├── Front/ #프론트엔드 코드 관련
│   ├── img/ # 이미지 자원
│   ├── mainpage/ # 메인 페이지 - 공모전, 스터디, 동아리, 팀원 모집, 자유 게시판
│   ├── manage/ # 관리자 페이지 - 공모전 정보, 유저 정보, 데이터 관리
│   └── profilepage/ # 프로필 페이지 - 로그인, 사용자 등록, 프로필 수정
├── PHP_Script/ # mainpage PHP Server 관련
├── PHP_Script_Manage/ # manage PHP Server 관련
├── PHP_Script_Profile/ # profilepage PHP Server 관련
├── Python_Script/ # mainpage DB 관련
├── Python_Script/ # manage DB 관련
├── Python_Script_Profile/ # profilepage DB 관련
├── TEST/ # 렌더링 테스트
├── venv/ # 가상환경
├── .gitignore
├── README.md
└── requirements.txt
 ```
### ⚙️ Project preferences
-  ```Python3 -m venv venv ``` 가상환경을 Local에서 생성해주세요 *가상환경 진입후 
- ``` pip install -r requirements.txt``` 림크몬 프로젝트에 필요한 라이브러리를 읽어와주세요