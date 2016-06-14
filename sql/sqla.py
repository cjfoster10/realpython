import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
            
    cities = [
            ('New York City', 'Northeast'),
            ('San Francisco', 'West'),
            ('Chicago', 'Midwest'),
            ('Houston', 'South'),
            ('Phoenix', 'West'),
            ('Boston', 'Northeast'),
            ('Los Angeles', 'West'),
            ('Houston', 'South'),
            ('Philadelphia', 'Northeast'),
            ('San Antonio', 'South'),
            ('San Diego', 'West'),
            ('Dallas', 'South'),
            ('San Jose', 'West'),
            ('Jacksonville', 'South'),
            ('Indianapolis', 'Midwest'),
            ('Austin', 'South'),
            ('Detroit', 'Midwest')
             ]

    c.execute("""CREATE TABLE regions
              (city TEXT, region TEXT)
              """)

    c.executemany("INSERT INTO regions VALUES(?, ?)", cities)

    c.execute("SELECT * FROM regions ORDER BY region ASC")
    rows = c.fetchall()

    for r in rows:
        print(r)
#cursor.execute("""CREATE TABLE population
#               (city TEXT, state TEXT, population INT)
#               """)
#
#    try:
#        c.execute("INSERT INTO populations VALUES('New York City', \
#                  'NY', 8200000)")
#    
#        c.execute("INSERT INTO populations VALUES('San Francisco', \
#                  'CA', 8000000)")
#        connection.commit()
#    except sqlite3.OperationalError:
#        print("Oops! Something went wrong. Try again...")

connection.close()
