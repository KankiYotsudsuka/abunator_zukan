import pytest
import psycopg2
import random
import pic_book

def get_connection():
    return psycopg2.connect(host="abunator.postgres.database.azure.com",database="Abunator",user="teamD@abunator",port=5432, password="Nagato1109")

def test_Zukan():
    no = random.randint(1,40)
    name = pic_book.resName(no)
    number = pic_book.resNo(name)
    assert no == number