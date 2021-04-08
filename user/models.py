# 크게 함수가 2개 있음

from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor

def findbyno():
    sql = 'select no, name, email, gender from user where no = %s'
    pass

def findby_email_and_password(email, password): # app 에다가 주는 것
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)  # cursor: 쿼리 날려주는 것

        # SQL 실행
        sql = 'select no, name from user where email=%s and password = %s'
        cursor.execute(sql, (email, password))

        # 결과 받아오기
        result = cursor.fetchone()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return result

    except OperationalError as e:
        print(f'error: {e}')

def insert(name, email, password, gender): # app 에서 가져오는 것
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()  # cursor: 쿼리 날려주는 것

        # SQL 실행
        sql = 'insert into user values(null, %s, %s, %s, %s, now())'
        count = cursor.execute(sql, (name, email, password, gender))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def update(email):
    pass


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')