
import sqlite3


cnt = sqlite3.connect("bollywood")


cnt.execute('''CREATE TABLE movies(
name TEXT,
actor TEXT,
actress TEXT,
yearOfRelease INTEGER,);''')

cnt.execute('''INSERT INTO movies VALUES(
'Entertainment', 'Akshay','Tamannaah', 2014);''')

cnt.commit()


cnt.execute('SELECT * FROM movies')

cnt.execute('SELECT * FROM movies WHERE actor = 'Akshay Kumar'')
