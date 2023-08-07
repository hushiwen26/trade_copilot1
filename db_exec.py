import pymysql

class MySQLExecutor:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

    def execute_query(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        # print(cursor.description)
        # print(len(cursor.description))
        result = cursor.fetchall()
        cursor.close()
        return result

    def execute_update(self, query):
        cursor = self.connection.cursor()
        cursor.execute(query)
        self.connection.commit()
        affected_rows = cursor.rowcount
        cursor.close()
        return affected_rows

    def disconnect(self):
        if self.connection is not None:
            self.connection.close()


if __name__ == "__main__":
    executor = MySQLExecutor(host="localhost", user="root", password="sensors2017", database="openai")
    executor.connect()
