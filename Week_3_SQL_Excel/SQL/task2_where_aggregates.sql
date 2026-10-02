-- =====================================================
-- INTERN NOVA INTERNSHIP
-- WEEK 3 ASSIGNMENT: SQL & EXCEL
-- TASK 2: WHERE, ORDER BY & AGGREGATE FUNCTIONS
-- =====================================================

-- Select the database
USE InternNova;


-- 1. WHERE CLAUSE
-- Display employees working in the IT department

SELECT *
FROM Employees
WHERE Department = 'IT';


-- 2. WHERE WITH COMPARISON OPERATOR
-- Display employees whose salary is greater than 40000

SELECT *
FROM Employees
WHERE Salary > 40000;


-- 3. WHERE WITH AND OPERATOR
-- Display employees older than 25 with a salary greater than 40000

SELECT *
FROM Employees
WHERE Age > 25 AND Salary > 40000;


-- 4. WHERE WITH OR OPERATOR
-- Display employees working in IT or HR

SELECT *
FROM Employees
WHERE Department = 'IT' OR Department = 'HR';


-- 5. ORDER BY ASCENDING
-- Display employees sorted by salary in ascending order

SELECT *
FROM Employees
ORDER BY Salary ASC;


-- 6. ORDER BY DESCENDING
-- Display employees sorted by salary in descending order

SELECT *
FROM Employees
ORDER BY Salary DESC;


-- 7. COUNT()
-- Count the total number of employees

SELECT COUNT(*) AS Total_Employees
FROM Employees;


-- 8. SUM()
-- Calculate the total salary of all employees

SELECT SUM(Salary) AS Total_Salary
FROM Employees;


-- 9. AVG()
-- Calculate the average salary of employees

SELECT AVG(Salary) AS Average_Salary
FROM Employees;


-- 10. MIN()
-- Find the minimum salary

SELECT MIN(Salary) AS Minimum_Salary
FROM Employees;


-- 11. MAX()
-- Find the maximum salary

SELECT MAX(Salary) AS Maximum_Salary
FROM Employees;


-- 12. COMBINED AGGREGATE FUNCTIONS
-- Display all aggregate values in one query

SELECT
    COUNT(*) AS Total_Employees,
    SUM(Salary) AS Total_Salary,
    ROUND(AVG(Salary), 2) AS Average_Salary,
    MIN(Salary) AS Minimum_Salary,
    MAX(Salary) AS Maximum_Salary
FROM Employees;