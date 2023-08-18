import mysql.connector
import pandas as pd

class Database:
    def __init__(self):
        
        self.__databaseName = "temps"
        self.__tableName="tempdata"
        
        self.checkDatabaseExists()
        
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="pi",
            password="abc123",
            database=self.__databaseName
        )
        
        self.checkTableExists()
        
  
    def checkDatabaseExists(self):
        
        temp_connection = mysql.connector.connect(
            host="localhost",
            user="pi",
            password="abc123"
        )

        # Create a cursor to execute queries
        cursor = temp_connection.cursor()

        # Check if the database exists
     
        cursor.execute(f"SHOW DATABASES LIKE '{self.__databaseName}'")
        exists = cursor.fetchone()

        # Close the temporary connection
        temp_connection.close()

        # If the database does not exist, notify the user or create it
        if not exists:
            print(f"Database '{self.__databaseName}' does not exist.")
            cursor.execute("CREATE DATABASE {database_name}")    
        
        cursor.close()
        
    
    def getDataFrame(self):
        # Create a cursor to execute queries
        cursor = self.mydb.cursor()
        # SQL query to select data from the table
        sql = f"SELECT * FROM {self.__tableName}"
        # Execute the query to select data
        cursor.execute(sql)
        # Fetch all the selected data
        selected_data = cursor.fetchall()

        # Create a Pandas DataFrame from the selected data
        df = pd.DataFrame(selected_data, columns=[col[0] for col in cursor.description])
        return df 
    
    def checkTableExists(self):
        
        cursor = self.mydb.cursor()
        
        # Check if the table exists
        cursor.execute(f"SHOW TABLES LIKE '{self.__tableName}'")
        
        # Fetch one row from the result (if any)
        result = cursor.fetchone()
       
        # If table not in database create table
        if not result:
            cursor.execute(f"CREATE TABLE {self.__tableName} (recorded_time DATETIME, temperature NUMERIC, temperature_category VARCHAR(255), humidity NUMERIC, humidity_category VARCHAR(255))")
        
        cursor.close() 
    
    def insert(self,data):
        cursor = self.mydb.cursor()
        sql = f"INSERT INTO {self.__tableName} (recorded_time, temperature, temperature_category, humidity, humidity_category) VALUES (%s, %s, %s, %s, %s)" 
        cursor.execute(sql, (data["recorded_time"], data["temperature"], data["temperature_category"],data['humidity'],data['humidity_category']))
        self.mydb.commit()
        cursor.close()
    
    def select(self):
        cursor = self.mydb.cursor()
        cursor.execute(f"SELECT * FROM {self.__tableName}")
        result = cursor.fetchall()
        for x in result:
            print(x)
        