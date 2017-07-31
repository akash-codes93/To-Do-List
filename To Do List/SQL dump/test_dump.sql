/*
SQLyog Community Edition- MySQL GUI v6.14
MySQL - 5.6.26 : Database - to_do_list
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `to_do_list`;

USE `to_do_list`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `task_information` */

DROP TABLE IF EXISTS `task_information`;

CREATE TABLE `task_information` (
  `task_id` int(11) NOT NULL AUTO_INCREMENT,
  `task_name` varchar(50) DEFAULT NULL,
  `task_description` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`task_id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=latin1;

/*Data for the table `task_information` */

insert  into `task_information`(`task_id`,`task_name`,`task_description`) values (24,'Complete homework','Complete the homework given in class and pack my work for tommorrow.'),(25,'Study computer','Study computer chapter number 10 and 11 for unit test exam\n'),(26,'Remind','Remind Atul to bring the notebook to the classroom tommorow.'),(27,'test task','This is a test task created to check the working of the api.');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
