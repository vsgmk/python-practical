import pymysql

def get_db_info(name):
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database=name
    )


def get_all_info():

    conn=get_db_info("college")
    query="select * from vsgmk"
    conn_ch=conn.cursor()
    conn_ch.execute(query)
    result=conn_ch.fetchall()
    print(result)
get_all_info()

