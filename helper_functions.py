import pandas as pd

def table_info(conn,cur):
    '''
    conn: Database connection object
    cur: Database cursor object
    
    Lists tables present in the database and columns associated with each table
    '''
    tables=cur.execute('SELECT name from sqlite_master where type=\'table\';').fetchall()
    
    for x in tables:
        table_name=x[0]
        table=pd.read_sql('SELECT * FROM {} LIMIT 0'.format(table_name),conn)
        print(table_name)
        
        for col in table.columns:
            print('\t'+col)
        print()
    return None