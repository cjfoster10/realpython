#NOTE: You can also use the ":memory:" string to create a database in memory only

with sqlite3.connect('roster.db') as connection:
  c = connection.cursor()
  c.execute("DROP TABLE IF EXISTS Roster")
  c.execute("CREATE TABLE Roster(Name TEXT, Species TEXT, IQ INT)")
  c.executemany("INSERT INTO Roster VALUES(?,?,?)", roster)

with sqlite3.connect('roster.db') as connection:
  c = connection.cursor()
  c.execute("UPDATE Roster SET Species=? WHERE Name=?", ('Human', 'Korben Dallas'))

with sqlite3.connect('roster.db') as connection:
  c = connection.cursor()
  c.execute("SELECT * FROM Roster")
  while True:
    row = c.fetchone()
    if row is None:
      break
      print(row)
     
with sqlite3.connect('roster.db') as connection:
  c = connection.cursor()
  c.execute("SELECT Name, IQ, Species FROM Roster WHERE Species == 'Human'")
  for row in c.fetchall():
    print(row)

with sqlite3.connect('roster.db') as connection:
  c = connection.cursor()
  c.execute("SELECT Name, Species, IQ FROM Roster WHERE IQ > 120")
  for row in c.fetchall():
    print(row)

Basic SQL syntax:

Create table:
    cursor.execute("""CREATE TABLE population
                (city TEXT, state TEXT, population INT)
                """)
Inserting:
    INSERT INTO table_name (column1, column2, column3)
    VALUES (value1, value2, value3);

Updating:
    UPDATE table_name
    SET column1=value1
    WHERE some_column=some_value;

Deleting:
    DELETE FROM table_name
    WHERE some_column=some_value;
