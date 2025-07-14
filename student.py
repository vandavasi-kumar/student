import pymysql

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="admin@123",
    database="student1"
)

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    grade VARCHAR(10)
)
""")
conn.commit()

def add_student(cursor, conn):
    name = input("Enter name: ")
    age = input("Enter age: ")
    grade = input("Enter grade: ")
    cursor.execute("INSERT INTO students (name, age, grade) VALUES (%s, %s, %s)", (name, age, grade))
    conn.commit()
    print("Student added.")

def view_students(cursor):
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    if students:
        print("\nStudent List:")
        for student in students:
            print(student)
    else:
        print("No students found.")

def update_student(cursor, conn):
    student_id = input("Enter student ID to update: ")
    name = input("New name: ")
    age = input("New age: ")
    grade = input("New grade: ")
    cursor.execute("UPDATE students SET name=%s, age=%s, grade=%s WHERE id=%s", (name, age, grade, student_id))
    conn.commit()
    print("Student updated.")

def delete_student(cursor, conn):
    student_id = input("Enter student ID to delete: ")
    cursor.execute("DELETE FROM students WHERE id=%s", (student_id,))
    conn.commit()
    print("Student deleted.")

def menu(cursor, conn):
    while True:
        print("\nStudent Management System")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_student(cursor, conn)
        elif choice == '2':
            view_students(cursor)
        elif choice == '3':
            update_student(cursor, conn)
        elif choice == '4':
            delete_student(cursor, conn)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    menu(cursor, conn)

