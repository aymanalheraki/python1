import pymysql

# Replace these with your database credentials
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "sakila"
}

# Establish a connection
connection = pymysql.connect(host = "localhost",
user = "root",
password = "123456",
database = "sakila")

# Create a cursor
cursor = connection.cursor()

# Now you can execute SQL queries using the cursor
cursor.execute("SELECT * FROM film")

# Fetch and print results
for row in cursor.fetchone():
    print(row)

# Close the cursor and connection when done
cursor.close()
connection.close()
