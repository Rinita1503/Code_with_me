# Write your MySQL query statement below
SELECT
    p.firstname,
    p.Lastname,
    a.City,
    a.State
FROM Person as p
LEFT JOIN Address as a 
using (personID);       