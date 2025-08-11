import sqlite3 

# connect to sqlite 
connection = sqlite3.connect("student.db")

# create a cursor object
cursor = connection.cursor()

# create table (fixed VARCHAR9 -> VARCHAR)
table_info = """
CREATE TABLE STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
)
"""
cursor.execute(table_info)

# Sample dataset
students = [
    ("Alice Johnson", "10", "A", 85),
    ("Brian Smith", "10", "B", 78),
    ("Charlie Lee", "9", "A", 92),
    ("Diana King", "9", "C", 67),
    ("Ethan Brown", "11", "B", 88),
    ("Fiona Davis", "11", "A", 95),
    ("George White", "12", "C", 73),
    ("Hannah Black", "12", "B", 81),
    ("Ian Green", "10", "A", 89),
    ("Jane Adams", "9", "B", 76),
]

# Use ? placeholders in SQLite
cursor.executemany(
    "INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES (?, ?, ?, ?)",
    students
)

# commit changes
connection.commit()

# display all the records 
print("The inserted Records are:")
data = cursor.execute("SELECT * FROM STUDENT")
for row in data:
    print(row)

# close connection
connection.close()
