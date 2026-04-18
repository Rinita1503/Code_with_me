# Write your MySQL query statement below
SELECT name as Customers
FROM Customers 
LEFT JOIN Orders
on Customers.id = Orders.customerID
WHERE Orders.customerID is null;