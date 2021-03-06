CREATE DATABASE IF NOT EXISTS student;
USE student;

CREATE TABLE IF NOT EXISTS `student` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`name` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
);

INSERT INTO `student` (`id`, `name`, `password`, `email`) VALUES (1, 'Admin', 'goodOne', 'admin@gmail.com');
INSERT INTO `student` (`id`, `name`, `password`, `email`) VALUES (2, 'John', 'badOne', 'me@gmail.com');