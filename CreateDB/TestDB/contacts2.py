import sqlite3

db = sqlite3.connect('contacts.sqlite')

update_sql = "UPDATE contacts SET email = 'newmail@gmail.com' WHERE phone = 0234234"
update_cursor = db.cursor()
update_cursor.execute(update_sql)
print("{} rows updated".format(update_cursor.rowcount)) # counting how many rows has been updated

print("Are connection the same: {}".format(update_cursor.connection == db)) # check if stored connections are ==
print("_" * 20)

update_cursor.connection.commit() #connection property highly recommended to commit
                                  # this commit will update the data in contacts3
                                  #commit when you are happy with the changes
update_cursor.close()

for row in db.execute("SELECT DISTINCT * FROM contacts ORDER BY name"): # without using cursor
    print(row)

db.close()