# Question1 - 

import mysql.connector
from mysql.connector import Error


def connect_database():
    # database connection parameters
    db_name = "GYM_DATABASE"
    user = "root"
    password = "Amrit101!"
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
    
#task1 

def add_member(id, name, age):
    """Function to add a new member to the Members table."""
    try:
        conn = connect_database()
        if conn is not None:
            cursor = conn.cursor()

            query = """INSERT INTO Members (id, name, age)
                       VALUES (%s, %s, %s)"""
            data = (id, name, age)

            cursor.execute(query, data)
            conn.commit()

            print(f"Member with ID {id} successfully added to the database!")

    except Exception as e:
        print(f"Error: {e}")
        if e.errno == 1062:
            print("Error: Member ID already exists in the database.")

    finally:
        cursor.close()
        conn.close()
        print("Exiting the MySQL connection.")

add_member(5, "John Doe", 57)

#task 2-

def add_workout_session(member_id, date, duration_minutes, calories_burned):
    """Function to add a new workout session."""
    try:
        conn = connect_database()
        if conn is not None:
            cursor = conn.cursor()

            query = """INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
                       VALUES (%s, %s, %s, %s)"""
            data = (member_id, date, duration_minutes, calories_burned)

            cursor.execute(query, data)
            conn.commit()

            print(f"Workout for member ID {member_id} successfully added to the database!")

    except Exception as e:
        print(f"Error: {e}")
        if e.errno == 1062:
            print("Error: Member ID already exists in the database.")

    finally:
        cursor.close()
        conn.close()
        print("Exiting the MySQL connection.")

add_workout_session(3, "2025-01-07", 46, 300)

def update_member_age(member_id, new_age):
    """Updates the age of a member based on their member_id"""
    try:
        conn = connect_database()
        if conn is not None:
            cursor = conn.cursor()

            check_query = "SELECT id FROM Members WHERE id = %s"
            cursor.execute(check_query, (member_id,))
                
            if cursor.fetchone():  
                update_query = "UPDATE Members SET age = %s WHERE id = %s"
                cursor.execute(update_query, (new_age, member_id))
            
                conn.commit()
                print(f"Member with ID {member_id} successfully updated to age {new_age}.")
            else:
                print(f"Error: Member with ID {member_id} does not exist.")

    except Exception as e:
        print(f"Error: {e}")

update_member_age(1,25)   #updating age of member
update_member_age(2,29) 
update_member_age(15,45)  #testing error catching for ID that does not exist

def delete_workout_session(session_id):
    """Deleting a workout session via its session_id"""
    try:
        conn = connect_database()
        if conn is not None:
            cursor = conn.cursor()

            check_query = "SELECT session_id FROM WorkoutSessions WHERE session_id = %s"
            cursor.execute(check_query, (session_id,))
                
            # If session exists, delete it
            if cursor.fetchone():  # Session exists
                delete_query = "DELETE FROM WorkoutSessions WHERE session_id = %s"
                cursor.execute(delete_query, (session_id,))
                    
                # Commit the changes to the database
                conn.commit()
                print(f"Workout session with ID {session_id} successfully deleted.")
            else:
                print(f"Error: Workout session with ID {session_id} does not exist.")
    except Exception as e:
        print(f"Error: {e}")

delete_workout_session(3) #deleting existing session
delete_workout_session(10)  #testing on non-existant session 