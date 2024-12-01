import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="school"
    )

# Insert a new student record
def insert_student(roll,name):
    db = connect_db()
    cursor = db.cursor()
    cursor.execute('INSERT INTO student (roll_no, name) VALUES (%s, %s)', (roll,name))
    db.commit()
    print(f"Inserted student: {name}")
    db.close()

insert_student("20","C")
