import psycopg2

# PostgreSQL 접속 정보
conn = psycopg2.connect(
    host="localhost",          # 또는 실제 DB 서버 주소
    port="5432",               # 기본 포트
    database="riskqueens",     # 사용할 데이터베이스 이름
    user="ubuntu",      # 사용자 이름
    password="0000"   # 비밀번호
)

# 커서 생성
cur = conn.cursor()
# sql = """INSERT INTO financialstatements (
#     CompanyID, companyname, currentassets, revenue, operatingincome, totalliabilities, totalequity
# ) VALUES
# ('1', 'Alpha Corp', 150000, 500000, 120000, 200000, 300000),
# ('2', 'Beta Ltd', 80000, 250000, 60000, 100000, 180000),
# ('3', 'Gamma Inc', 200000, 750000, 250000, 300000, 450000),
# ('4', 'Delta Co', 120000, 400000, 90000, 150000, 270000),
# ('5', 'Epsilon LLC', 175000, 600000, 200000, 250000, 350000);"""
sql = """SELECT * FROM financialstatements;"""


# # 쿼리 실행
# 임시저장소한테 실행해달라고 요청
cur.execute(sql)
print(cur.fetchall())

# # 변경사항 커밋
conn.commit()

# # 연결 종료
cur.close()
conn.close()
