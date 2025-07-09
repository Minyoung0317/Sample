from fastapi import FastAPI
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.get("/", response_class=PlainTextResponse)
def read_root():
    return "auth-service"

# 아래와 같이 실행하세요:
# uvicorn gateway.app.main:app --host 0.0.0.0 --port 8081 --reload 