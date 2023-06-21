-- MySQL dump 10.13  Distrib 8.0.28, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: base_poderjudicial
-- ------------------------------------------------------
-- Server version	8.0.28

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
-- Table structure for table `categorias`
--

DROP TABLE IF EXISTS `categorias`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `categorias` (
  `ID_categoria` int NOT NULL AUTO_INCREMENT,
  `categoria` varchar(90) NOT NULL,
  PRIMARY KEY (`ID_categoria`),
  UNIQUE KEY `ID_Categorias_UNIQUE` (`ID_categoria`),
  UNIQUE KEY `Categoria_UNIQUE` (`categoria`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `categorias`
--

LOCK TABLES `categorias` WRITE;
/*!40000 ALTER TABLE `categorias` DISABLE KEYS */;
/*!40000 ALTER TABLE `categorias` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `normativas`
--

DROP TABLE IF EXISTS `normativas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `normativas` (
  `ID_nroregistro` int NOT NULL AUTO_INCREMENT,
  `tipo_normativa` varchar(50) NOT NULL,
  `nro_normativa` int NOT NULL,
  `fecha_sancion` date NOT NULL,
  `descripcion` text NOT NULL,
  `jurisdiccion` varchar(60) NOT NULL,
  `palabra_clave` varchar(250) NOT NULL,
  `ID_categoria` int NOT NULL,
  `ID_organo_legislativo` int NOT NULL,
  PRIMARY KEY (`ID_nroregistro`),
  UNIQUE KEY `ID_nroNormativas_UNIQUE` (`ID_nroregistro`),
  UNIQUE KEY `nro_normativa_UNIQUE` (`nro_normativa`),
  UNIQUE KEY `palabra_clave_UNIQUE` (`palabra_clave`),
  KEY `ID_categoria_idx` (`ID_categoria`),
  KEY `ID_organo_legislativo_idx` (`ID_organo_legislativo`),
  CONSTRAINT `ID_categoria` FOREIGN KEY (`ID_categoria`) REFERENCES `categorias` (`ID_categoria`),
  CONSTRAINT `ID_organo_legislativo` FOREIGN KEY (`ID_organo_legislativo`) REFERENCES `organoslegislativos` (`ID_organo_legislativo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `normativas`
--

LOCK TABLES `normativas` WRITE;
/*!40000 ALTER TABLE `normativas` DISABLE KEYS */;
/*!40000 ALTER TABLE `normativas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `organoslegislativos`
--

DROP TABLE IF EXISTS `organoslegislativos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `organoslegislativos` (
  `ID_organo_legislativo` int NOT NULL AUTO_INCREMENT,
  `organo_legislativo` varchar(250) NOT NULL,
  PRIMARY KEY (`ID_organo_legislativo`),
  UNIQUE KEY `ID_organo_legislativo_UNIQUE` (`ID_organo_legislativo`),
  UNIQUE KEY `Organo_Legislativo_UNIQUE` (`organo_legislativo`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `organoslegislativos`
--

LOCK TABLES `organoslegislativos` WRITE;
/*!40000 ALTER TABLE `organoslegislativos` DISABLE KEYS */;
/*!40000 ALTER TABLE `organoslegislativos` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-20  7:26:37
