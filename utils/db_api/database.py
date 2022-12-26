import sqlite3


class Database:
    def __init__(self, path_to_db='data/users.db'):
        self.path_to_db = path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execute(self, sql: str, fetchone=False, fetchall=False, commit=False):
        print(sql)
        connection = self.connection
        cursor = connection.cursor()
        cursor.execute(sql)
        data = None
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fetchall:
            data = cursor.fetchall()
        connection.close()
        return data

    def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS Users (
        id int NOT NULL,
        language varchar(255),
        PRIMARY KEY (id)
        );
        """
        self.execute(sql, commit=True)

    def add_user(self, id, language=None):
        sql = f"""INSERT INTO Users (id, language) VALUES ({id}, "{language}");"""
        self.execute(sql, commit=True)

    def select_language(self, id):
        sql = f"SELECT language FROM Users WHERE id={id};"
        return self.execute(sql, fetchone=True)

    def select_all(self):
        sql = f"SELECT * FROM Users;"
        return self.execute(sql, fetchall=True)

    def update_language(self, id, new_language):
        sql = f"""UPDATE Users SET language="{new_language}" WHERE id={id};"""
        self.execute(sql, commit=True)
