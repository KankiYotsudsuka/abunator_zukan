#図鑑のDB pic_bookと連動する
#result.pyのtableを変えた物を作る

import sys
sys.path.append("/abunator_zukan/")
import psycopg2

users = "postgres"
dbnames = "Abunator"
passwords = "postgres"

#データベースにアクセスするための情報(ローカルの場合)
DATABASE_URL= " user=" + users +" dbname=" + dbnames +" password=" + passwords

def get_connection():
#    return psycopg2.connect(DATABASE_URL)

    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")


def resNumber(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select no from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        num = i[0]
        break
    return int(num)

def resName(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select name from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        animals = i[0]
        break
    return str(animals)

def resDealing(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select dealing from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        explanation = i[0]
        break
    return str(explanation)

def resRank(no):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select danger from pic_book where no = " + str(no))
                results = cur.fetchall()
    for i in results:
        rank = i[0]
        break
    return str(rank)

def resNo(name):
    with get_connection() as con:
            with con.cursor() as cur:
                cur.execute("select no from pic_book where name = '" + name +"'")
                results = cur.fetchall()
    for i in results:
        num = i[0]
        break
    return int(num)

def result(no):
    with get_connection() as conn:
        with conn.cursor() as cur:
            #SQL文実行
            cur.execute('select * from pic_book where no = ' + str(no))
            results = cur.fetchall()
    for i in results:
#        no = str(i[0])
        name = str(i[1])
        dealing = str(i[2])
        rank = str(i[3])
        resultList = [no,name,dealing,rank]
        break
    return resultList