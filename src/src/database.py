import sqlite3
import pandas as pd

def save_to_db(df, table_name):
    conn = sqlite3.connect("data/stocks.db")
    df.to_sql(table_name, conn, if_exists="replace", index=True)
    conn.close()

def read_from_db(table_name):
    conn = sqlite3.connect("data/stocks.db")
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    conn.close()
    return df
