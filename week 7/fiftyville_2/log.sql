-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Searched crime_scene_reports table
SELECT * 
FROM crime_scene_reports 
WHERE year = 2021 
AND month = 7 
AND day = 28 
AND street = 'Humphrey Street';

-- Check interviews
SELECT * FROm interviews WHERE day = 28 AND month = 7 AND day = 28 AND transcript LIKE '%bakery%';


-- Check security footage
SELECT * FROM bakery_security_logs WHERE year = 2021 AND month = 7  AND day = 28 AND minute BETWEEN 15 AND 25 AND activity = 'exit';

-- Check Legget ATM
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw';

-- Check phone calls
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60;

-- Find person_name from each event
SELECT name FROM people WHERE license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7  AND day = 28 AND minute BETWEEN 15 AND 25 AND activity = 'exit');
SELECT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw');
SELECT name FROM people WHERE phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60);

-- Combine all 3 quiries
SELECT name FROM people JOIN bank_accounts ON people.id = bank_accounts.person_id WHERE account_number IN (SELECT account_number FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2021 AND atm_location = 'Leggett Street' AND transaction_type = 'withdraw') AND phone_number IN (SELECT caller FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2021 AND duration < 60) AND license_plate IN (SELECT license_plate FROM bakery_security_logs WHERE year = 2021 AND month = 7  AND day = 28 AND minute BETWEEN 15 AND 25 AND activity = 'exit');

-- Find Fiftyville airport id
SELECT id FROM airports WHERE city = 'Fiftyville';

-- Find earliest flight from Fiftyville
Select * FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour LIMIT 1;

-- Find all passengers on first flight
SELECT passport_number FROM passengers WHERE flight_id = (Select id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour LIMIT 1);
SELECT name FROM people WHERE passport_number IN (SELECT passport_number FROM passengers WHERE flight_id = (Select id FROM flights WHERE day = 29 AND month = 7 AND year = 2021 AND origin_airport_id = (SELECT id FROM airports WHERE city = 'Fiftyville') ORDER BY hour LIMIT 1));

-- Combine All for pieces of evidence to find thief
SELECT name 
FROM people JOIN bank_accounts 
ON people.id = bank_accounts.person_id 
    WHERE account_number 
    IN (SELECT account_number 
    FROM atm_transactions 
        WHERE day = 28 
        AND month = 7 
        AND year = 2021 
        AND atm_location = 'Leggett Street' 
        AND transaction_type = 'withdraw') 
  
    AND phone_number 
    IN (SELECT caller 
    FROM phone_calls 
        WHERE day = 28 
        AND month = 7 
        AND year = 2021 
        AND duration < 60) 
    
    AND license_plate 
    IN (SELECT license_plate 
    FROM bakery_security_logs 
        WHERE year = 2021 
        AND month = 7 
        AND day = 28 
        AND minute 
        BETWEEN 15 AND 25 
        AND activity = 'exit') 
        
    AND passport_number 
    IN (SELECT passport_number 
    FROM passengers 
        WHERE flight_id = (Select id 
        FROM flights 
            WHERE day = 29 
            AND month = 7 
            AND year = 2021 
            AND origin_airport_id = (SELECT id
            FROM airports 
                WHERE city = 'Fiftyville') 
                ORDER BY hour LIMIT 1));





-- Find Thief
SELECT name 
FROM people 
JOIN bank_accounts ON people.id = bank_accounts.person_id 
WHERE account_number 
    IN (SELECT account_number 
    FROM atm_transactions 
        WHERE day = 28 
        AND month = 7 
        AND year = 2021 
        AND atm_location = 'Leggett Street' 
        AND transaction_type = 'withdraw') 

    AND phone_number 
    IN (SELECT caller 
    FROM phone_calls 
        WHERE day = 28 
        AND month = 7 
        AND year = 2021 
        AND duration < 60) 
        
    AND license_plate 
    IN (SELECT license_plate 
    FROM bakery_security_logs 
        WHERE year = 2021 
        AND month = 7 
        AND day = 28 
        AND minute 
        BETWEEN 15 AND 25 
        AND activity = 'exit') 

    AND passport_number 
    IN (SELECT passport_number 
    FROM passengers 
        WHERE flight_id = (Select id 
        FROM flights 
            WHERE day = 29 
            AND month = 7 
            AND year = 2021 
            AND origin_airport_id = (SELECT id 
            FROM airports 
                WHERE city = 'Fiftyville')
        ORDER BY hour 
        LIMIT 1));

-- Escape city
SELECT city 
    FROM airports 
    JOIN flights ON airports.id = destination_airport_id 
    JOIN passengers ON flights.id = passengers.flight_id 
        WHERE passport_number = (SELECT passport_number 
        FROM people 
        JOIN bank_accounts ON people.id = bank_accounts.person_id 
            WHERE account_number IN (SELECT account_number 
            FROM atm_transactions 
                WHERE day = 28 
                AND month = 7 
                AND year = 2021 
                AND atm_location = 'Leggett Street' 
                AND transaction_type = 'withdraw') 
                
            AND phone_number IN (SELECT caller 
            FROM phone_calls 
                WHERE day = 28 
                AND month = 7 
                AND year = 2021 
                AND duration < 60) 
                
            AND license_plate IN (SELECT license_plate 
            FROM bakery_security_logs 
                WHERE year = 2021 
                AND month = 7 
                AND day = 28 
                AND minute BETWEEN 15 AND 25 
                AND activity = 'exit') 
                
            AND passport_number IN (SELECT passport_number 
            FROM passengers 
                WHERE flight_id = (Select id 
                FROM flights 
                    WHERE day = 29 
                    AND month = 7 
                    AND year = 2021 
                    AND origin_airport_id = (SELECT id 
                    FROM airports 
                        WHERE city = 'Fiftyville') 
                    ORDER BY hour 
                    LIMIT 1)));

-- Accomplice
SELECT name 
    FROM people 
    JOIN phone_calls ON phone_calls.receiver = people.phone_number 
        WHERE day = 28 
        AND month = 7 
        AND year = 2021 
        AND duration < 60 
        AND caller = (SELECT phone_number 
        FROM people 
        JOIN bank_accounts ON people.id = bank_accounts.person_id     
            WHERE account_number IN (SELECT account_number 
            FROM atm_transactions 
                WHERE day = 28 
                AND month = 7 
                AND year = 2021 
                AND atm_location = 'Leggett Street' 
                AND transaction_type = 'withdraw') 
                
        AND phone_number IN (SELECT caller 
        FROM phone_calls 
            WHERE day = 28 
            AND month = 7 
            AND year = 2021 
            AND duration < 60) 
            
        AND license_plate IN (SELECT license_plate 
        FROM bakery_security_logs 
            WHERE year = 2021 
            AND month = 7 
            AND day = 28 
            AND minute BETWEEN 15 AND 25 
            AND activity = 'exit') 
            
        AND passport_number IN (SELECT passport_number 
        FROM passengers 
            WHERE flight_id = (Select id 
            FROM flights 
                WHERE day = 29 
                AND month = 7 
                AND year = 2021 
                AND origin_airport_id = (SELECT id 
                FROM airports 
                    WHERE city = 'Fiftyville') 
                ORDER BY hour 
                LIMIT 1)));
