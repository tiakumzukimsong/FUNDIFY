-- MySQL dump 10.13  Distrib 8.0.32, for Linux (x86_64)
--
-- Host: localhost    Database: flask
-- ------------------------------------------------------
-- Server version	8.0.32-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `NGO_request_details`
--

DROP TABLE IF EXISTS `NGO_request_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NGO_request_details` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `NGO_Name` varchar(30) DEFAULT NULL,
  `Email` varchar(40) DEFAULT NULL,
  `Phone` varchar(13) DEFAULT NULL,
  `City` varchar(50) DEFAULT NULL,
  `NGO_registration_ID` varchar(25) DEFAULT NULL,
  `Amount` int DEFAULT NULL,
  `status` varchar(25) DEFAULT 'pending',
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NGO_request_details`
--

LOCK TABLES `NGO_request_details` WRITE;
/*!40000 ALTER TABLE `NGO_request_details` DISABLE KEYS */;
INSERT INTO `NGO_request_details` VALUES (1,'SS','s@s.c','12098','None','oqawiejf',50000,'pending'),(2,'qwer','johnimsong@gmail.com','8837030229','None','pojasdgf',50000,'Rejected'),(3,'TIA','tiakumzukimsong@gmail.com','8837030229','None','158493',10000,'Approved'),(4,'TT','tiakumzukimsong@gmail.com','883 703 0229','None','846215',10000,'pending'),(5,'AABB','abc@gmail.com','qwer','None','41253245',50000,'pending');
/*!40000 ALTER TABLE `NGO_request_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `NGO_signup_details`
--

DROP TABLE IF EXISTS `NGO_signup_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `NGO_signup_details` (
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `u_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `NGO_signup_details`
--

LOCK TABLES `NGO_signup_details` WRITE;
/*!40000 ALTER TABLE `NGO_signup_details` DISABLE KEYS */;
INSERT INTO `NGO_signup_details` VALUES ('johnimsong@gmail.com','asdf',NULL),('ok@gmail.com','asd',NULL),('abc@gmail.com','qwe','akangsha');
/*!40000 ALTER TABLE `NGO_signup_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `admin`
--

DROP TABLE IF EXISTS `admin`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `admin` (
  `ID` int NOT NULL AUTO_INCREMENT,
  `Password` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `admin`
--

LOCK TABLES `admin` WRITE;
/*!40000 ALTER TABLE `admin` DISABLE KEYS */;
INSERT INTO `admin` VALUES (1,'tiakumzuk'),(2,'tanay'),(3,'mahek');
/*!40000 ALTER TABLE `admin` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donor_signup_details`
--

DROP TABLE IF EXISTS `donor_signup_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donor_signup_details` (
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(25) DEFAULT NULL,
  `u_name` varchar(25) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donor_signup_details`
--

LOCK TABLES `donor_signup_details` WRITE;
/*!40000 ALTER TABLE `donor_signup_details` DISABLE KEYS */;
INSERT INTO `donor_signup_details` VALUES ('tiakumzukimsong@gmail.com','tia','tia');
/*!40000 ALTER TABLE `donor_signup_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `donors`
--

DROP TABLE IF EXISTS `donors`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `donors` (
  `first_name` varchar(25) DEFAULT NULL,
  `last_name` varchar(25) DEFAULT NULL,
  `amount` int DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `donors`
--

LOCK TABLES `donors` WRITE;
/*!40000 ALTER TABLE `donors` DISABLE KEYS */;
INSERT INTO `donors` VALUES ('Tia','kumzuk',10000),('pongen','imli',10000),('pongen','',10000),('adithya','shivshankar',50000),('chahak','bhartiya',20000),('new','user',20000),('tanay','goyal',25000);
/*!40000 ALTER TABLE `donors` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmer_details`
--

DROP TABLE IF EXISTS `farmer_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_details` (
  `SL_No` int unsigned NOT NULL AUTO_INCREMENT,
  `Name` text,
  `email` text,
  `Phone` varchar(13) DEFAULT NULL,
  `address` text,
  `farmer_id` text,
  `age` int DEFAULT NULL,
  `amount` int DEFAULT NULL,
  `status` varchar(25) DEFAULT 'pending',
  PRIMARY KEY (`SL_No`)
) ENGINE=InnoDB AUTO_INCREMENT=30 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_details`
--

LOCK TABLES `farmer_details` WRITE;
/*!40000 ALTER TABLE `farmer_details` DISABLE KEYS */;
INSERT INTO `farmer_details` VALUES (1,'tia','Tia@gmail.com','8837030229','burma camp','9813hgasd',NULL,NULL,'Approved'),(2,'Tiakumzuk','tiakumzukimsong@gmail.com','8837030229','JP NAGAR','qwertasdf1234vs',NULL,NULL,'Approved'),(3,'qwer','qwer@gma.com','qwer','qwer','qwer',NULL,NULL,'Approved'),(4,'None','None','None','None','None',NULL,NULL,'Rejected'),(5,'None','None','None','None','None',NULL,NULL,'Rejected'),(6,'None','None','None','None','None',NULL,NULL,'Rejected'),(7,'laura','la@gmail.com','1234567890','london','123pq',NULL,NULL,'pending'),(8,'q','q@q.c','q','q','q',NULL,NULL,'pending'),(9,'','','','','',NULL,NULL,'pending'),(10,'a','a','12','a','a',NULL,NULL,'Approved'),(11,'qwer','qewrt@as.c','123513123','asdf','aergf',NULL,NULL,'Approved'),(12,'qpoweri','qwer@qwer.q','12334','qwre','qwer',NULL,NULL,'pending'),(13,'ppp','pp@p.p','123','pp','pp',NULL,NULL,'pending'),(14,'km','km@k.c','123','qwer','qwer',NULL,NULL,'pending'),(15,'rqwer','qwer@qw.v','0124','qwdoi','oqierjg',NULL,NULL,'pending'),(16,'ppp','p@p.c','123','qwe','ppp',NULL,NULL,'pending'),(17,'ll','ll@l.c','123','ll','ll',NULL,NULL,'pending'),(18,'pp','pp@p.p','123','pp','pp',NULL,NULL,'pending'),(19,'paul','paul@gmial.com','8812340912','vithyathil','PP',NULL,NULL,'pending'),(20,'','','','','',NULL,NULL,'pending'),(21,'tia','tiakumzukimsong@gmail.com','8837030229','bangalore','poqgrope',NULL,NULL,'Approved'),(22,'tia','tiakumzukimsong@gmail.com','8837030229','asdf','qwerf',NULL,NULL,'Approved'),(23,'tia','harshvardhanthirani@gmail.com','8837030229','qwer','qwer',NULL,NULL,'Approved'),(24,'imli','imlikumla@gmail.com','8837030229','rqwer','qwer',NULL,NULL,'pending'),(25,'akangsha','akangsha@gmail.com','qepofg','qwerf','qwefqw',NULL,NULL,'pending'),(26,'Tiakumzuk','harshvardhanthirani@gmail.com','883 703 0229','qwe','qw',NULL,NULL,'Approved'),(27,'Interface24-tia','johnimsong@gmail.com','7085477015','bengaluru','124902u3it31r',21,25000,'pending'),(28,'adithya','tiakumzukimsong@gmail.com','66521039','jp nagar','r1039rjv',20,6000,'pending'),(29,'tanay','tanay.goyal@gmail.com','12345678','rajasthan','powsdr2231',20,5000,'pending');
/*!40000 ALTER TABLE `farmer_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `farmer_signup_details`
--

DROP TABLE IF EXISTS `farmer_signup_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `farmer_signup_details` (
  `Username` varchar(50) DEFAULT NULL,
  `Password` varchar(50) DEFAULT NULL,
  `u_name` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `farmer_signup_details`
--

LOCK TABLES `farmer_signup_details` WRITE;
/*!40000 ALTER TABLE `farmer_signup_details` DISABLE KEYS */;
INSERT INTO `farmer_signup_details` VALUES ('harshvardhanthirani@gmail.com','asd',NULL),('tiakumzukimsong@gmail.com','asdpvok',NULL),('johnimsong@gmail.com','qwer',NULL),('ok@gmail.com','qwer',NULL),('ok@gmail.com','qwer',NULL),('tiakumzuk@bca.christuniversity.in','q',NULL),('tiakumzuk@bca.christuniversity.in','q',NULL),('johnimsong@gmail.com12','q',NULL),('12@q.c','1234',NULL),('tiakumzuk@bca.christuniversity.in','qw',NULL),('harshvardhanthirani@gmail.com','qwe',NULL),('abc@gmail.com','qq',NULL),('abc@gmail.com','qq',NULL),('tiakumzukimsong@gmail.com','q',NULL),('harshvardhanthirani@gmail.com','asd',NULL),('p@p.c','qwer',NULL),('p@p.c','qwer',NULL),('harshvardhanthirani@gmail.com123','qwer',NULL),('a@ac.c','aaa',NULL),('abc@gmail.com','aa',NULL),('abc@gmail.com','aa',NULL),('abc@gmail.com','aa',NULL),('joohn@gmmm.ccc','pow',NULL),('tushar@gmail.com','tushar',NULL),('tanay.goyal@gmail.com','tanay',NULL),('makeh@kappor.com','mahek',NULL),('imlikumla@gmail.com','imli','imli'),('akangsha@gmail.com','akangsha','akangsha');
/*!40000 ALTER TABLE `farmer_signup_details` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-04-15 10:51:22
