import sqlite3

with sqlite3.connect('cars.db') as connection:
    c = connection.cursor()

    newCars = [
                ('Ford', 'Explorer', 15),
                ('Ford', 'Focus', 20),
                ('Ford', 'Mustang', 25),
                ('Honda', 'Accord', 20),
                ('Honda', 'Civic', 15)
            ]
    
#   c.executemany("INSERT INTO inventory(Make, Model, Quantity)\
#                  values (?,?,?)", newCars)
#   c.execute("UPDATE inventory SET Quantity=? WHERE Quantity=?", (1, 20))

    c.execute("SELECT * FROM inventory")
    c.execute("SELECT * FROM inventory WHERE Make='Ford'")

    rows = c.fetchall()
    for row in rows:
        print(row)
