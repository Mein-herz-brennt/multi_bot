import sqlite3


def new_db():
    conn = sqlite3.connect("multach_users.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users_id (id_ int)""")
    cursor.execute("""CREATE TABLE users (id_ int, first_name text, last_name text, username text)""")
    cursor.execute("""CREATE TABLE course (id_ int, first_name text, username text, about_course text)""")
    cursor.execute("""CREATE TABLE admins (id_ int)""")
    cursor.execute("""CREATE TABLE channels (id_ int)""")


class DateBase:
    def __init__(self):
        self.conn = sqlite3.connect("multach_users.db")
        self.cursor = self.conn.cursor()


if __name__ == '__main__':
    print(5 / 1.75)
