# EKS <-> ECR <->  ArgoCD 구축
https://sungbin-park.tistory.com/122

# 좋은 Pytest 링크
https://sangjuncha-dev.github.io/posts/programming/python/2022-02-08-python-pytest-guide/

# 🚀 Pytest 실습 Repository

이 저장소는 `pytest`를 활용한 자동화 테스트를 연습하기 위한 프로젝트입니다.  
API 테스트, 유닛 테스트, 예외 처리, 로깅, CI/CD 연동 등을 포함합니다.  
추후 AWS 와 연동하여 해보기

```bash
git clone -b main https://github.com/rookieboba/pytest/
```

---

## 📌 프로젝트 개요

✅ `pytest`를 활용하여 다양한 테스트 케이스 작성  
✅ API, 파일 처리, 계산기 등 다양한 기능 테스트  
✅ `pytest.ini` 설정을 통한 자동화 테스트 최적화  
✅ GitHub Actions를 활용한 CI/CD 테스트 자동화  

---

## 🛠️ 개발 환경

| 도구 | 버전 확인 방법 | 사용 버전 |
|------|------|------|
| **Python** | `python --version` | `Python 3.11.9` |
| **Git** | `git --version` | `git 2.49.1` |
| **pytest** | `pytest --version` | `pytest 7.4.2` |

---

## 📂 프로젝트 폴더 구조

```
pytest-project/
│── src/                 # 개발 코드 (테스트 대상)
│── tests/               #  Pytest 테스트 코드
│── .github/             # GitHub Actions 설정
│── .gitignore           # Git에 올리지 않을 파일 설정
│── pytest.ini           # pytest 설정 파일
│── requirements.txt     # Python 패키지 목록
│── README.md            # 프로젝트 설명 파일ttt#
```

---

## 📦 1️⃣ 프로젝트 설치 방법

📌 **필요한 패키지 설치**

```bash
pip install -r requirements.txt
```

📌 **설치된 `pytest` 버전 확인**

```bash
pytest --version
```

---

## 🚀 2️⃣ 테스트 실행 방법

📌 **모든 테스트 실행**

```bash
pytest
```

📌 **특정 파일 테스트 실행**

```bash
pytest tests/test_api.py
```

📌 **특정 테스트 함수 실행**

```bash
pytest tests/test_auth.py::test_login_success
```

📌 **로그 출력 테스트 실행**

```bash
pytest -s tests/test_calc.py
```

📌 **테스트 커버리지 확인**

```bash
pytest --cov=src
```

---

## 🐳 3️⃣ Docker 환경에서 실행 (선택)

📌 **Docker 컨테이너에서 `pytest` 실행**

```bash
docker build -t pytest-container .
docker run --rm pytest-container
```

📌 **Docker Compose 사용 (선택)**

```bash
docker-compose up --build
```

---

## 🔧 4️⃣ GitHub Actions (CI/CD) 연동

📌 **`.github/workflows/pytest.yml` 설정 예시**

```yaml
name: Pytest CI

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: 코드 체크아웃
        uses: actions/checkout@v3

      - name: Python 설치
        uses: actions/setup-python@v3
        with:
          python-version: "3.11"

      - name: 의존성 설치
        run: pip install -r requirements.txt

      - name: Pytest 실행
        run: pytest --cov=src
```

📌 **GitHub Actions 실행 확인**  
- GitHub에서 **Actions 탭**에서 실행 내역 확인 가능  

---

## ✅ 마무리
참고)
https://docs.pytest.org/en/stable/how-to/usage.html
