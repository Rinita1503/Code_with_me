# Write your MySQL query statement below
SELECT s.price, s.year, p.product_name
FROM Sales s
LEFT JOIN Product p
ON s.product_id = p.product_id