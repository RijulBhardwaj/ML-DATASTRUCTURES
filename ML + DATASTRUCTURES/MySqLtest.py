import mysql.connector
from mysql.connector import Error

try:
    # Establish the connection
    connection = mysql.connector.connect(
        host='localhost',         
        database='mydatabase',    
        user='root',      
        password='RijulRyka@2608'   
    )

    if connection.is_connected():
        print("Connected to MySQL database")

        
        cursor = connection.cursor()

       #inserting data
        insert_query = """
        INSERT INTO mytable (name, age, email)
        VALUES (%s, %s, %s)
        """
        records_to_insert = [
            ('Laura Palmer', 27, 'laura@example.com'),
            ('Michael Scott', 45, 'michael@example.com'),
            ('Pam Beesly', 30, 'pam@example.com'),
        ]
        cursor.executemany(insert_query, records_to_insert)
        connection.commit()
        print(cursor.rowcount, "records inserted successfully")

        # Example query to fetch data
        select_query = "SELECT * FROM mytable"
        cursor.execute(select_query)
        records = cursor.fetchall()

        print("Displaying records from mytable:")
        for row in records:
            print(row)

except Error as e:
    print(f"Error while connecting to MySQL: {e}")
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
