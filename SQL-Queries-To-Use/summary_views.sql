-- summary_views.sql - used to look at quick summary information from the data

-- #1. Monthly Incident Summary
CREATE OR REPLACE VIEW monthly_incident_summary AS 
SELECT year, month, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY year, month
ORDER BY year, month;

-- #2. Quadrant Incident Summary
CREATE OR REPLACE VIEW quadrant_incident_summary AS
SELECT quadrant, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY quadrant
ORDER BY incident_count DESC;

-- #3. Location Incident Summary
CREATE OR REPLACE VIEW location_incident_summary AS
SELECT location, COUNT(*) AS incident_count
FROM traffic_incidents
GROUP BY location
ORDER BY incident_count DESC;