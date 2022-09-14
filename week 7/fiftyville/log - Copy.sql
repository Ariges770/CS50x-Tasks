-- Searched crime_scene_reports table
SELECT * 
FROM crime_scene_reports 
WHERE year = 2021 
AND month = 7 
AND day = 28 
AND street = 'Humphrey Street';

-- Find the plates of the cars leaving after 10.15
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15;


SELECT name, people.license_plate FROM bakery_security_logs JOIN people ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10;

-- 3 quiries to find the person who called/used the atm/left carpark
SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street';
SELECT people.id FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE day = 28 AND month = 7 AND year = 2021;
SELECT people.license_plate FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15 AND activity = 'exit';

-- Combine both
SELECT people.id, passport_number, name FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60 AND people.id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street') AND people.license_plate IN (SELECT people.license_plate FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15 AND activity = 'exit');

-- Find list of passengers who flew next day morning
SELECT people.name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON flights.id = passengers.flight_id WHERE year = 2021 AND month = 7 AND day = 29;

-- Combine atm, caller and driver with passengers
SELECT people.name FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON flights.id = passengers.flight_id WHERE year = 2021 AND month = 7 AND day = 29 AND hour < 12 AND people.id IN (SELECT people.id FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60 AND people.id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street') AND people.license_plate IN (SELECT people.license_plate FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15 AND activity = 'exit'));

-- Check numbers of people flying against calls and receives
SELECT name, phone_number FROM people WHERE id IN (SELECT people.id FROM people JOIN passengers ON people.passport_number = passengers.passport_number JOIN flights ON flights.id = passengers.flight_id WHERE year = 2021 AND month = 7 AND day = 29 AND hour < 12 AND people.id IN (SELECT people.id FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60 AND people.id IN (SELECT person_id FROM atm_transactions JOIN bank_accounts ON bank_accounts.account_number = atm_transactions.account_number WHERE year = 2021 AND month = 7 AND day = 28 AND atm_location = 'Leggett Street') AND people.license_plate IN (SELECT people.license_plate FROM people JOIN bakery_security_logs ON people.license_plate = bakery_security_logs.license_plate WHERE day = 28 AND month = 7 AND year = 2021 AND hour = 10 AND minute > 15 AND activity = 'exit'))); 

SELECT people.name, caller, receiver FROM people JOIN phone_calls ON phone_calls.caller = people.phone_number WHERE day = 28 AND month = 7 AND year = 2021 AND people.name = 'Bruce' AND people.name = 'Taylor';

