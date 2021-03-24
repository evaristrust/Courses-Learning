import sqlite3
# import pytz
#
# db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)
#
# for row in db.execute("SELECT * FROM histories"):
#     utc_time = row[0]
#     local_time = pytz.utc.localize(utc_time).astimezone()
#     print("{}\t{}".format(utc_time, local_time))
#
# db.close()

# You can also do the above by using this simple way.. it has advantages when creating view
db = sqlite3.connect("accounts.sqlite", detect_types=sqlite3.PARSE_DECLTYPES)

# for row in db.execute("SELECT strftime('%Y-%m-%d %H:%M:%f', histories.time, 'localtime') AS localtime,"
#                       "histories.account, histories.amount FROM histories ORDER BY histories.time"):

for row in db.execute("SELECT * FROM localhistory"):
    print(row)

db.close()