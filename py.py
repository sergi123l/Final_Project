import sqlite3 
con = sqlite3.connect("dvd.db") # соединение с базой данных, если бд нет, то файл создастся

cur = con.cursor()
cur.execute("CREATE TABLE quest(answ, ques)")
cur.execute("""
    INSERT INTO quest VALUES
        ('Monty Python and the Holy Grail', 1975, 8.2),
        ('And Now for Something Completely Different', 1971, 7.5)
""")
con.commit()

for row in cur.execute("SELECT ques, answ FROM qest ORDER BY ques"):
    print(row)
con.close()