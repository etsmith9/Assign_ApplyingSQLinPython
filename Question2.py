#Question2

import mysql.connector
from mysql.connector import Error


def connect_database():
    # database connection parameters
    db_name = "GYM_DATABASE"
    user = "root"
    password = "****"
    host = "localhost"

    try: 
        #Attemping to establish a connection
        conn = mysql.connector.connect(
            database = db_name,
            user = user,
            password = password,
            host = host
        )

    #check if the connection is successful
        print("Connected to MySQL database successfully")
        return conn

    except Error as e:
        #hangling any connection errors
        print("Error: {e}")
        return None
    
def get_members_in_age_range(start_age, end_age):
    """Retrieve members whose ages fall between the specified range"""
    try:
        with connect_database() as conn:
            with conn.cursor() as cursor:
                query = """
                SELECT id, name, age 
                FROM Members 
                WHERE age BETWEEN %s AND %s;
                """
                cursor.execute(query, (start_age, end_age))
                
                result = cursor.fetchall()
                
                if result:
                    print(f"Members between the ages of {start_age} and {end_age}:")
                    for row in result:
                        print(f"ID: {row[0]}, Name: {row[1]}, Age: {row[2]}")
                else:
                    print(f"No members found between the ages of {start_age} and {end_age}.")
    
    except Exception as e:
        print(f"Error: {e}")


get_members_in_age_range(25, 30)  