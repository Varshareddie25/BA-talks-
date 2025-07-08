-- Create database
CREATE DATABASE emp_db;

-- Use the database
USE emp_db;

-- Create employees table
CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    name VARCHAR(100),                 
    emp_id VARCHAR(20),                
    department VARCHAR(50),           
    designation VARCHAR(50)            
);
