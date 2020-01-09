CREATE DATABASE tobii;

USE tobii;

CREATE TABLE `gaze` (
  `id` varchar(255) DEFAULT NULL,
  `left_x` double DEFAULT NULL,
  `left_y` double DEFAULT NULL,
  `right_x` double DEFAULT NULL,
  `right_y` double DEFAULT NULL,
  `t` int(11) DEFAULT NULL,
  `t_order` int(11) DEFAULT NULL,
  `left_validity` int(11) DEFAULT NULL,
  `right_validity` int(11) DEFAULT NULL,
  `width` int(11) DEFAULT NULL,
  `height` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;