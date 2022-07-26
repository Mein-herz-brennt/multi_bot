import sqlite3
import logging
import datetime


def new_db():
    conn = sqlite3.connect("multach_users.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE users_id (id_ int)""")
    cursor.execute("""CREATE TABLE users (id_ int, first_name text, last_name text, username text)""")
    cursor.execute("""CREATE TABLE course (id_ int, first_name text, username text, about_course text)""")
    cursor.execute("""CREATE TABLE admins (id_ int)""")
    cursor.execute("""CREATE TABLE channels (id_ int)""")
    conn.close()


class DateBase:
    def __init__(self):
        self.conn = sqlite3.connect("multach_users.db")
        self.cursor = self.conn.cursor()
        self.conn.row_factory = sqlite3.Row

    # work with users id
    def add_new_user(self, user_id: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO users_id VALUES (?)", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-add new user-*- " + str(e))
            return False
        finally:
            self.conn.close()

    def get_all_users_id(self) -> list:
        try:
            return [i[0] for i in self.cursor.execute("SELECT * FROM users_id").fetchall()]
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-get all users id-*- " + str(e))
            return []
        finally:
            self.conn.close()

    def delete_user(self, user_id: int) -> bool:
        try:
            self.cursor.execute("""DELETE FROM users_id WHERE id_ = ?""", (user_id,))
            self.cursor.execute("""DELETE FROM users WHERE id_ = ?""", (user_id,))
            self.cursor.execute("""DELETE FROM course WHERE id_ = ?""", (user_id,))
            self.cursor.execute("""DELETE FROM admins WHERE id_ = ?""", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-delete-*- " + str(e))
            return False
        finally:
            self.conn.close()

    # work with admins id
    def add_new_admin(self, user_id: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO admins VALUES (?)", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-add new admin-*- " + str(e))
            return False
        finally:
            self.conn.close()

    def get_all_admins_id(self) -> list:
        try:
            return [i[0] for i in self.cursor.execute("SELECT * FROM users_id").fetchall()]
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-get all admins id-*- " + str(e))
            return []
        finally:
            self.conn.close()

    def delete_admin(self, user_id: int) -> bool:
        try:
            self.cursor.execute("""DELETE FROM admins WHERE id_ = ?""", (user_id,))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-delete-*- " + str(e))
            return False
        finally:
            self.conn.close()

    # work with channel
    def add_channel(self, channel_id: int) -> bool:
        try:
            self.cursor.execute("INSERT INTO channels VALUES (?)", (channel_id,))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-add new user-*- " + str(e))
            return False
        finally:
            self.conn.close()

    # work with new user
    def add_new_user_info(self, user_id: int, first_name: str, last_name: str, username: str) -> bool:
        try:
            self.cursor.execute("""INSERT INTO users VALUES (?,?,?,?)""", (user_id, first_name, last_name, username))
            self.conn.commit()
            return True
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-add new user-*- " + str(e))
            return False
        finally:
            self.conn.close()

    def get_all_users_info(self) -> list:
        try:
            return [{"id_": i[0], "first_name": i[1], "last_name": i[2], "username": i[3]}
                    for i in self.cursor.execute("""SELECT * FROM users""").fetchall()]
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-get all info about all user-*- " + str(e))
            return []
        finally:
            self.conn.close()

    def get_one_user_info(self, user_id: int) -> list:
        try:
            return [{"id_": i[0], "first_name": i[1], "last_name": i[2], "username": i[3]}
                    for i in self.cursor.execute("""SELECT * FROM users WHERE id_ = ?""", (user_id,)).fetchall()]
        except Exception as e:
            time = str(datetime.datetime.now())
            logging.warning(msg=time + " -*-get all info about one user-*- " + str(e))
            return []
        finally:
            self.conn.close()


if __name__ == '__main__':
    # DateBase().add_new_user(812748924)
    # print(DateBase().get_all_users_id())
    # DateBase().delete_user(812748924)
    pass
