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
