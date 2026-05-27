-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: May 26, 2026 at 11:07 PM
-- Server version: 10.4.32-MariaDB
-- PHP Version: 8.0.30

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `payroll`
--

-- --------------------------------------------------------

--
-- Table structure for table `attendance`
--

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `month` varchar(20) DEFAULT NULL,
  `working_days` int(11) DEFAULT NULL,
  `present_days` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `attendance`
--

INSERT INTO `attendance` (`attendance_id`, `emp_id`, `month`, `working_days`, `present_days`) VALUES
(1, 101, 'Jan', 26, 24),
(2, 102, 'Jan', 26, 22),
(3, 103, 'Jan', 26, 25),
(4, 104, 'Jan', 26, 20),
(5, 105, 'Jan', 26, 23),
(6, 106, 'Jan', 26, 21),
(7, 107, 'may', 30, 28);

-- --------------------------------------------------------

--
-- Table structure for table `department`
--

CREATE TABLE `department` (
  `dept_id` int(11) NOT NULL,
  `dept_name` varchar(50) DEFAULT NULL,
  `location` varchar(50) DEFAULT NULL,
  `manager_name` varchar(50) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `department`
--

INSERT INTO `department` (`dept_id`, `dept_name`, `location`, `manager_name`, `contact_no`) VALUES
(1, 'HR', 'Delhi', 'Anita Sharma', '9876543210'),
(2, 'IT', 'Noida', 'Rahul Verma', '9876501234'),
(3, 'Finance', 'Gurgaon', 'Suresh Mehta', '9123456789'),
(4, 'Marketing', 'Delhi', 'Neha Kapoor', '9988776655'),
(5, 'Sales', 'Noida', 'Amit Singh', '9090909090');

-- --------------------------------------------------------

--
-- Table structure for table `employee`
--

CREATE TABLE `employee` (
  `emp_id` int(11) NOT NULL,
  `emp_name` varchar(50) DEFAULT NULL,
  `gender` varchar(10) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `dept_id` int(11) DEFAULT NULL,
  `user_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `employee`
--

INSERT INTO `employee` (`emp_id`, `emp_name`, `gender`, `dob`, `dept_id`, `user_id`) VALUES
(101, 'Riya', 'Female', '2003-05-12', 1, 1),
(102, 'Aman', 'Male', '2002-08-21', 2, 2),
(103, 'Kunal', 'Male', '2001-03-15', 3, 3),
(104, 'Sneha', 'Female', '2003-11-10', 2, 2),
(105, 'Arjun', 'Male', '2002-07-19', 4, 4),
(106, 'Priya', 'Female', '2001-09-25', 5, 5),
(107, 'kriti', 'female', '2005-05-10', 1, NULL),
(201, 'kat', 'female', '2005-01-01', 2, NULL);

-- --------------------------------------------------------

--
-- Table structure for table `payroll`
--

CREATE TABLE `payroll` (
  `payroll_id` int(11) NOT NULL,
  `emp_id` int(11) DEFAULT NULL,
  `basic_salary` decimal(10,2) DEFAULT NULL,
  `bonus` decimal(10,2) DEFAULT NULL,
  `net_salary` decimal(10,2) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `payroll`
--

INSERT INTO `payroll` (`payroll_id`, `emp_id`, `basic_salary`, `bonus`, `net_salary`) VALUES
(1, 101, 30000.00, 2000.00, 32000.00),
(2, 102, 35000.00, 3000.00, 38000.00),
(3, 103, 40000.00, 2500.00, 42500.00),
(4, 104, 28000.00, 1500.00, 29500.00),
(5, 105, 32000.00, 2000.00, 34000.00),
(6, 106, 30000.00, 1000.00, 31000.00),
(7, 107, 50000.00, 2000.00, 48666.67);

-- --------------------------------------------------------

--
-- Table structure for table `users`
--

CREATE TABLE `users` (
  `user_id` int(11) NOT NULL,
  `username` varchar(50) DEFAULT NULL,
  `password` varchar(50) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  `contact_no` varchar(15) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `users`
--

INSERT INTO `users` (`user_id`, `username`, `password`, `role`, `contact_no`) VALUES
(1, 'admin_hr', '123', 'HR', '9999999991'),
(2, 'admin_it', '123', 'IT', '9999999992'),
(3, 'admin_fin', '123', 'Finance', '9999999993'),
(4, 'admin_mkt', '123', 'Marketing', '9999999994'),
(5, 'admin_sales', '123', 'Sales', '9999999995');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `attendance`
--
ALTER TABLE `attendance`
  ADD PRIMARY KEY (`attendance_id`),
  ADD KEY `emp_id` (`emp_id`);

--
-- Indexes for table `department`
--
ALTER TABLE `department`
  ADD PRIMARY KEY (`dept_id`);

--
-- Indexes for table `employee`
--
ALTER TABLE `employee`
  ADD PRIMARY KEY (`emp_id`),
  ADD KEY `dept_id` (`dept_id`),
  ADD KEY `user_id` (`user_id`);

--
-- Indexes for table `payroll`
--
ALTER TABLE `payroll`
  ADD PRIMARY KEY (`payroll_id`),
  ADD KEY `emp_id` (`emp_id`);

--
-- Indexes for table `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`user_id`);

--
-- Constraints for dumped tables
--

--
-- Constraints for table `attendance`
--
ALTER TABLE `attendance`
  ADD CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`);

--
-- Constraints for table `employee`
--
ALTER TABLE `employee`
  ADD CONSTRAINT `employee_ibfk_1` FOREIGN KEY (`dept_id`) REFERENCES `department` (`dept_id`),
  ADD CONSTRAINT `employee_ibfk_2` FOREIGN KEY (`user_id`) REFERENCES `users` (`user_id`);

--
-- Constraints for table `payroll`
--
ALTER TABLE `payroll`
  ADD CONSTRAINT `payroll_ibfk_1` FOREIGN KEY (`emp_id`) REFERENCES `employee` (`emp_id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
