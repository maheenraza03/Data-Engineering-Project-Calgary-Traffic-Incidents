-- analysis.sql - used for analysis queries on the traffic incidents data from the API

-- #1. Incident Counts by Month
SELECT year, month, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY year, month
ORDER BY year, month;

-- #2. Incident Counts by Quadrants
SELECT quadrant, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY quadrant
ORDER BY incident_count DESC;

-- #3. Top 10 incident locations by incident count
SELECT location, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY location
ORDER BY incident_count DESC
LIMIT 10;