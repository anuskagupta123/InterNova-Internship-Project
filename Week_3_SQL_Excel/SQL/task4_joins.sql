USE InternNova;

-- Create Departments table
CREATE TABLE IF NOT EXISTS Departments (
    DepartmentID INT PRIMARY KEY,
    DepartmentName VARCHAR(50),
    Location VARCHAR(50)
);

-- Insert department data
INSERT IGNORE INTO Departments
(DepartmentID, DepartmentName, Location)
VALUES
(1, 'IT', 'Coimbatore'),
(2, 'HR', 'Chennai'),
(3, 'Finance', 'Bangalore'),
(4, 'Marketing', 'Coimbatore'),
(5, 'Sales', 'Chennai');

-- Display Departments
SELECT * FROM Departments;


-- 1. INNER JOIN
SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
INNER JOIN Departments
ON Employees.Department = Departments.DepartmentName;


-- 2. LEFT JOIN
SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
LEFT JOIN Departments
ON Employees.Department = Departments.DepartmentName;


-- 3. RIGHT JOIN
SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
RIGHT JOIN Departments
ON Employees.Department = Departments.DepartmentName;


-- 4. FULL OUTER JOIN using UNION
SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
LEFT JOIN Departments
ON Employees.Department = Departments.DepartmentName

UNION

SELECT
    Employees.Employee_ID,
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
RIGHT JOIN Departments
ON Employees.Department = Departments.DepartmentName;


-- 5. JOIN with WHERE
SELECT
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
INNER JOIN Departments
ON Employees.Department = Departments.DepartmentName
WHERE Departments.Location = 'Coimbatore';


-- 6. JOIN with ORDER BY
SELECT
    Employees.Employee_Name,
    Employees.Department,
    Departments.Location
FROM Employees
INNER JOIN Departments
ON Employees.Department = Departments.DepartmentName
ORDER BY Employees.Employee_Name ASC;