import sqlite3

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()

    sql = {'avg': "SELECT avg(num) FROM numbers",
          'max': "SELECT max(num) FROM numbers",
          'min': "SELECT min(num) FROM numbers",
          'sum': "SELECT sum(num) FROM numbers"}

    user = input("Please Enter avg, max, min or sum: ")
    sqlKeys = sorted(sql.keys())
    flag = True
    while flag == True:
        if user in sqlKeys:
            c.execute(sql[user])
            print(c.fetchone())
            userInput = input('press any key to continue or q to quit: ')
        else:
            userInput = input('Wrong selection, press any key to continue or q to quit: ')
            if userInput == "q":
                flag = False
