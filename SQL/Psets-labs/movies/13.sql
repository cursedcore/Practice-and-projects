/*SELECT DISTINCT name FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE movies.title IN(SELECT DISTINCT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Kevin Bacon" AND people.birth = 1958)
AND people.name != "Kevin Bacon";*/

 SELECT DISTINCT name FROM people
 JOIN stars ON people.id = stars.person_id
 JOIN movies ON stars.movie_id = movies.id
 WHERE movies.title IN(SELECT DISTINCT title FROM movies
 JOIN stars ON movies.id = stars.movie_id
 JOIN people ON stars.person_id = people.id
 WHERE people.name = "Kevin Bacon" AND people.birth = 1958)
 AND people.name != "Kevin Bacon";

/*SELECT DISTINCT people.name FROM movies
JOIN stars ON movies.id = stars.movie_id
JOIN people ON stars.person_id = people.id
WHERE movies.title IN(SELECT DISTINCT movies.title FROM people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
WHERE people.name = "Kevin Bacon" AND people.birth = 1958)
AND people.name != "Kevin Bacon";*/

