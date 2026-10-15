-- Write your query below
SELECT 
    u.name, COALESCE(sum(r.distance), 0) as travelled_distance
FROM users u 
LEFT JOIN rides r on u.id = r.user_id 
GROUP BY u.id, u.name
ORDER BY travelled_distance DESC, u.name ASC