import psycopg2


# Create and connect to a table named 'store' and reference using a cursor object
# No row with auto increment primary key for now
def create_table():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='aslan' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


# Function to iterate table adding data to the rows
def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='aslan' host='localhost' port='5432'")
    cur = conn.cursor()
    # Use ? to avoid SQL injection in real world DB
    cur.execute("INSERT INTO  store VALUES (%s,%s,%s)", (item, quantity, price))
    conn.commit()
    conn.close()


# Function to delete rows
def delete_data(item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='aslan' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s", (item,))
    # Ensure the comma after 'item' is in place
    conn.commit()
    conn.close()


# Function to update data
def update_data(quantity, price, item):
    conn = psycopg2.connect("dbname='database1' user='postgres' password='aslan' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (quantity, price, item))
    # In update, there is no need for a comma after 'item'
    conn.commit()
    conn.close()


# Function to display the data stored
def view_data():
    conn = psycopg2.connect("dbname='database1' user='postgres' password='aslan' host='localhost' port='5432'")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # Store the data in a variable
    rows = cur.fetchall()
    conn.close()
    return rows


create_table()
# insert_data('Cover', 10, 300)
update_data(3, 750, 'Screen')
# delete_data("Cover")
print(view_data())
# Operation to insert data using multiple lines of SQL code
# insert_data('Flash Disk', 7, 800.0)
