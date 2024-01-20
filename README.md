# Piro20_CardGame_4

## 협업

- 사용한 툴

| 협업툴 | 기능 | 링크 |
| --- | --- | --- |
| 깃허브 | 이슈, pr 기능 활용, pr approve로 브랜치 보호 | https://github.com/Pirogramming-20/Piro20_CardGame_4/issues |
| 노션 | 칸반 보드를 활용한 업무 분배 | 피로그래밍 카드게임 (https://www.notion.so/5c4922bff16647a5bdd16587ceb84be5?pvs=21)  |
| 피그마 | 디자인 협업 | https://www.figma.com/file/FR0uwTUWRLaeVqnywBnaH7/piro20-(Copy)?type=design&node-id=0%3A1&mode=design&t=7BQ1FQzUqAT70Gv0-1 |
| ERD Clound | DB 협업 | https://www.erdcloud.com/d/EnWxjrDyoWoPaTZhK |

## 구현 내용

- 구조
    - Game 앱
        - Game 모델 저장
        - 카드 게임 룰, 게임 생성 및 삭제, 게임 진행 등을 담당
    - Common 앱
        - User 모델 저장 (Abstract User 상속)
        - 로그인, 로그아웃, 회원가입, 소셜로그인 등을 담당
- 로그인/로그아웃/회원가입
    - 장고 내부 로그인, 로그아웃, 회원가입 구현
    - 소셜 로그인, 회원가입 (최초 로그인 시 자동으로 회원가입) 구현
        - 구글, 깃허브, 네이버, 카카오 구현
        - 로그인 버튼 클릭 시 소셜 로그인 화면으로 즉시 이동 (GET 접근 허용)
- 게임 생성(공격하기) 및 반격하기
    - 공격 Form, 반격 Form을 따로 구현
    - 생성자를 사용하여 랜덤 숫자 선택 기능 구현
- 전적 페이지
    - 현재 사용자가 관여된 게임을 불러오도록 구현
    - 게임 수락 여부에 따라 다르게 구현
    - 전적이 많아지면 스크롤 내려가도록 구현
- 게임 상세 페이지
    - 진행 중인 게임과 끝난 게임을 따로 구현
    - 게임에 참여하는 두 유저의 정보를 가져와 결과에 따라 출력
        - 게임 결과, 승부 요청, 승부수락
- 게임 삭제
    - 게임취소를 누르면 request와 pk를 받아서 삭제 구현
- 랭킹 기능
    - 1~3순위만 보이도록 구현
- 사이트 디자인
    - 피그마 협업 툴 사용