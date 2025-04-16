-- Step 1: Create the database
CREATE DATABASE  Travel_Planner;

-- Step 2: Use the database
USE Travel_Planner;

-- Step 3: Create the bookings table
CREATE TABLE bookings (
    user_id INT,
    flight_id INT,
    hotel_id INT,
    activity_id INT,
    booking_date DATE
);

-- Step 4: Insert dummy data
INSERT INTO bookings (user_id, flight_id, hotel_id, activity_id, booking_date) VALUES
(1, 101, 201, 301, '2025-04-10'),
(2, 102, 202, 302, '2025-04-11'),
(3, 103, 203, 303, '2025-04-12'),
(4, 104, 204, 304, '2025-04-13'),
(5, 105, 205, 305, '2025-04-14');
