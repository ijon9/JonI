import sqlite3

#open db if exists, otherwise create
db = sqlite3.connect("foo")

c = db.cursor() #facilitate db ops

c.execute("CREATE TABLE roster(name TEXT, userid INTEGER)")

db.commit()
db.close()
