# nbc_personal_project3
스파르타코딩클럽 내일배움캠프 personal project3 todo list with drf


## 1. 소개
- poetry를 사용해 의존성 관리

  ```
  # 패키지 설치
  poetry install
  
  # 가상환경 실행
  poetry shell
  
  # 추가 패키지 설치 시
  poetry add 패키지 이름
  
  # 서버 실행시키기
  poetry run python manage.py runserver
  ```
  
- `secrets.json`을 통해 secret key를 관리하기 때문에 반드시 `secrets.json` 파일을 생성해서 key를 넣어줄 것.
  ```json
  // secrets.json
  
  {
      "SECRET_KEY": "내 시크릿 키"
  }
  ```
  
## 2. users

- jwt 기반의 토큰 인증 체제. 토큰 만료 시간 60분

  수정 시
  ```python
  # settings.py
  
  SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=원하는 시간 숫자로),
    ...
  }
  ```
  
- 회원 가입, 로그인, 유저 프로필 열람, 수정, 삭제 기능 구현 완료

## 3. todos

- todo 열람, todo 상세 확인, 수정, 삭제 기능 구현 완료

- 기본적으로 자신이 작성한 todo만 열람 가능, 수정, 삭제 가능
