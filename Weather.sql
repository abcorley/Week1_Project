-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: Weather
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `Boston`
--

DROP TABLE IF EXISTS `Boston`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Boston` (
  `Date` text DEFAULT NULL,
  `Temp` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Boston`
--

LOCK TABLES `Boston` WRITE;
/*!40000 ALTER TABLE `Boston` DISABLE KEYS */;
INSERT INTO `Boston` VALUES ('2021-07-21',74);
/*!40000 ALTER TABLE `Boston` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `Houston`
--

DROP TABLE IF EXISTS `Houston`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Houston` (
  `Date` text DEFAULT NULL,
  `Temp` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Houston`
--

LOCK TABLES `Houston` WRITE;
/*!40000 ALTER TABLE `Houston` DISABLE KEYS */;
INSERT INTO `Houston` VALUES ('2021-07-06',80.3),('2021-07-07',78.2),('2021-07-08',80.3),('2021-07-09',80.6),('2021-07-10',82.6),('2021-07-11',83.5),('2021-07-12',83),('2021-07-13',84.2),('2021-07-14',85.2),('2021-07-15',83.7),('2021-07-16',85.6),('2021-07-17',86.3),('2021-07-18',85.9),('2021-07-19',85.8),('2021-07-20',86.8),('2021-07-21',84.8);
/*!40000 ALTER TABLE `Houston` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-07  2:48:53
