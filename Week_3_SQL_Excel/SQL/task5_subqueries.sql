USE InternNova;

-- 1. Find employees earning more than the average salary
SELECT Employee_ID, Employee_Name, Department, Salary
FROM Employees
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
);


-- 2. Find employees earning the highest salary
SELECT Employee_ID, Employee_Name, Department, Salary
FROM Employees
WHERE Salary = (
    SELECT MAX(Salary)
    FROM Employees
);


-- 3. Find employees earning the lowest salary
SELECT Employee_ID, Employee_Name, Department, Salary
FROM Employees
WHERE Salary = (
    SELECT MIN(Salary)
    FROM Employees
);


-- 4. Find employees working in departments with more than 2 employees
SELECT Employee_ID, Employee_Name, Department
FROM Employees
WHERE Department IN (
    SELECT Department
    FROM Employees
    GROUP BY Department
    HAVING COUNT(*) > 2
);


-- 5. Find employees earning more than the average salary
-- in their own department
SELECT Employee_ID, Employee_Name, Department, Salary
FROM Employees e
WHERE Salary > (
    SELECT AVG(Salary)
    FROM Employees
    WHERE Department = e.Department
);


-- 6. Find departments whose average salary is greater
-- than the overall average salary
SELECT Department, AVG(Salary) AS Average_Salary
FROM Employees
GROUP BY Department
HAVING AVG(Salary) > (
    SELECT AVG(Salary)
    FROM Employees
);


-- 7. Find employees earning more than the salary of Rahul
SELECT Employee_ID, Employee_Name, Department, Salary
FROM Employees
WHERE Salary > (
    SELECT Salary
    FROM Employees
    WHERE Employee_Name = 'Rahul'
);


-- 8. Find employees who work in the same department as Priya
SELECT Employee_ID, Employee_Name, Department
FROM Employees
WHERE Department = (
    SELECT Department
    FROM Employees
    WHERE Employee_Name = 'Priya'
);