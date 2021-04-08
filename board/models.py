from django.db import models

from MySQLdb import connect, OperationalError
from MySQLdb.cursors import DictCursor


def findall():
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor(DictCursor)

        # SQL 실행
        sql = '''
          select no,
                 title,
                 contents,
                 hit,
                 date_format(reg_date, "%Y-%m-%d %p %h:%i:%s") as reg_date
            from board
        order by reg_date desc'''
        cursor.execute(sql)

        # 결과 받아오기
        results = cursor.fetchall()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return results

    except OperationalError as e:
        print(f'error: {e}')


def insert(title, contents):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'insert into board value(null, %s, %s, ifnull((select max(g_no) from board), 0) + 1, 1, 0)'
        count = cursor.execute(sql, (title, contents))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def deleteby_no_and_password(no, password):
    try:
        # 연결
        db = conn()

        # cursor 생성
        cursor = db.cursor()

        # SQL 실행
        sql = 'delete from guestbook where no = %s and password = %s'
        count = cursor.execute(sql, (no, password))

        # commit
        db.commit()

        # 자원 정리
        cursor.close()
        db.close()

        # 결과 반환
        return count == 1

    except OperationalError as e:
        print(f'error: {e}')


def conn():
    return connect(
        user='webdb',
        password='webdb',
        host='localhost',
        port=3306,
        db='webdb',
        charset='utf8')