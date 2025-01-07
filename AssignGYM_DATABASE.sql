CREATE DATABASE GYM_DATABASE;

USE GYM_DATABASE;

CREATE TABLE Members (
    id INT PRIMARY KEY,            
    name VARCHAR(255) NOT NULL,
    age INT
);

CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,   
    member_id INT,                     
    date DATE,
    duration_minutes VARCHAR(50),
    calories_burned VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)  
);

ALTER TABLE WorkoutSessions 
MODIFY session_id INT AUTO_INCREMENT;


INSERT INTO Members (id, name, age)
VALUES 
    (1, 'Emily Smith', 30),
    (2, 'Harry Dhillon', 40),
    (3, 'Amrit Singh', 17),
    (4, 'Indie Dhillon', 20);

INSERT INTO WorkoutSessions (member_id, date, duration_minutes, calories_burned)
VALUES 
    (1, '2024-12-12', '45', '301'),
    (2, '2024-12-12', '60', '300'),
    (3, '2024-12-13', '120', '500'),
    (4, '2024-12-13', '30', '150');

SELECT * FROM GYM_DATABASE.Members;
SELECT * FROM GYM_DATABASE.WorkoutSessions;
