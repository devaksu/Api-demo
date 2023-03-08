import pyodbc
import pandas as pd

SERVER = 'localhost'
DATABASE = 'MyyntiDB'
USER = 'sa'
PWD = 'Password1'

def get_customer_info(customer_id):
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+SERVER+';DATABASE='+DATABASE+';UID='+USER+';PWD='+ PWD)
    df = pd.read_sql_query('Select * from Asiakas where asiakas_id = ?',params=[customer_id], con=cnxn)
    cnxn.close()
    result = df.to_json(force_ascii=False, orient='records', date_format='iso')
    return result
