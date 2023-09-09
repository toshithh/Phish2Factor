import mysql.connector
import pandas as pd

class DB_conn:
    def __init__(self) -> None:
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="phish2fact"
        )
        self.id = 1

    def close(self):
        return self.conn.close()
    
    def username(self):
        qry = f"select * from google_user_dtl where machine_id={self.id}"
        res = pd.read_sql_query(qry)
        unm = res["username"][0]
        if unm:
            return unm
        else:
            return 0