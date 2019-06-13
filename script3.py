import sqlite3
# import curses


# Create and connect to a table named 'store' and reference using a cursor object
# No row with auto increment primary key for now
def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()
    conn.close()


# Function to iterate table adding data to the rows
def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    # Use ? to avoid SQL injection in real world DB
    cur.execute("INSERT INTO  store VALUES (?,?,?)", (item, quantity, price))
    conn.commit()
    conn.close()


# Function to delete rows
def delete_data(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?", (item,))
    # Ensure the comma after 'item' is in place
    conn.commit()
    conn.close()


# Function to update data
def update_data(quantity, price, item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (quantity, price, item))
    # In update, there is no need for a comma after 'item'
    conn.commit()
    conn.close()


# Function to display the data stored
def view_data():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    # Store the data in a variable
    rows = cur.fetchall()
    conn.close()
    return rows


update_data(3, 750, 'Flash Disk')
# delete_data("Hard disk")
print(view_data())
# Operation to insert data using multiple lines of SQL code
# insert_data('Flash Disk', 7, 800.0)
