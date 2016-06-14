import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    
#    c.execute("UPDATE population SET population = 90000 WHERE city=\
#              'New York City'")
#
#    c.execute("DELETE FROM population WHERE city='Boston'")

    print("\nNEW DATA:\n")

    c.execute("SELECT * FROM population WHERE state='CA'")

    rows = c.fetchall()
    for row in rows:
        print(row)
