import psycopg2

CREATE TABLE Contacts (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(100),
    Phone VARCHAR(20)
);

CREATE TABLE CSVData (
    ID INT PRIMARY KEY AUTO_INCREMENT,
    CSVData TEXT
);