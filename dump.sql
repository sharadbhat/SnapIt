-- MySQL dump 10.13  Distrib 5.7.19, for Win64 (x86_64)
--
-- Host: localhost    Database: unsplash
-- ------------------------------------------------------
-- Server version	5.7.19-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `favourites`
--

DROP TABLE IF EXISTS `favourites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favourites` (
  `username` varchar(30) NOT NULL,
  `id` varchar(10) NOT NULL,
  PRIMARY KEY (`username`,`id`),
  KEY `id` (`id`),
  CONSTRAINT `favourites_ibfk_1` FOREIGN KEY (`username`) REFERENCES `users` (`username`),
  CONSTRAINT `favourites_ibfk_2` FOREIGN KEY (`id`) REFERENCES `images` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favourites`
--

LOCK TABLES `favourites` WRITE;
/*!40000 ALTER TABLE `favourites` DISABLE KEYS */;
INSERT INTO `favourites` VALUES ('sharad','MTA5Mz'),('sharad','MTI0OT'),('sharad','NTg0NT'),('sharad','ODkzOT');
/*!40000 ALTER TABLE `favourites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `images`
--

DROP TABLE IF EXISTS `images`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `images` (
  `id` varchar(10) NOT NULL,
  `title` text,
  `uploader` varchar(30) DEFAULT NULL,
  `likes` int(11) DEFAULT NULL,
  `tags` text,
  PRIMARY KEY (`id`),
  KEY `uploader` (`uploader`),
  CONSTRAINT `images_ibfk_1` FOREIGN KEY (`uploader`) REFERENCES `users` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `images`
--

LOCK TABLES `images` WRITE;
/*!40000 ALTER TABLE `images` DISABLE KEYS */;
INSERT INTO `images` VALUES ('MjAzOD','Top View of Forest','shaman',0,'forest drone green trees'),('Mjc1Mj','Circular Ceiling','sharad',0,'architecture circle lines'),('MjczOT','Faded Greens','mckinnon',0,'faded green leaf plant nature'),('MjEwOT','Soar','mohandas',0,'fog eagle trees blue mountain nature sky clouds'),('MjgwNz','Sharp Concentrics','mckinnon',0,'cactus green flower nature'),('MjIxOD','Patterns','alen',0,'pattern sharp brown diagonal'),('Mjk3Mz','Circular Staircase','shaman',0,'circle stairs dark lights architecture'),('MjQ0OD','Purple Windows','suman',0,'purple architecture dark night lights'),('MTA5Mz','Plane in a Forest','shaman',1,'aeroplane forest green jungle drone'),('MTc2Mz','Dark Purples','mckinnon',0,'dark purple flowers white macro'),('MTE2NT','Hard Waters','suman',0,'water waterfall brown drone'),('MTEzOT','Faded Flowers','alen',0,'faded flowers petals colorful'),('MTI0OT','Apocalyptic Beach','mattih',1,'beach water green sand drone view'),('MTM0OD','Hexagonal Windows','sharad',0,'hexagon architecture windows pattern'),('MTM2OD','Beach Rocks','max',0,'beach drone rocks waves blue brown water white'),('MTU2OT','Deserted City','mckinnon',0,'city buildings faded concrete jungle road'),('Mzg0Mz','White Squares','sig',0,'white architecture lines light squares'),('Mzk2NT','Rocky Waves','alen',0,'clear sky rocks brown blue waves'),('MzQwOD','Sandy Isthmus','max',0,'water blue drone dark beach'),('NDk2NT','Calm Waters','mattih',0,'water rocks mountains peaks'),('Njg4Mj','Escalator','mattih',0,'steps faded lights underground'),('NjMzNz','Airport Ceiling','sharad',0,'architecture color lines ceiling'),('NjU5MD','Red Building','sharad',0,'red architecture building futuristic dark lights'),('NTg0NT','Bridge Lines','suman',1,'lines white minimal concrete bridge'),('ODA3Nj','Macro Leaf','max',0,'macro leaf green light lines'),('ODcxNT','Cracks','swappnal',0,'cracks lines blue brown'),('ODkzOT','Boats on Water','swappnal',1,'boats water blue calm white');
/*!40000 ALTER TABLE `images` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `users` (
  `username` varchar(30) NOT NULL,
  `password` text,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES ('alen','pbkdf2:sha256:50000$QQpjD2Ww$2f63f869433813bf7035f0b5fb434737d93233cd968c930db7a31643c52c735d'),('mattih','pbkdf2:sha256:50000$EAz9vamW$c339b298d028856b861b3dc4d7cdc46683fdf82e54f5017475d8472fc0569975'),('max','pbkdf2:sha256:50000$4ABdZ7kQ$4b89a6c793ef5828300ed1956dc23aaf8170b7068c98f6bb8cab66e1a5b1d871'),('mckinnon','pbkdf2:sha256:50000$YfWxqNTJ$5a8281312a498cf1764640d6c64203efe4757a2ee4f513b17d1ab03a1cbcb111'),('mohandas','pbkdf2:sha256:50000$P2KisPuO$010fef57caa21c679b3d184582b9c17d3a2d49ead93bffee8a23c4d148526134'),('prajwal','pbkdf2:sha256:50000$6MbmK4Id$3c75e01574e1bba3e4a638388bbae6f0dae24adcce15a89b8d39c333bc954117'),('shaman','pbkdf2:sha256:50000$nViXHEj5$835ecd4861091b360d401b609917ef05966462301c3383be8de629efaa5bee6f'),('sharad','pbkdf2:sha256:50000$qLwjrBqo$ddcebe23e6d211efb5028eff49a0356e3ac7ae18dcb7068e8c58a188ae667987'),('sig','pbkdf2:sha256:50000$gIHEvRM0$c77e6a04548b02b169b3676c7aeb362008b4bf1bbcd16dd647d9e3996cbd69ef'),('suman','pbkdf2:sha256:50000$cZGiqWjy$cce490968d3dc68fe41f328d8b1e08d47570ea522efc76f766a86b2b85384eeb'),('swappnal','pbkdf2:sha256:50000$4ZYb54ZK$d5a2f63e5e2677a847606c4a3d07f78607eaa9358b618de4d011a1b2b25eabc6');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-10-21  1:59:29
