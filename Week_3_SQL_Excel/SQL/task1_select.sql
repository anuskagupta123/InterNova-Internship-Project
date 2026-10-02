-- =====================================================
-- INTERN NOVA INTERNSHIP
-- WEEK 3 ASSIGNMENT: SQL & EXCEL
-- TASK 1: INTRODUCTION TO DATABASES & SELECT
-- =====================================================

-- 1. CREATE DATABASE
CREATE DATABASE IF NOT EXISTS InternNova;

-- 2. SELECT DATABASE
USE InternNova;

-- 3. CREATE EMPLOYEES TABLE
CREATE TABLE IF NOT EXISTS Employees (
    Employee_ID INT PRIMARY KEY,
    Employee_Name VARCHAR(50),
    Department VARCHAR(50),
    Age INT,
    Salary DECIMAL(10,2)
);

-- 4. INSERT SAMPLE DATA
INSERT IGNORE INTO Employees
(Employee_ID, Employee_Name, Department, Age, Salary)
VALUES
(101, 'Rahul', 'IT', 25, 35000.00),
(102, 'Priya', 'HR', 28, 40000.00),
(103, 'Arun', 'Finance', 30, 45000.00),
(104, 'Sneha', 'IT', 24, 32000.00),
(105, 'Karan', 'Marketing', 29, 38000.00),
(106, 'Divya', 'HR', 27, 42000.00),
(107, 'Vikram', 'Finance', 32, 50000.00),
(108, 'Ananya', 'IT', 26, 37000.00),
(109, 'Rohit', 'Marketing', 31, 46000.00),
(110, 'Meena', 'Finance', 29, 48000.00);

-- 5. DISPLAY ALL RECORDS
SELECT * FROM Employees;

-- 6. SELECT SPECIFIC COLUMNS
SELECT Employee_Name, Salary
FROM Employees;

-- 7. SELECT WITH COLUMN ALIASES
SELECT
    Employee_ID AS ID,
    Employee_Name AS Name,
    Department AS Dept,
    Salary AS Monthly_Salary
FROM Employees;

-- 8. DISPLAY ONLY EMPLOYEE NAMES
SELECT Employee_Name
FROM Employees;

-- 9. DISPLAY EMPLOYEE ID AND DEPARTMENT
SELECT Employee_ID, Department
FROM Employees;

-- 10. DISPLAY TABLE STRUCTURE
DESCRIBE Employees;