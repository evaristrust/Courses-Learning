import sqlite3

db = sqlite3.connect('contacts.sqlite')

db.execute("CREATE TABLE IF NOT EXISTS contacts(NAME TEXT, PHONE INT, EMAIL TEXT)")
db.execute("INSERT INTO contacts(NAME, PHONE, EMAIL) VALUES('Big Man', 087894, 'big@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Tiny Man', 085343, 'tiny@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Shy Man', 0234234, 'shy@gmail.com')")
db.execute("INSERT INTO contacts VALUES('Bad Man', 2502321, 'bado@gmail.com')")

#Querying my database by executing queries using cursor
cursor = db.cursor()
cursor.execute("SELECT DISTINCT * FROM contacts")

# print(cursor.fetchall()) # returns  a list of rows.. allowing moving back and forth through rows.
# print(cursor.fetchone()) # This is quite useful... returns list in a style
# for row in cursor:
#     print(row)

for name, phone, email in cursor:
    print(name)
    print(phone)
    print(email)
    print("-" * 20)

cursor.close()

db.commit() # This will save the data well and can be reached in contacts2
db.close()