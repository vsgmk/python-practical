import pymysql

def get_db_info(name):
    return pymysql.connect(
        host="localhost",
        user="root",
        password="root123",
        database=name
    )

def get_all_info():
    conn = get_db_info("college")
    query = "INSERT INTO vsgmk VALUES (2, 'v', 's')"  # Correct the SQL syntax
    conn_ch = conn.cursor()
    conn_ch.execute(query)
    conn.commit()  # Commit the transaction for INSERT
    print("Data inserted successfully!")
    conn.close()  # Close the connection
get_all_info()

