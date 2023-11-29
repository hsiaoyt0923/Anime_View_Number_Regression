import requests
import psycopg2
import password as pw



if __name__ == '__main__':
    conn = psycopg2.connect(database=pw.DATABASE,
                            user=pw.USER,
                            password=pw.PASSWORD,
                            host=pw.HOST,
                            port=pw.PORT)
