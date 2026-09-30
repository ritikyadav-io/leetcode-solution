SELECT MAX(salary) As SecondHighestSalary
FROM employee 
WHERE salary < (SELECT MAX(salary) FROM employee);
