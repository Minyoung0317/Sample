# 1. Python 베이스 이미지 사용
FROM python:3.10-slim

# 2. 작업 디렉토리 생성 및 설정
WORKDIR /app

# 3. 현재 디렉토리의 모든 파일을 컨테이너의 /app으로 복사
COPY . /app

# 4. 필요 패키지 설치 (FastAPI, Uvicorn)
RUN pip install --no-cache-dir fastapi uvicorn

# 5. 컨테이너가 8081 포트를 사용하도록 지정
EXPOSE 8081

# 6. 컨테이너 시작 시 FastAPI 앱 실행
CMD ["uvicorn", "gateway.app.main:app", "--host", "0.0.0.0", "--port", "8081"]
