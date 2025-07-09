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
-- Child table
CREATE TABLE IF NOT EXISTS child (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    age INT NOT NULL,
    parent_name VARCHAR(100) NOT NULL
);

-- Student table
CREATE TABLE IF NOT EXISTS student (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    roll_no VARCHAR(20) NOT NULL,
    class_name VARCHAR(50) NOT NULL
);
