-- Top 10 Most Popular Tracks
SELECT track_name, track_popularity
FROM datawarehouse
ORDER BY track_popularity DESC
LIMIT 10;

-- Average Popularity of Artists
SELECT artist_id, AVG(artist_popularity) AS avg_popularity
FROM datawarehouse
GROUP BY artist_id
ORDER BY avg_popularity DESC;

-- Tracks Released by a Specific Label
SELECT track_name, album_name, release_date
FROM datawarehouse
WHERE label = 'YourLabelName'
ORDER BY release_date DESC;

-- Count of Tracks by Genre
SELECT genre, COUNT(*) AS track_count
FROM datawarehouse
GROUP BY genre
ORDER BY track_count DESC;

-- Tracks Longer Than 5 Minutes
SELECT track_name, duration_sec
FROM datawarehouse
WHERE duration_sec > 300
ORDER BY duration_sec DESC;

-- Albums with Most Popular Tracks
SELECT album_name, track_name, track_popularity
FROM datawarehouse
ORDER BY track_popularity DESC
LIMIT 10;
