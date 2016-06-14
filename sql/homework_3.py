import sqlite3

with sqlite3.connect("cars.db") as connection:
    c = connection.cursor()

#    c.execute("""CREATE TABLE orders
#              (make TEXT, model TEXT, order_date TEXT)
#              """
#             )

    car_orders = [ 
        ('Ford', 'Focus', '2015-03-30'),
        ('Ford', 'Focus', '2015-11-30'),
        ('Ford', 'Focus', '2011-11-30'),
        ('Ford', 'Mustang', '2009-04-30'),
        ('Ford', 'Mustang', '2009-05-30'),
        ('Ford', 'Mustang', '2011-04-30'),
        ('Honda', 'Civic', '2011-11-30'),
        ('Honda', 'Civic', '2012-01-30'),
        ('Honda', 'Civic', '2011-11-30'),
    ]

#    c.executemany("INSERT INTO orders VALUES(?,?,?)", car_orders)

#    c.execute("""SELECT inventory.Make, 
#        inventory.Model, inventory.Quantity, orders.order_date
#              FROM inventory, orders WHERE
#        inventory.Model = orders.model
#              ORDER by inventory.Model ASC""")
    car_sql = {'count': "SELECT count(order_date) FROM orders\
               GROUP BY orders.model"} 

    for keys, values in car_sql.items():

         c.execute(values)
         result = c.fetchone()
         print(keys + ":", result[0])
#    for r in row:
#        print("Car\'s Make and Model: {} {}".format(r[0], r[1]))
#        print("Quantity: {}".format(r[2]))
#        print("Order Date: {}".format(r[3]))
