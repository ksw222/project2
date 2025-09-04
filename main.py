from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

import uvicorn
import psycopg2
# PostgreSQL 접속 정보
conn = psycopg2.connect(
    host="localhost",          # 또는 실제 DB 서버 주소
    port="5432",               # 기본 포트
    database="riskqueens",     # 사용할 데이터베이스 이름
    user="postgres",      # 사용자 이름
    password="0000"   # 비밀번호
)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/html", response_class=HTMLResponse)
def html(request: Request):
    cur = conn.cursor()
    sql = """SELECT * FROM financialstatements;"""
        # # 쿼리 실행
    # 임시저장소한테 실행해달라고 요청
    cur.execute(sql)
    data = cur.fetchall()

    # # 변경사항 커밋
    conn.commit()

    return templates.TemplateResponse("test.html", {"request": request, "data": data[0]})

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)