import sqlite3

conn = sqlite3.connect('contacts.sqlite')

name = input("Please enter your name: ")
#searching for rows that contain a specific name
for row in conn.execute("SELECT DISTINCT * FROM contacts WHERE name LIKE ?", (f'%{name}%',)):
    print(row)

#how should I know the details of tables to inject attack

# for row in conn.execute("SELECT DISTINCT * FROM sqlite_master"):
#     print(row)

conn.close()