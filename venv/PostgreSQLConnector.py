import psycopg2

class PostgreSQLConnector:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = dbname
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.connection = None
        self.cursor = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                dbname=self.dbname,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
            print("Connected to the PostgreSQL database.")

        except psycopg2.Error as e:
            print(f"Error connecting to the PostgreSQL database: {e}")

    def execute_query(self, query, params=None):
        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchall()
            return result

        except psycopg2.Error as e:
            print(f"Error executing the query: {e}")

    def get_user_by_id(self, user_id):
        query = "SELECT username, password FROM account_table WHERE id = %s;"
        params = (user_id,)
        result = self.execute_query(query, params)

        if result:
            username, password = result[0]
            return {"username": username, "password": password}
        else:
            print(f"No user found with ID {user_id}")
            return None

    def add_user(self, username, phone_number):
        query = "INSERT INTO numbers_table (username, phone_number) VALUES (%s, %s);"
        params = (username, phone_number)

        try:
            self.cursor.execute(query, params)
            self.connection.commit()
            print(f"User '{username}' with phone number '{phone_number}' added successfully.")

        except psycopg2.Error as e:
            print(f"Error adding user: {e}")
            self.connection.rollback()

    def username_exists(self, username):
        query = "SELECT COUNT(*) FROM numbers_table WHERE username = %s;"
        params = (username,)

        try:
            self.cursor.execute(query, params)
            result = self.cursor.fetchone()
            return result[0] > 0  # True if the username exists, False otherwise

        except psycopg2.Error as e:
            print(f"Error checking username existence: {e}")
            return False

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
            print("Connection closed.")