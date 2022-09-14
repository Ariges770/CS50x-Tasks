-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Searched crime_scene_reports table
SELECT * 
FROM crime_scene_reports 
WHERE year = 2021 
AND month = 7 
AND day = 28 
AND street = 'Humphrey Street';
/*Theft of the CS50 duck took place at 10:15am at the Humphrey Street bakery. 
Interviews were conducted today with three witnesses who were present at the time 
– each of their interview transcripts mentions the bakery. 

Result: Look at 3 interviews from 28/07/2021*/ 

-- Checked that days interviews
SELECT * 
FROM interviews 
WHERE day = 28 
AND month = 7 
AND year = 2021;
-- Ruth says to check bakery security logs for cars that left at around 10:15
-- Eugene knows of thief and states that thief took money from ATM on Leggett st prior to theft 
-- Raymond claims that the thief made a call whilst leaving the bakey

-- Check people who left Humprhey parking lot right after 10:15
SELECT * 
FROM bakery_security_logs 
WHERE day = 28 
AND month = 7 
AND year = 2021 
AND hour = 10 
AND minute > 15 
AND activity = 'exit';  

-- find names of people with these number plates
SELECT name 
FROM people 
WHERE license_plate 
IN (SELECT license_plate 
FROM bakery_security_logs 
WHERE day = 28 
AND month = 7 
AND year = 2021 
AND hour = 10 
AND minute > 15 
AND activity = 'exit');

-- Compare people who left 
SELECT * 
  FROM phone_calls 
 WHERE day = 28 
   AND month = 7 
   AND year = 2021 
   AND receiver 
    IN (SELECT phone_number 
  FROM people 
 WHERE license_plate 
    IN (SELECT license_plate 
  FROM bakery_security_logs 
 WHERE day = 28 
    AND month = 7 
    AND year = 2021 
    AND hour = 10
    AND minute > 15 
    AND activity = 'exit')); 
-- Result of this quiry is that Luca is the accomplace as he was called for a minute and left the carpark on that day

-- Find person on other end of the call
SELECT name FROM people WHERE phone_number = '(609) 555-5876';  

-- Atm transactions
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street';  



SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10;
SELECT name, people.license_plate FROM bakery_security_logs JOIN people ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10