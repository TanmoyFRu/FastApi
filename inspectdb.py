import sqlite3

def check_tables_and_dates(db_name: str):
  
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    for table in tables:
        table_name = table[0]
        
  
        cursor.execute(f"SELECT sql FROM sqlite_master WHERE name='{table_name}';")
        create_table_statement = cursor.fetchone()
       
        if create_table_statement:
            print(f"Table: {table_name}")
            print(f"Creation SQL: {create_table_statement[0]}")
            
        
            cursor.execute(f"SELECT * FROM {table_name};")
            rows = cursor.fetchall()
            
            if rows:
                print(f"Data in {table_name}:")
                for row in rows:
                    print(row)
            else:
                print(f"No data found in {table_name}.")
            
            print("-" * 40)

    conn.close()

if __name__ == "__main__":
 
    db_name = 'blog.db'
    check_tables_and_dates(db_name)