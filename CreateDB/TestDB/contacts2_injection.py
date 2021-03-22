import sqlite3

db = sqlite3.connect('contacts.sqlite')

new_email = input("Enter your new email: ")
new_phone = input("Please enter your phone: ") # B.C: Here's where sql injection attack can occur

# update_sql = "UPDATE contacts SET email = '{}' WHERE phone = {}".format(new_email, new_phone)

"""Prevent sql injection attack by using ? (placeholders) 
   than using string formatting.    
"""
update_sql = "UPDATE contacts SET email = ? WHERE phone = ?" # highly recommended where user input
update_cursor = db.cursor()
# update_cursor.executescript(update_sql) # executescript to allow executing multiple statements
                                        # Can result into danger though. just be careful (B.C)
update_cursor.execute(update_sql, (new_email, new_phone))
print("{} rows updated".format(update_cursor.rowcount))

print("Are connection the same: {}".format(update_cursor.connection == db)) # check if stored connections are ==
print("_" * 20)

update_cursor.connection.commit() #connection property highly recommended to commit
                                  # this commit will update the data in contacts3
                                  #commit when you are happy with the changes
update_cursor.close()

for row in db.execute("SELECT DISTINCT * FROM contacts ORDER BY name"): # without using cursor
    print(row)

db.close()