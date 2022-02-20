import sqlite3

def create_table(table_name, fields):
    conn = sqlite3.connect('../../static/database/test.db')
    begin = "CREATE TABLE IF NOT EXISTS " + table_name
    conn.execute(begin+fields)
    print("Created Table")

    conn.execute("INSERT INTO company (id,name,age,address,salary) VALUES (1, 'Paul', 32, 'California', 20000.00 )");
    conn.execute("INSERT INTO company (id,name,age,address,salary) VALUES (2, 'Paul', 32, 'California', 20000.00 )");
    conn.execute("INSERT INTO company (id,name,age,address,salary) VALUES (3, 'Allen', 25, 'Texas', 15000.00 )");
    conn.execute("INSERT INTO company (id,name,age,address,salary) VALUES (4, 'Teddy', 23, 'Norway', 20000.00 )");
    conn.execute("INSERT INTO company (id,name,age,address,salary) VALUES (5, 'Mark', 25, 'Rich-Mond ', 65000.00 )");

    conn.commit()
    print("Records created successfully")
    conn.close()

def drop_table(table_name):
    conn = sqlite3.connect('../../static/database/test.db')
    conn.execute('DROP TABLE '+table_name)
    conn.commit()
    conn.close()

    return None

def query_table(query):
    conn = sqlite3.connect('../../static/database/test.db')
    results = conn.execute(query)
    return results

drop_table(table_name="company")
create_table(table_name="company",fields="""( id integer PRIMARY KEY,name text NOT NULL,age integer NOT NULL,address text NOT NULL,salary integer NOT NULL )""")
data = query_table(query="SELECT * FROM company")

for result in data:
    print(result)