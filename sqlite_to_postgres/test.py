import psycopg2

connection = psycopg2.connect(
    user="app",
    password="123qwe",
    host="127.0.0.1",
    port="5432",
    database="movies_database"
)

cursor = connection.cursor()

query = "SELECT * FROM content.film_work"
cursor.execute(query)
amount = cursor.fetchall()

cursor.close()
connection.close()