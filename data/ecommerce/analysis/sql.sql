-- 1667. Fix Names in a Table

-- Write your PostgreSQL query statement below
SELECT
u.user_id,
UPPER(LEFT(u.name,1)) || LOWER(SUBSTRING(u.name from 2)) AS name
FROM Users AS u
order by u.user_id



-- 176. Second Highest Salary
-- Write your PostgreSQL query statement below
WITH second_cte AS(
    SELECT
    CASE WHEN COUNT(DISTINCT(e.salary))>1 THEN NULL ELSE e.salary END as salary,
    ROW_NUMBER() OVER(ORDER BY e.salary DESC) as SecondHighestSalary
    FROM Employee as e
    GROUP BY e.salary
)
SELECT COALESCE(
    (SELECT s.salary FROM second_cte AS s where s.SecondHighestSalary=2),NULL
) AS "SecondHighestSalary"