/* Keep a log of any SQL queries you execute as you solve the mystery.
--Step 1: get some information about the crime.
-- Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time – each of their interview transcripts mentions the bakery.
--SELECT * FROM "people" WHERE name = "Bruce";
--Robin
--id: 864400 Phone_number: (375) 555-8161 passport_number:	NULL	4V16VO0*/
SELECT description FROM crime_scene_reports
WHERE month = 7 AND day = 28
AND street = "Humphrey Street";
--Step 2: Find any sus
SELECT license_plate from bakery_security_logs
WHERE month = 7 AND day = 28
AND hour <= 10 AND minute <= 15;
--Bruce
--id: 686048 phone_number: (367) 555-5533  passport_number: 5773159633 license_plate: 94KL13X
SELECT * FROM people
JOIN bakery_security_logs ON bakery_security_logs.license_plate = people.license_plate
WHERE bakery_security_logs.license_plate = "94KL13X";
/*--Then I searched in the interviews with the witnesses and I took the information given
--They said there was a call that lasted less than a minute, and I looked for calls in that moment that lasted less than the minute
--When I found the call, I saw the number of the person who might be the accomplice, I found that the name is Robin, and this person does not have passport
--I realized that Bruce made that call and I checked if he flied in the next day, because someone said that the ticket for the flight
--was for the next day. When I found in the airport the flight that bruce took, I looked the destination of that flight, and it was on
--New York City
--SELECT * FROM "passengers" WHERE passport_number= 5773159633*/

