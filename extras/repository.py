import mysql.connector
import pandas as pd

class Database:
    """
    Represents a database handler for storing temperature and humidity data.

    This class provides methods to interact with a MySQL database to store and retrieve temperature 
    and humidity data.
    """
    def __init__(self):
        """
        Initializes a Database instance.

        This constructor sets up the database connection and ensures the database and table exist.
        """
        self.__database_name = "temps"
        self.__table_name = "tempdata"

        self.check_database_exists()

        self.mydb = mysql.connector.connect(
            host="localhost",
            user="pi",
            password="abc123",
            database=self.__database_name
        )

        self.check_table_exists()

    def check_database_exists(self):
        """
        Checks if the specified database exists and creates it if it doesn't.

        This method checks for the existence of the database with the specified name and creates 
        it if not found.
        """
        temp_connection = mysql.connector.connect(
            host="localhost",
            user="pi",
            password="abc123"
        )

        cursor = temp_connection.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{self.__database_name}'")
        exists = cursor.fetchone()
        temp_connection.close()

        if not exists:
            print(f"Database '{self.__database_name}' does not exist.")
            cursor.execute(f"CREATE DATABASE {self.__database_name}")
        cursor.close()

    def get_dataframe(self):
        """
        Retrieves data from the table and returns it as a Pandas DataFrame.

        Returns:
        pandas.DataFrame: A DataFrame containing the selected data from the table.
        """
        cursor = self.mydb.cursor()
        sql = f"SELECT * FROM {self.__table_name}"
        cursor.execute(sql)
        selected_data = cursor.fetchall()

        df = pd.DataFrame(selected_data, columns=[col[0] for col in cursor.description])
        return df

    def check_table_exists(self):
        """
        Checks if the specified table exists and creates it if it doesn't.

        This method checks for the existence of the table with the specified name and creates it 
        if not found.
        """
        cursor = self.mydb.cursor()
        cursor.execute(f"SHOW TABLES LIKE '{self.__table_name}'")
        result = cursor.fetchone()

        if not result:
            create_table_query = (
                f"CREATE TABLE {self.__table_name} ("
                "recorded_time DATETIME, "
                "temperature NUMERIC, "
                "temperature_category VARCHAR(255), "
                "humidity NUMERIC, "
                "humidity_category VARCHAR(255)"
                ")"
            )
            cursor.execute(create_table_query)
            cursor.close()
    def insert(self, data):
        """
        Inserts data into the table.

        Parameters:
        data (dict): A dictionary containing data to be inserted into the table.
        """
        cursor = self.mydb.cursor()
        insert_query = (
            f"INSERT INTO {self.__table_name} "
            "(recorded_time, temperature, temperature_category, humidity, humidity_category) "
            "VALUES (%s, %s, %s, %s, %s)"
        )
        insert_data = (
            data["recorded_time"],
            data["temperature"],
            data["temperature_category"],
            data['humidity'],
            data['humidity_category']
        )
        cursor.execute(insert_query, insert_data)
        self.mydb.commit()
        cursor.close()

    def select(self):
        """
        Retrieves all data from the table and prints it.

        This method retrieves all data from the table and prints each record.
        """
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT * FROM {self.__table_name}")
        result = cursor.fetchall()
        for row in result:
            print(row)
        