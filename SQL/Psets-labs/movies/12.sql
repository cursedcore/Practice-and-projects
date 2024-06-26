/*SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Johnny Depp" and movies.title
IN(SELECT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Helena Bonham Carter");*/

SELECT title from movies
 JOIN stars on stars.movie_id = movies.id
 JOIN people on people.id = stars.person_id
 WHERE people.name = "Johnny Depp" and movies.title
 IN(SELECT title from movies
 JOIN stars on stars.movie_id = movies.id
 JOIN people on people.id = stars.person_id
 WHERE people.name = "Helena Bonham Carter");