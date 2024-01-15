import sqlite3

connection = sqlite3.connect('employer.db')

#create cursor to insert, update, and retrive employee
cursor = connection.cursor()

#create table
table_info = """
create table EMPLOYEE(NAME VARCHAR(255), JOB VARCHAR(255), YOE INT, SALARY INT);
"""

cursor.execute(table_info)

# Inserting 10 records into the EMPLOYEE table
records_to_insert = [
    ('Sunil Giri', 'Analyst', 5, 70000),
    ('Jane Smith', 'Developer', 3, 60000),
    ('Bob Johnson', 'Manager', 2, 55000),
    ('Alice Williams', 'Designer', 4, 65000),
    ('Charlie Brown', 'Engineer', 6, 75000),
    ('Eva Davis', 'Tester', 1, 50000),
    ('Frank Wilson', 'Administrator', 8, 80000),
    ('Grace Miller', 'Consultant', 7, 75000),
    ('Henry Taylor', 'Programmer', 4, 65000),
    ('Ivy Martin', 'Support', 2, 55000)
]

# Inserting records into the EMPLOYEE table
for record in records_to_insert:
    cursor.execute("INSERT INTO EMPLOYEE VALUES (?, ?, ?, ?)", record)

print("Inserted records are")

data = cursor.execute('''select * from EMPLOYEE''')

for row in data:
    print(row)

# Commit the changes to the database
connection.commit()
connection.close()