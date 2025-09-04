import psycopg2
from datetime import date
import config

connection = psycopg2.connect(
    host = config.HOST,
    port = config.PORT,
    user = config.USER,
    password = config.PASSWORD,
    dbname = config.DBNAME
)


cursor = connection.cursor()
cursor.execute("DROP TABLE IF EXISTS tasks;")
cursor.execute("""
    CREATE TABLE tasks(
        id SERIAL,
        title VARCHAR(128) NOT NULL,
        description TEXT,
        due_date DATE NOT NULL,
        created_at DATE NOT NULL,
               
        PRIMARY KEY(id)
    );
""")

due_date = date( year = 2025, month = 8, day = 21)
today = date.today()

cursor.execute("""
    INSERT INTO tasks(title, description, due_date, created_at)
    VALUES (%s, %s, %s, %s)
""", ['yugurish', 'ertalab 3,5km yugurish kerak', due_date, today])
cursor.execute("""
    INSERT INTO tasks(title, description, due_date, created_at)
    VALUES (%s, %s, %s, %s)
""", ['dars qilish', 'ertalab 2 soat dars qilishim kerak', due_date, today])

cursor.execute("SELECT * FROM tasks;")
rows = cursor.fetchall()
for row in rows:
    id, title, desc, due_date, created_ad = row
    print(id, due_date)

cursor.close()

connection.commit()
connection.close()

