-- =====================================================
-- INTERN NOVA INTERNSHIP
-- WEEK 3 ASSIGNMENT: SQL & EXCEL
-- TASK 3: GROUP BY & HAVING
-- =====================================================

-- Select the database
USE InternNova;


-- 1. GROUP BY
-- Count the number of employees in each department

SELECT
    Department,
    COUNT(*) AS Total_Employees
FROM Employees
GROUP BY Department;


-- 2. GROUP BY WITH SUM()
-- Calculate the total salary for each department

SELECT
    Department,
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department;


-- 3. GROUP BY WITH AVG()
-- Calculate the average salary for each department

SELECT
    Department,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees
GROUP BY Department;


-- 4. GROUP BY WITH MIN() AND MAX()
-- Find the minimum and maximum salary in each department

SELECT
    Department,
    MIN(Salary) AS Minimum_Salary,
    MAX(Salary) AS Maximum_Salary
FROM Employees
GROUP BY Department;


-- 5. GROUP BY WITH MULTIPLE AGGREGATE FUNCTIONS
-- Calculate employee count, total salary, and average salary
-- for each department

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    SUM(Salary) AS Total_Salary,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees
GROUP BY Department;


-- 6. HAVING CLAUSE
-- Display departments with more than 2 employees

SELECT
    Department,
    COUNT(*) AS Total_Employees
FROM Employees
GROUP BY Department
HAVING COUNT(*) > 2;


-- 7. HAVING WITH SUM()
-- Display departments with total salaries greater than 100000

SELECT
    Department,
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department
HAVING SUM(Salary) > 100000;


-- 8. HAVING WITH AVG()
-- Display departments with an average salary greater than 40000

SELECT
    Department,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > 40000;


-- 9. GROUP BY WITH WHERE AND HAVING
-- Consider only employees older than 25
-- Display departments with an average salary above 40000

SELECT
    Department,
    COUNT(*) AS Total_Employees,
    ROUND(AVG(Salary), 2) AS Average_Salary
FROM Employees
WHERE Age > 25
GROUP BY Department
HAVING AVG(Salary) > 40000;


-- 10. GROUP BY WITH ORDER BY
-- Display departments sorted by total salary
-- from highest to lowest

SELECT
    Department,
    SUM(Salary) AS Total_Salary
FROM Employees
GROUP BY Department
ORDER BY Total_Salary DESC;