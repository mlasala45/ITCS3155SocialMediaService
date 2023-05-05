-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: socialmedia_service
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user_credentials`
--

DROP TABLE IF EXISTS `user_credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_credentials` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(36) NOT NULL,
  `password` varchar(20) NOT NULL,
  PRIMARY KEY (`uid`),
  UNIQUE KEY `uid_UNIQUE` (`uid`),
  UNIQUE KEY `username_UNIQUE` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_credentials`
--

LOCK TABLES `user_credentials` WRITE;
/*!40000 ALTER TABLE `user_credentials` DISABLE KEYS */;
INSERT INTO `user_credentials` VALUES (1,'sysadmin','password'),(2,'elonmusk','password'),(3,'Cristiano','password'),(4,'realDonaldTrump','password'),(5,'NASA','password');
/*!40000 ALTER TABLE `user_credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_posts`
--

DROP TABLE IF EXISTS `user_posts`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_posts` (
  `uid` int NOT NULL AUTO_INCREMENT,
  `user` int NOT NULL,
  `timePosted` datetime NOT NULL,
  `text` varchar(280) NOT NULL,
  PRIMARY KEY (`uid`)
) ENGINE=InnoDB AUTO_INCREMENT=35 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_posts`
--

LOCK TABLES `user_posts` WRITE;
/*!40000 ALTER TABLE `user_posts` DISABLE KEYS */;
INSERT INTO `user_posts` VALUES (14,2,'2023-04-17 12:36:13','Anarcho-Capitalism is not a political ideology. It is a description of the human animal.'),(15,2,'2023-04-16 16:01:35','Wyden is threatening to subpoena Twitter for info on Trump’s secret deal with Putin'),(16,2,'2023-04-27 16:41:55','Is Twitter ready to ban Alex Jones?'),(17,2,'2023-04-26 18:39:28','Starlink balloons go into orbit, then descend to top of stratosphere, where they beam down internet from space, providing reliable, fast internet to almost anyone on Earth, affordably.'),(18,2,'2023-04-07 13:42:05','We’re going to start our own country'),(19,2,'2023-04-09 01:27:39','In 2 years, I’ll finally be a billionaire'),(20,2,'2023-04-16 04:33:04','My entire life is about science & tech. I will be the greatest science president, ever. And I will be the best president, ever.'),(21,2,'2023-04-29 08:19:45','I never wanted Twitter to be a business.\n\nBut someone needs to make money off social media, so I’ll be building that business.\n\n... And I promise to be awesome at it.'),(22,3,'2023-04-11 13:44:05','A vida não é um balneário. É uma montanha e uma montanha tão grande que você pode ouvir o ar e ouvir o sonho. A montanha que você tem'),(23,3,'2023-04-09 05:48:38','Another historic night! Unforgettable ?'),(24,3,'2023-04-21 23:45:49','100 trajetórios!\n100 conquistas do nosso clube, 100 conquistas do nosso espírito, 100 conquistas de melhor carinho, 100 conquistas de valor e ética, 100 conquistas de amor, 100 conquistas de'),(25,4,'2023-04-20 19:19:26','Red Wave in 2018. Now, BIG RED WAVE in 2020.'),(26,4,'2023-04-26 04:02:00','Healthy young child goes to doctor, gets pumped with massive shot of many vaccines, doesn’t feel good and changes – AUTISM. Many such cases!'),(27,4,'2023-04-26 15:58:50','Sorry losers and haters, but my I.Q. is one of the highest -and you all know it! Please don’t feel so stupid or insecure,it’s not your fault'),(28,4,'2023-04-14 03:44:52','Windmills are the greatest threat in the US to both bald and golden eagles. Media claims fictional ‘global warming’ is worse.'),(29,4,'2023-04-29 06:36:40','The Miss Universe Pageant will be broadcast live from MOSCOW, RUSSIA on November 9th. A big deal that will bring our countries together!'),(30,4,'2023-04-18 07:27:48','We should have gotten more of the oil in Syria, and we should have gotten more of the oil in Iraq. Dumb leaders.'),(31,5,'2023-04-05 23:59:30','Today\'s spacewalk is officially underway! The two astronauts have switched their spacesuits to battery power. Steve Bowen of \n@NASA_Astronauts\n and \n@Astro_Alneyadi\n will route power cables to prepare for future power system upgrades outside the \n@Space_Station\n.'),(32,5,'2023-04-06 12:28:28','People travel to national parks every year to be surrounded by the beauty of nature. #NationalParkWeek\n\nNational parks seen from space are just as beautiful. Maybe more? \n\nYou be the judge. https://go.nasa.gov/4449VtO'),(33,5,'2023-04-10 06:22:35','What\'s your favorite \n@NASAHubble\n image? http://bit.ly/3NauIG3\n\nLaunched 33 years ago today, the orbiting telescope captured this image of a nebula where stars are born -- 960 light-years away. http://go.nasa.gov/3VizSlr'),(34,5,'2023-04-19 16:55:09','NOW: \n@NASAEarth\n and \n@CenterForAstro\n scientists are answering questions on Reddit about TEMPO, a new space-based instrument that will revolutionize our understanding of air quality.\n \nWant to learn more? Ask your own Qs on our AMA.');
/*!40000 ALTER TABLE `user_posts` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-30 19:21:27
