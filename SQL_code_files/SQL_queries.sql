-- JOIN query of artists and albums, all of Taylor Swifts albums.

SELECT albums.id, 
    albums.title
FROM albums
    JOIN artists
    ON albums.artist_id = artists.id
WHERE artists.name = 'Taylor Swift';

-- JOIN query of artista and albums to find the only Pixies album from 1988.

SELECT albums.id, 
    albums.title
FROM albums
    JOIN artists
    ON albums.artist_id = artists.id
WHERE artists.name = 'Pixies' AND albums.release_year = 1988;

-- JOIN query to find album_id and title of albums from Nina Simone after 1975.

SELECT albums.id AS album_id,
    albums.title
FROM albums
    JOIN artists
    ON albums.artist_id = artists.id
WHERE artists.name = 'Nina Simone' AND albums.release_year > 1975;