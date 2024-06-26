SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
JOIN ratings ON movies.id = ratings.movie_id
WHERE name = "Chadwick Boseman"
ORDER BY rating DESC LIMIT 5;

/*SELECT title from movies
join ratings on movies.id = ratings.movie_id
join movies on ratings.movie_id = movies.movie_id
join stars on movies.movie_id = stars.movie_id
join people on stars.person_id = people.id
where people.name = "Chadwick Boseman"
order by rating desc limit 5;*/