-- a script that lists the tv shows in the given database
-- but displays null if tvshow doesn't have a genre
SELECT tv_shows.title, IFNULL(tv_show_genres.genre_id, 'NULL')
	FROM tv_shows
       	LEFT JOIN tv_show_genres 
	ON tv_shows.id = tv_show_genres.show_id 
	ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
