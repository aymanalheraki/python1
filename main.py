import pandas as pd
import pyodbc
# Replace 'your_file.xlsx' with the path to your Excel file
file_path = 'E:\\ExcelFiles\\1 (10).xlsx'

# Load the Excel file into a Pandas DataFrame
df = pd.read_excel(file_path)
print(df.iloc[2, 1])


server = 'AYMANPC'
database = 'SakhrDB2'
username = 'sa'
password = '#Amsco100'

# Establish a connection to the SQL Server database
connection = pyodbc.connect(
    f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={server};DATABASE={database};UID={username};PWD={password}')


# Create a cursor
cursor = connection.cursor()

# Execute a COUNT query to count the rows in the table
cursor.execute("SELECT COUNT(*) FROM Entry")

# Fetch the row count as a single value
row_count = cursor.fetchone()[0]

# Execute a SELECT query to fetch data from the table
cursor.execute("SELECT * FROM Entry")

# Fetch all rows as a list of tuples
data_rows = cursor.fetchall()

# Process and print the data and row count
# for row in data_rows:
#     print(row)

print(f"Row count: {row_count}")

# Close the cursor and the connection
cursor.close()
connection.close()
