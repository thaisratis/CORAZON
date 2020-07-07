-- MySQL dump 10.13  Distrib 5.7.22, for Linux (x86_64)
--
-- Host: localhost    Database: meanshift
-- ------------------------------------------------------
-- Server version	5.7.22-0ubuntu18.04.1

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
-- Table structure for table `Users`
--

DROP TABLE IF EXISTS `Users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `Users` (
  `user` varchar(255) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  KEY `useridx` (`user`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `Users`
--

LOCK TABLES `Users` WRITE;
/*!40000 ALTER TABLE `Users` DISABLE KEYS */;
INSERT INTO `Users` VALUES ('miguelito','$pbkdf2-sha256$200000$ACAkhFDKeU/pPac0Zizl3FvLeY9xDkGolQ$f8hh2jcKygJbrZ1wJqB3KP39z78aHpuhunxx51Fx8YA'),('viniciusmaracaja','$pbkdf2-sha256$200000$WwuhtNZaKwVgzJnT.v./lxLC2BujNOYcow$.2cM3PV8BkhNio46hTp0NaKA3lbVlz1ZgxOryYT8BQU'),('thais','$pbkdf2-sha256$200000$vXeOEYIwJuT8X2tN6X1PKeV8z3mvtRZC6A$RA7lXaqSF7wxcvmfjKWxSf9G5hI5O5aY08FkNqHEa0I'),('teste','$pbkdf2-sha256$200000$YGyN8b73fg9ByHmvVQoBAAAAIKQUopTSWg$lKsHvkpwUrqqtxh3LD6ppZxxJ8S/zaq/AqbOV4J563s'),('test','$pbkdf2-sha256$200000$2xujtPb.H0PoHSPEOOfcO2dsrfVeyxkDYA$TJSmNhD1NwCWsxSBV1HdWJQHa9VpzSXTh3Uzjn4Qjlk');
/*!40000 ALTER TABLE `Users` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `alljobs`
--

DROP TABLE IF EXISTS `alljobs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `alljobs` (
  `pid` int(11) NOT NULL AUTO_INCREMENT,
  `id` int(11) DEFAULT NULL,
  `tipo` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=MyISAM AUTO_INCREMENT=506 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `alljobs`
--

LOCK TABLES `alljobs` WRITE;
/*!40000 ALTER TABLE `alljobs` DISABLE KEYS */;
INSERT INTO `alljobs` VALUES (200,411,'MeanShift'),(201,412,'MeanShift'),(202,413,'MeanShift'),(203,414,'MeanShift'),(204,415,'MeanShift'),(205,416,'MeanShift'),(206,417,'MeanShift'),(207,418,'MeanShift'),(208,419,'MeanShift'),(209,420,'MeanShift'),(210,421,'MeanShift'),(211,422,'MeanShift'),(212,423,'MeanShift'),(213,97,'KMeans'),(214,98,'KMeans'),(215,99,'KMeans'),(216,424,'MeanShift'),(217,425,'MeanShift'),(218,426,'MeanShift'),(219,427,'MeanShift'),(220,428,'MeanShift'),(221,429,'MeanShift'),(222,430,'MeanShift'),(223,431,'MeanShift'),(224,432,'MeanShift'),(225,433,'MeanShift'),(226,434,'MeanShift'),(227,435,'MeanShift'),(228,436,'MeanShift'),(229,437,'MeanShift'),(230,438,'MeanShift'),(231,439,'MeanShift'),(232,440,'MeanShift'),(233,441,'MeanShift'),(234,442,'MeanShift'),(235,443,'MeanShift'),(236,444,'MeanShift'),(237,445,'MeanShift'),(238,446,'MeanShift'),(239,447,'MeanShift'),(240,448,'MeanShift'),(241,449,'MeanShift'),(242,450,'MeanShift'),(243,451,'MeanShift'),(244,452,'MeanShift'),(245,453,'MeanShift'),(246,454,'MeanShift'),(247,100,'KMeans'),(248,455,'MeanShift'),(249,456,'MeanShift'),(250,457,'MeanShift'),(251,458,'MeanShift'),(252,459,'MeanShift'),(253,460,'MeanShift'),(254,101,'KMeans'),(255,102,'KMeans'),(256,103,'KMeans'),(257,461,'MeanShift'),(258,462,'MeanShift'),(259,463,'MeanShift'),(260,104,'KMeans'),(261,105,'KMeans'),(262,106,'KMeans'),(263,107,'KMeans'),(264,464,'MeanShift'),(265,108,'KMeans'),(266,109,'KMeans'),(267,110,'KMeans'),(268,465,'MeanShift'),(269,466,'MeanShift'),(270,467,'MeanShift'),(271,111,'KMeans'),(272,112,'KMeans'),(273,468,'MeanShift'),(274,469,'MeanShift'),(275,113,'KMeans'),(276,470,'MeanShift'),(277,471,'MeanShift'),(278,472,'MeanShift'),(279,473,'MeanShift'),(280,114,'KMeans'),(281,1,'hierarchical'),(282,115,'KMeans'),(283,116,'KMeans'),(284,2,'hierarchical'),(285,3,'hierarchical'),(286,4,'hierarchical'),(287,5,'hierarchical'),(288,6,'hierarchical'),(289,7,'hierarchical'),(290,8,'hierarchical'),(291,9,'hierarchical'),(292,10,'hierarchical'),(293,11,'hierarchical'),(294,12,'hierarchical'),(295,13,'hierarchical'),(296,14,'hierarchical'),(297,15,'hierarchical'),(298,16,'hierarchical'),(299,17,'hierarchical'),(300,18,'hierarchical'),(301,19,'hierarchical'),(302,20,'hierarchical'),(303,21,'hierarchical'),(304,22,'hierarchical'),(305,23,'hierarchical'),(306,24,'hierarchical'),(307,25,'hierarchical'),(308,26,'hierarchical'),(309,27,'hierarchical'),(310,28,'hierarchical'),(311,29,'hierarchical'),(312,30,'hierarchical'),(313,31,'hierarchical'),(314,32,'hierarchical'),(315,33,'hierarchical'),(316,34,'hierarchical'),(317,35,'hierarchical'),(318,36,'hierarchical'),(319,37,'hierarchical'),(320,38,'hierarchical'),(321,39,'hierarchical'),(322,40,'hierarchical'),(323,41,'hierarchical'),(324,42,'hierarchical'),(325,43,'hierarchical'),(326,44,'hierarchical'),(327,45,'hierarchical'),(328,46,'hierarchical'),(329,47,'hierarchical'),(330,48,'hierarchical'),(331,49,'hierarchical'),(332,117,'KMeans'),(333,118,'KMeans'),(334,50,'hierarchical'),(335,119,'KMeans'),(336,51,'hierarchical'),(337,52,'hierarchical'),(338,53,'hierarchical'),(339,474,'MeanShift'),(340,54,'hierarchical'),(341,55,'hierarchical'),(342,56,'hierarchical'),(343,57,'hierarchical'),(344,58,'hierarchical'),(345,59,'hierarchical'),(346,60,'hierarchical'),(347,61,'hierarchical'),(348,475,'MeanShift'),(349,476,'MeanShift'),(350,120,'KMeans'),(351,121,'KMeans'),(352,62,'hierarchical'),(353,477,'MeanShift'),(354,478,'MeanShift'),(355,479,'MeanShift'),(356,480,'MeanShift'),(357,481,'MeanShift'),(358,482,'MeanShift'),(359,483,'MeanShift'),(360,484,'MeanShift'),(361,485,'MeanShift'),(362,486,'MeanShift'),(363,487,'MeanShift'),(364,488,'MeanShift'),(365,489,'MeanShift'),(366,490,'MeanShift'),(367,491,'MeanShift'),(368,492,'MeanShift'),(369,493,'MeanShift'),(370,494,'MeanShift'),(371,495,'MeanShift'),(372,496,'MeanShift'),(373,497,'MeanShift'),(374,498,'MeanShift'),(375,499,'MeanShift'),(376,500,'MeanShift'),(377,501,'MeanShift'),(378,502,'MeanShift'),(379,503,'MeanShift'),(380,504,'MeanShift'),(381,505,'MeanShift'),(382,506,'MeanShift'),(383,507,'MeanShift'),(384,508,'MeanShift'),(385,509,'MeanShift'),(386,122,'KMeans'),(387,510,'MeanShift'),(388,511,'MeanShift'),(389,512,'MeanShift'),(390,513,'MeanShift'),(391,514,'MeanShift'),(392,515,'MeanShift'),(393,516,'MeanShift'),(394,517,'MeanShift'),(395,518,'MeanShift'),(396,519,'MeanShift'),(397,520,'MeanShift'),(398,521,'MeanShift'),(399,123,'KMeans'),(400,124,'KMeans'),(401,63,'hierarchical'),(402,64,'hierarchical'),(403,522,'MeanShift'),(404,65,'hierarchical'),(405,523,'MeanShift'),(406,524,'MeanShift'),(407,525,'MeanShift'),(408,526,'MeanShift'),(409,527,'MeanShift'),(410,528,'MeanShift'),(411,529,'MeanShift'),(412,530,'MeanShift'),(413,125,'KMeans'),(414,66,'hierarchical'),(415,531,'MeanShift'),(416,532,'MeanShift'),(417,533,'MeanShift'),(418,534,'MeanShift'),(419,535,'MeanShift'),(420,126,'KMeans'),(421,67,'hierarchical'),(422,68,'hierarchical'),(423,69,'hierarchical'),(424,70,'hierarchical'),(425,71,'hierarchical'),(426,72,'hierarchical'),(427,1,'Normalization'),(428,2,'Normalization'),(429,3,'Normalization'),(430,4,'Normalization'),(431,5,'Normalization'),(432,6,'Normalization'),(433,7,'Normalization'),(434,8,'Normalization'),(435,9,'Normalization'),(436,10,'Normalization'),(437,536,'MeanShift'),(438,11,'Normalization'),(439,127,'KMeans'),(440,73,'hierarchical'),(441,537,'MeanShift'),(442,538,'MeanShift'),(443,128,'KMeans'),(444,129,'KMeans'),(445,74,'hierarchical'),(446,75,'hierarchical'),(447,76,'hierarchical'),(448,77,'hierarchical'),(449,78,'hierarchical'),(450,79,'hierarchical'),(451,539,'MeanShift'),(452,80,'hierarchical'),(453,540,'MeanShift'),(454,541,'MeanShift'),(455,542,'MeanShift'),(456,543,'MeanShift'),(457,544,'MeanShift'),(458,545,'MeanShift'),(459,546,'MeanShift'),(460,547,'MeanShift'),(465,552,'MeanShift'),(462,549,'MeanShift'),(463,550,'MeanShift'),(469,556,'MeanShift'),(470,557,'MeanShift'),(471,558,'MeanShift'),(472,559,'MeanShift'),(473,560,'MeanShift'),(474,561,'MeanShift'),(475,562,'MeanShift'),(476,563,'MeanShift'),(477,564,'MeanShift'),(478,565,'MeanShift'),(479,566,'MeanShift'),(484,571,'MeanShift'),(485,572,'MeanShift'),(486,573,'MeanShift'),(487,574,'MeanShift'),(488,575,'MeanShift'),(489,576,'MeanShift'),(490,577,'MeanShift'),(491,578,'MeanShift'),(492,579,'MeanShift'),(493,580,'MeanShift'),(494,581,'MeanShift'),(495,582,'MeanShift'),(496,583,'MeanShift'),(497,584,'MeanShift'),(498,585,'MeanShift'),(499,586,'MeanShift'),(500,587,'MeanShift'),(501,588,'MeanShift'),(502,589,'MeanShift'),(503,590,'MeanShift'),(504,591,'MeanShift'),(505,592,'MeanShift');
/*!40000 ALTER TABLE `alljobs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_hierarchical`
--

DROP TABLE IF EXISTS `jobs_hierarchical`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_hierarchical` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomeARQ` varchar(255) DEFAULT NULL,
  `User` varchar(255) DEFAULT NULL,
  `num_clusters` int(11) DEFAULT NULL,
  `linkage` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `tpm` varchar(255) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  `attributes` varchar(255) DEFAULT NULL,
  `normalizacao` varchar(255) DEFAULT NULL,
  `normalizacao2` varchar(255) DEFAULT NULL,
  `fpkm` varchar(255) DEFAULT NULL,
  `true_tpm` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=81 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_hierarchical`
--

LOCK TABLES `jobs_hierarchical` WRITE;
/*!40000 ALTER TABLE `jobs_hierarchical` DISABLE KEYS */;
INSERT INTO `jobs_hierarchical` VALUES (1,'aqui.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(2,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(3,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(4,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(5,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(6,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(7,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(8,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(9,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(10,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(11,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(12,'Book2.txt','Guest',3,1,3,'1','0','0','0','0',NULL,NULL),(13,'Book2.txt','Guest',3,1,3,'1','0','0','0','0',NULL,NULL),(14,'Book2.txt','Guest',3,1,3,'1','0','0','0','0',NULL,NULL),(15,'Book2.txt','Guest',3,1,2,'1','0','0','0','0',NULL,NULL),(16,'Book2.txt','Guest',3,1,2,'1','1','0','1','1',NULL,NULL),(17,'Book2.txt','Guest',3,1,2,'1','1','0','1','1',NULL,NULL),(18,'Book2.txt','teste',3,1,2,'1','1','0','1','1',NULL,NULL),(19,'Book2.txt','teste',3,1,2,'1','1','0','1','1',NULL,NULL),(20,'Book2.txt','teste',3,1,2,'0','0','0','0','0',NULL,NULL),(21,'Book2.txt','teste',3,1,2,'1','1','0','1','1',NULL,NULL),(22,'Book2.txt','teste',3,1,2,'0','0','0','0','0',NULL,NULL),(23,'Book2.txt','teste',3,1,2,'0','0','0','0','0',NULL,NULL),(24,'Book2.txt','teste',3,1,2,'0','0','0','0','0',NULL,NULL),(25,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(26,'Book2.txt','teste',3,1,2,'1','1','0','1','1',NULL,NULL),(27,'Book2.txt','teste',3,1,2,'1','0','0','1','0',NULL,NULL),(28,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(29,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(30,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(31,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(32,'Book2.txt','teste',3,1,2,'1','1','0','1','1',NULL,NULL),(33,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(34,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(35,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(36,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(37,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(38,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(39,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(40,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(41,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(42,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(43,'Book2.txt','Guest',3,1,2,'0','0','1','0','0',NULL,NULL),(44,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(45,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(46,'Book2.txt','Guest',3,1,2,'0','0','1','0','0',NULL,NULL),(47,'Book2.txt','Guest',3,1,2,'0','0','1','0','0',NULL,NULL),(48,'Book2.txt','Guest',3,1,3,'0','0','1','0','0',NULL,NULL),(49,'Book2.txt','Guest',3,1,2,'0','0','1','0','0',NULL,NULL),(50,'LOGallgenes.txt','thais',9,1,2,'0','0','0','0','0',NULL,NULL),(51,'testar.txt','Guest',2,1,3,'0','0','0','0','0',NULL,NULL),(52,'testar.txt','Guest',2,1,3,'0','0','0','0','0',NULL,NULL),(53,'testar.txt','Guest',2,1,3,'0','0','0','0','0',NULL,NULL),(54,'Book2.txt','Guest',3,1,3,'0','0','0','0','0',NULL,NULL),(55,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(56,'Book2.txt','Guest',3,1,3,'0','1','0','0','0',NULL,NULL),(57,'Book2.txt','Guest',3,1,2,'0','0','0','0','0',NULL,NULL),(58,'Book2.txt','Guest',3,2,2,'0','1','0','0','0',NULL,NULL),(59,'Book2.txt','teste',3,1,2,'0','1','0','0','0',NULL,NULL),(60,'testando.txt','teste',3,2,2,'0','0','0','0','0',NULL,NULL),(61,'testando.txt','teste',3,1,2,'0','1','0','0','0',NULL,NULL),(62,'Book2.txt','teste',3,1,2,'0','0','0','0','0',NULL,NULL),(63,'testando.txt','teste',3,1,2,'0','0','0','0','0','0',NULL),(64,'testando.txt','teste',3,1,2,'0','0','0','0','0','1',NULL),(65,'testando.txt','teste',3,1,2,'1','1','0','1','1','1',NULL),(66,'testando.txt','teste',3,1,2,'1','1','0','1','1','1',NULL),(67,'testando.txt','teste',3,1,2,'0','0','0','0','0','0','0'),(68,'testando.txt','teste',3,1,2,'0','0','0','0','0','0','0'),(69,'testando.txt','teste',3,1,2,'0','0','0','0','0','1','0'),(70,'testando.txt','Guest',3,1,2,'0','0','0','0','0','0','0'),(71,'testando.txt','Guest',3,1,2,'0','0','0','0','0','0','0'),(72,'testando.txt','teste',3,1,2,'0','0','0','0','0','0','1'),(73,'testando.txt','teste',3,1,2,'1','1','0','1','1','1','1'),(74,'Book2.txt','teste',3,1,2,'1','1','0','1','1','1','1'),(75,'Book2.txt','teste',3,1,3,'0','0','1','0','0','0','0'),(76,'Book2.txt','teste',3,1,2,'0','0','1','0','0','0','0'),(77,'Book2.txt','teste',3,1,3,'0','0','1','0','0','0','0'),(78,'Book2.txt','teste',3,1,3,'0','0','1','0','0','0','0'),(79,'Book2.txt','teste',3,1,2,'0','0','1','0','0','0','0'),(80,'Book2.txt','Guest',3,1,2,'0','0','0','0','0','0','0');
/*!40000 ALTER TABLE `jobs_hierarchical` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_kmeans`
--

DROP TABLE IF EXISTS `jobs_kmeans`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_kmeans` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nomeARQ` varchar(255) DEFAULT NULL,
  `User` varchar(255) DEFAULT NULL,
  `num_clusters` int(11) DEFAULT NULL,
  `max_iter` int(11) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `tpm` varchar(255) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  `attributes` varchar(255) DEFAULT NULL,
  `normalizacao` varchar(255) DEFAULT NULL,
  `normalizacao2` varchar(255) DEFAULT NULL,
  `fpkm` varchar(255) DEFAULT NULL,
  `true_tpm` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=130 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_kmeans`
--

LOCK TABLES `jobs_kmeans` WRITE;
/*!40000 ALTER TABLE `jobs_kmeans` DISABLE KEYS */;
INSERT INTO `jobs_kmeans` VALUES (94,'Book2.txt','Guest',3,300,2,'0','0','0','0','0',NULL,NULL),(95,'Book2.txt','teste',3,300,2,'0','0','1','0','0',NULL,NULL),(96,'Book2.txt','teste',3,300,2,'0','0','0','0','0',NULL,NULL),(97,'Book2.txt','teste',3,300,2,'1','1','0','1','1',NULL,NULL),(98,'Book2.txt','teste',3,300,2,'1','1','0','1','1',NULL,NULL),(99,'Book2.txt','teste',3,300,2,'0','0','0','1','0',NULL,NULL),(100,'saidas.txt','thais',5,300,2,'0','0','0','0','0',NULL,NULL),(101,'LOGallgenes.txt','thais',5,300,2,'0','0','0','0','0',NULL,NULL),(102,'LOGallgenes.txt','thais',7,300,2,'0','0','0','0','0',NULL,NULL),(103,'Uhlen_expressed_log.txt','thais',9,300,2,'0','0','0','0','0',NULL,NULL),(104,'fpkm_matrix_filtered.txt','Guest',5,300,3,'0','0','0','0','0',NULL,NULL),(105,'fpkm_matrix_filtered.txt','Guest',5,300,3,'0','0','0','0','0',NULL,NULL),(106,'fpkm_matrix_filtered_nocomma.txt','Guest',5,300,2,'0','0','0','0','0',NULL,NULL),(107,'fpkm_matrix_filtered_nocomma.txt','Guest',5,300,2,'0','0','0','1','1',NULL,NULL),(108,'Esse.txt','Guest',7,300,2,'0','0','0','0','0',NULL,NULL),(109,'Uhlen_expressed.txt','thais',9,300,2,'0','1','0','0','0',NULL,NULL),(110,'LOGallgenes.txt','thais',7,300,2,'0','0','0','1','1',NULL,NULL),(111,'Encode_log.txt','thais',10,300,2,'0','0','0','0','0',NULL,NULL),(112,'Selected_Genes_Log.txt','thais',3,300,2,'0','0','0','0','0',NULL,NULL),(113,'Selected_Genes_LOG.txt','thais',3,300,2,'0','0','0','0','0',NULL,NULL),(114,'aqui.txt','Guest',3,300,2,'0','0','0','0','0',NULL,NULL),(115,'teste.txt','thais',11,300,2,'0','0','0','0','0',NULL,NULL),(116,'Encode_transposta.txt','thais',7,300,2,'0','0','0','0','0',NULL,NULL),(117,'Book2.txt','Guest',3,300,2,'0','0','0','0','0',NULL,NULL),(118,'LOGallgenes.txt','thais',9,300,2,'0','0','0','0','0',NULL,NULL),(119,'testar.txt','Guest',2,300,2,'0','0','0','0','0',NULL,NULL),(120,'testando.txt','teste',3,300,2,'0','0','0','0','0',NULL,NULL),(121,'testando.txt','teste',3,300,2,'0','1','0','0','0',NULL,NULL),(122,'zikab_meta_combat_quantile_infant_270_full_t.txt','Guest',30,300,2,'0','0','0','0','0',NULL,NULL),(123,'testando.txt','teste',3,300,2,'0','0','0','0','0','0',NULL),(124,'testando.txt','teste',3,300,2,'0','0','0','0','0','1',NULL),(125,'testando.txt','teste',3,300,2,'1','1','0','1','1','1',NULL),(126,'testando.txt','teste',3,300,2,'0','0','0','0','0','0','1'),(127,'testando.txt','teste',3,300,2,'1','1','0','1','1','1','1'),(128,'Book2.txt','teste',3,300,2,'0','0','0','0','0','0','1'),(129,'Book2.txt','teste',3,300,2,'0','0','1','0','0','0','0');
/*!40000 ALTER TABLE `jobs_kmeans` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_ms`
--

DROP TABLE IF EXISTS `jobs_ms`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_ms` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nomeARQ` varchar(255) DEFAULT NULL,
  `User` varchar(255) DEFAULT NULL,
  `cluster_all` varchar(255) DEFAULT NULL,
  `bandwidth` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `Attributes` varchar(255) DEFAULT NULL,
  `tpm` varchar(255) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  `normalizacao` varchar(255) DEFAULT NULL,
  `normalizacao2` varchar(255) DEFAULT NULL,
  `discretized_points` varchar(255) DEFAULT NULL,
  `fpkm` varchar(255) DEFAULT NULL,
  `true_tpm` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=593 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_ms`
--

LOCK TABLES `jobs_ms` WRITE;
/*!40000 ALTER TABLE `jobs_ms` DISABLE KEYS */;
INSERT INTO `jobs_ms` VALUES (400,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(401,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(402,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(403,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(404,'Book2.txt','teste','1','AutoBandwidth:11.6546234488',2,'0','1','1','0','0','0',NULL,NULL),(405,'Book2.txt','teste','1','AutoBandwidth:11.6546234488',2,'0','1','1','0','0','0',NULL,NULL),(406,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(407,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(408,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(409,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(410,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(411,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(412,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(413,'Book2.txt','teste','1','AutoBandwidth:435390.9614',2,'0','1','0','0','0','0',NULL,NULL),(414,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','1','1','1','0',NULL,NULL),(415,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(416,'Book2.txt','teste','1','AutoBandwidth:435390.9614',2,'0','1','0','0','0','0',NULL,NULL),(417,'Book2.txt','teste','1','AutoBandwidth',3,'0','1','0','0','0','0',NULL,NULL),(418,'Book2.txt','teste','1','AutoBandwidth:435390.9614',2,'0','1','0','0','0','0',NULL,NULL),(419,'Book2.txt','teste','1','AutoBandwidth:435390.9614',2,'0','1','0','0','0','0',NULL,NULL),(420,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(421,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(422,'Book2.txt','teste','1','AutoBandwidth:11.6546234488',2,'0','0','1','0','0','0',NULL,NULL),(423,'Book2.txt','teste','1','AutoBandwidth:435390.9614',2,'0','1','0','0','0','0',NULL,NULL),(424,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(425,'Book2.txt','teste','1','AutoBandwidth:61.8027185787',2,'0','1','1','0','1','0',NULL,NULL),(426,'Book2.txt','teste','0','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(427,'Book2.txt','teste','0','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(428,'teste.txt','Guest','1','AutoBandwidth:0.861711253069',2,'0','0','0','0','0','0',NULL,NULL),(429,'Book2.txt','Guest','1','AutoBandwidth:0.158085015562',2,'0','0','0','1','0','0',NULL,NULL),(430,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(431,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(432,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(433,'Book2.txt','teste','1','AutoBandwidth:61.8027185786',2,'0','1','1','1','1','0',NULL,NULL),(434,'output2.txt','tayronesm@gmail.com','1','AutoBandwidth:0.0406920342222',2,'0','0','0','0','0','0',NULL,NULL),(435,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(436,'tecidos.txt','thais','1','AutoBandwidth:0.650500239272',2,'0','0','0','0','0','0',NULL,NULL),(437,'tecidos.txt','thais','1','AutoBandwidth:0.650500239272',2,'0','0','0','0','0','1',NULL,NULL),(438,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(439,'saidas.txt','thais','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(440,'saidas.txt','thais','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(441,'saidas.txt','thais','1','AutoBandwidth:63593.9573064',2,'0','0','0','0','0','1',NULL,NULL),(442,'saidas.txt','thais','1','AutoBandwidth:0.0635939576203',2,'0','0','0','1','0','1',NULL,NULL),(443,'saidas.txt','thais','1','AutoBandwidth:19796879.7303',2,'0','1','0','0','0','1',NULL,NULL),(444,'saidas.txt','thais','1','AutoBandwidth',3,'0','0','1','0','0','1',NULL,NULL),(445,'saidas.txt','thais','1','AutoBandwidth:1433.3631615',2,'0','0','1','0','0','0',NULL,NULL),(446,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(447,'Uhlen_expressed.txt','None','0','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(448,'Uhlen_expressed.txt','thais','0','AutoBandwidth:131.369021018',2,'0','0','0','0','0','1',NULL,NULL),(449,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(450,'resultado.txt','thais','1','AutoBandwidth:35802.007808',2,'0','0','0','0','0','0',NULL,NULL),(451,'resultado.txt','thais','1','AutoBandwidth:19179824.4447',2,'0','1','0','0','0','0',NULL,NULL),(452,'resultado.txt','thais','1','AutoBandwidth:1397.94573395',2,'0','0','1','0','0','0',NULL,NULL),(453,'resultado.txt','thais','1','AutoBandwidth:0.119658349999',2,'0','0','0','1','0','0',NULL,NULL),(454,'resultado.txt','thais','1','AutoBandwidth:227.500158946',2,'0','0','0','0','1','0',NULL,NULL),(455,'saidas.txt','thais','1','1000',2,'0','0','0','0','0','0',NULL,NULL),(456,'saidas.txt','thais','1','30000',2,'0','0','0','0','0','0',NULL,NULL),(457,'saidas.txt','thais','1','50000',2,'0','0','0','0','0','0',NULL,NULL),(458,'saidas.txt','thais','1','1000',2,'0','0','1','0','0','0',NULL,NULL),(459,'saidas.txt','thais','1','1200',2,'0','0','1','0','0','0',NULL,NULL),(460,'LOGallgenes.txt','thais','1','AutoBandwidth:1433.3631615',2,'0','0','0','0','0','0',NULL,NULL),(461,'fpkm_matrix.txt','Guest','1','AutoBandwidth',3,'0','0','0','1','1','1',NULL,NULL),(462,'fpkm_matrix.txt','Guest','1','AutoBandwidth',3,'0','0','0','1','1','1',NULL,NULL),(463,'fpkm_matrix.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(464,'fpkm_matrix_filtered_nocomma.txt','Guest','1','AutoBandwidth:205.734623349',2,'0','0','0','1','1','0',NULL,NULL),(465,'teste2.txt','thais','1','AutoBandwidth:20.7065473311',2,'0','0','0','0','0','0',NULL,NULL),(466,'Fantom_log.txt','thais','1','AutoBandwidth:55.3921118579',2,'0','0','0','0','0','0',NULL,NULL),(467,'Encode_log.txt','thais','1','AutoBandwidth:22.9476265449',2,'0','0','0','0','0','0',NULL,NULL),(468,'Selected_Genes_Log.txt','thais','1','AutoBandwidth:14.7358929226',2,'0','0','0','0','0','0',NULL,NULL),(469,'Selected_Genes_Log.txt','thais','1','AutoBandwidth:23.7019714278',2,'0','0','0','0','0','0',NULL,NULL),(470,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(471,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(472,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0',NULL,NULL),(473,'aqui.txt','Guest','0','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(474,'testar.txt','Guest','0','AutoBandwidth:43.0550564608',2,'0','0','0','0','0','0',NULL,NULL),(475,'testando.txt','teste','1','AutoBandwidth:203.29761006',2,'0','0','0','0','0','1',NULL,NULL),(476,'testando.txt','teste','1','AutoBandwidth:19.7358597582',2,'0','0','1','0','0','1',NULL,NULL),(477,'Selected_Genes_Log.txt','thais','1','AutoBandwidth:23.7019714278',2,'0','0','0','0','0','0',NULL,NULL),(478,'Encode_log.txt','thais','1','AutoBandwidth:22.9476265449',2,'0','0','0','0','0','0',NULL,NULL),(479,'Encode_log.txt','thais','1','50',2,'0','0','0','0','0','0',NULL,NULL),(480,'Encode_log.txt','thais','1','35',2,'0','0','0','0','0','0',NULL,NULL),(481,'Encode_log.txt','thais','1','25',2,'0','0','0','0','0','0',NULL,NULL),(482,'Encode_log.txt','thais','1','24',2,'0','0','0','0','0','0',NULL,NULL),(483,'Encode_transposta.txt','thais','1','AutoBandwidth:1553.90534727',2,'0','0','0','0','0','0',NULL,NULL),(484,'Encode_transposta.txt','thais','1','1000',2,'0','0','0','0','0','0',NULL,NULL),(485,'Encode_transposta.txt','thais','1','1250',2,'0','0','0','0','0','0',NULL,NULL),(486,'Encode_transposta.txt','thais','1','1100',2,'0','0','0','0','0','0',NULL,NULL),(487,'Encode_transposta.txt','Guest','1','1050',2,'0','0','0','0','0','0',NULL,NULL),(488,'Encode_transposta.txt','Guest','1','1010',2,'0','0','0','0','0','0',NULL,NULL),(489,'Encode_transposta.txt','thais','1','1005',2,'0','0','0','0','0','0',NULL,NULL),(490,'Encode_transposta.txt','thais','1','1002',2,'0','0','0','0','0','0',NULL,NULL),(491,'Encode_transposta.txt','thais','1','1500',2,'0','0','0','0','0','0',NULL,NULL),(492,'Encode_transposta.txt','thais','1','1400',2,'0','0','0','0','0','0',NULL,NULL),(493,'Encode_transposta.txt','thais','1','1300',2,'0','0','0','0','0','0',NULL,NULL),(494,'Encode_transposta.txt','thais','1','1450',2,'0','0','0','0','0','0',NULL,NULL),(495,'Encode_transposta.txt','thais','1','1440',2,'0','0','0','0','0','0',NULL,NULL),(496,'Encode_transposta.txt','thais','1','1420',2,'0','0','0','0','0','0',NULL,NULL),(497,'Encode_transposta.txt','thais','1','1430',2,'0','0','0','0','0','0',NULL,NULL),(498,'Encode_transposta.txt','thais','1','1410',2,'0','0','0','0','0','0',NULL,NULL),(499,'Encode_transposta.txt','thais','1','1417',2,'0','0','0','0','0','0',NULL,NULL),(500,'Encode_transposta.txt','thais','1','1414',2,'0','0','0','0','0','0',NULL,NULL),(501,'Encode_transposta.txt','thais','1','1412',2,'0','0','0','0','0','0',NULL,NULL),(502,'Encode_transposta.txt','thais','1','1411',2,'0','0','0','0','0','0',NULL,NULL),(503,'Encode_transposta.txt','thais','1','1411.5',2,'0','0','0','0','0','0',NULL,NULL),(504,'Encode_transposta.txt','thais','1','1411.8',2,'0','0','0','0','0','0',NULL,NULL),(505,'Encode_transposta.txt','thais','1','1411.9',2,'0','0','0','0','0','0',NULL,NULL),(506,'zikab_meta_combat_quantile_infant_270_full.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(507,'zikab_meta_combat_quantile_infant_270_full.txt','Guest','1','AutoBandwidth:46.3456135753',2,'0','0','0','0','0','1',NULL,NULL),(508,'zikab_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(509,'zikab_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(510,'zikab_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth:303.324836645',2,'0','0','0','0','0','0',NULL,NULL),(511,'top5000_zikb_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(512,'top5000_zikb_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'1','0','0','0','0','1',NULL,NULL),(513,'top5000_zikb_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth:208.514262473',2,'0','0','0','0','0','0',NULL,NULL),(514,'top5000_zikb_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(515,'top5000_zikb_meta_combat_quantile_infant_270_full_t.txt','Guest','1','AutoBandwidth',3,'0','0','0','0','0','1',NULL,NULL),(516,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(517,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1',NULL,NULL),(518,'testando.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','None',NULL),(519,'testando.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','None',NULL),(520,'testando.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','0',NULL),(521,'testando.txt','teste','1','AutoBandwidth:15817292.2784',2,'0','0','0','0','0','0','1',NULL),(522,'testando.txt','teste','1','AutoBandwidth:62.2576409186',2,'0','1','1','1','1','0','1',NULL),(523,'testando.txt','teste','1','AutoBandwidth',3,'0','0','0','0','0','0','1',NULL),(524,'testando.txt','teste','1','AutoBandwidth',3,'0','0','0','0','0','0','0',NULL),(525,'testando.txt','teste','1','AutoBandwidth:202.364229167',2,'0','0','0','0','0','0','0',NULL),(526,'testando.txt','teste','1','AutoBandwidth:237832773.573',2,'0','0','0','0','0','0','1',NULL),(527,'testando.txt','teste','1','AutoBandwidth:202.364229167',2,'0','0','0','0','0','0','0',NULL),(528,'testando.txt','teste','1','AutoBandwidth:237832773.573',2,'0','0','0','0','0','0','1',NULL),(529,'testando.txt','teste','1','AutoBandwidth:474319.686696',2,'0','1','0','0','0','0','1',NULL),(530,'testando.txt','teste','1','AutoBandwidth:474319.686696',2,'0','1','0','0','0','0','1',NULL),(531,'testando.txt','teste','1','AutoBandwidth:202.364229167',2,'0','0','0','0','0','0','0',NULL),(532,'testando.txt','teste','1','AutoBandwidth:451646.742204',2,'0','1','0','0','0','0','0',NULL),(533,'testando.txt','teste','1','AutoBandwidth:202.364229167',2,'0','0','0','0','0','0','0','None'),(534,'testando.txt','teste','1','AutoBandwidth:202.364229167',2,'0','0','0','0','0','0','0','None'),(535,'testando.txt','teste','1','AutoBandwidth:474319.686696',2,'0','0','0','0','0','0','0','1'),(536,'testando.txt','teste','1','AutoBandwidth:62.2576409185',2,'0','1','1','1','1','0','1','1'),(537,'Book2.txt','teste','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','0','0'),(538,'Book2.txt','teste','1','AutoBandwidth:201.185472412',2,'1','0','0','0','0','0','0','0'),(539,'Book2.txt','Guest','1','AutoBandwidth:51.1524063075',2,'1','1','1','1','1','0','1','1'),(540,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(541,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(542,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(543,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','0','1','0'),(544,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','0','1','0'),(545,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(546,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(547,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(558,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(556,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(557,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(559,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(560,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(561,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(562,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(563,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','0','1','0'),(564,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','0','1','0'),(565,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(566,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(567,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(568,'Book2.txt','Guest','1','AutoBandwidth',3,'0','1','1','0','0','1','1','0'),(569,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(570,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(571,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(572,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(573,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(574,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1','0','0'),(575,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','0','0'),(576,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1','0','0'),(577,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1','0','0'),(578,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(579,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(580,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1','0','0'),(581,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','0','0'),(582,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','1','1','0'),(583,'Book2.txt','Guest','1','AutoBandwidth:10.5616915263',2,'0','1','1','0','0','0','1','0'),(584,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','1','0','0'),(585,'Book2.txt','Guest','1','AutoBandwidth:202.292022212',2,'0','0','0','0','0','0','0','0'),(586,'Book2.txt','Guest','1','AutoBandwidth:51.9135996363',2,'0','1','1','1','1','1','1','1'),(587,'Book2.txt','Guest','1','AutoBandwidth:51.9135996363',2,'0','1','1','1','1','0','1','1'),(588,'Book2.txt','teste','1','AutoBandwidth:51.9135996363',2,'0','1','1','1','1','1','1','1'),(589,'teste.txt','teste','1','AutoBandwidth',3,'0','0','0','0','0','1','0','0'),(590,'Book2.txt','teste','1','AutoBandwidth:51.9135996363',2,'0','1','1','1','1','1','1','1'),(591,'Book2.txt','teste','1','3',2,'0','1','1','1','1','1','1','1'),(592,'Book2.txt','teste','1','3',2,'0','1','1','1','1','0','1','1');
/*!40000 ALTER TABLE `jobs_ms` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `jobs_normalization`
--

DROP TABLE IF EXISTS `jobs_normalization`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `jobs_normalization` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `nomeARQ` varchar(255) DEFAULT NULL,
  `tpm` varchar(255) DEFAULT NULL,
  `log` varchar(255) DEFAULT NULL,
  `normalizacao` varchar(255) DEFAULT NULL,
  `status` int(11) DEFAULT NULL,
  `normalizacao2` varchar(255) DEFAULT NULL,
  `fpkm` varchar(255) DEFAULT NULL,
  `true_tpm` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `jobs_normalization`
--

LOCK TABLES `jobs_normalization` WRITE;
/*!40000 ALTER TABLE `jobs_normalization` DISABLE KEYS */;
INSERT INTO `jobs_normalization` VALUES (1,'testando.txt','None','None','None',2,'None','None','None'),(2,'testando.txt','None','None','None',2,'None','None','None'),(3,'testando.txt','None','None','None',2,'None','None','None'),(4,'testando.txt','None','None','None',2,'None','None','None'),(5,'testando.txt','None','None','None',2,'None','None','None'),(6,'testando.txt','0','0','0',2,'0','1','0'),(7,'testando.txt','0','0','0',2,'0','1','0'),(8,'testando.txt','0','0','0',2,'0','1','0'),(9,'testando.txt','0','0','0',2,'0','1','0'),(10,'testando.txt','1','1','1',2,'1','1','1'),(11,'testando.txt','1','1','1',2,'1','1','1');
/*!40000 ALTER TABLE `jobs_normalization` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2018-07-01 17:37:22
