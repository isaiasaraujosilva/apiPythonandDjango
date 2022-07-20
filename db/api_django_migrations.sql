-- MySQL dump 10.13  Distrib 8.0.29, for Linux (x86_64)
--
-- Host: localhost    Database: api
-- ------------------------------------------------------
-- Server version	8.0.29-0ubuntu0.22.04.2

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
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=33 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2022-07-20 00:59:51.007759'),(2,'auth','0001_initial','2022-07-20 00:59:52.981916'),(3,'admin','0001_initial','2022-07-20 00:59:53.417566'),(4,'admin','0002_logentry_remove_auto_add','2022-07-20 00:59:53.435431'),(5,'admin','0003_logentry_add_action_flag_choices','2022-07-20 00:59:53.457504'),(6,'api','0001_initial','2022-07-20 00:59:53.528715'),(7,'api','0002_rename_primeironome_cliente_nome_and_more','2022-07-20 00:59:53.624884'),(8,'api','0003_produto_rename_nome_cliente_nome','2022-07-20 00:59:53.738442'),(9,'api','0004_pedido','2022-07-20 00:59:54.093494'),(10,'api','0005_rename_unidade_produto_quantidade_and_more','2022-07-20 00:59:54.212719'),(11,'api','0006_pedido_valor_do_pedido','2022-07-20 00:59:54.289044'),(12,'api','0007_remove_pedido_valor_do_pedido_remove_pedido_produto_and_more','2022-07-20 00:59:54.906031'),(13,'api','0008_pedido_concluido','2022-07-20 00:59:54.990181'),(14,'api','0009_rename_concluido_pedido_pedido_concluido','2022-07-20 00:59:55.054246'),(15,'api','0010_faturamento','2022-07-20 00:59:55.121674'),(16,'api','0011_faturamento_faturamento_total','2022-07-20 00:59:55.192168'),(17,'api','0012_remove_faturamento_faturamento_total','2022-07-20 00:59:55.246199'),(18,'api','0013_faturamento_pedido','2022-07-20 00:59:55.657160'),(19,'contenttypes','0002_remove_content_type_name','2022-07-20 00:59:55.853333'),(20,'auth','0002_alter_permission_name_max_length','2022-07-20 00:59:56.009662'),(21,'auth','0003_alter_user_email_max_length','2022-07-20 00:59:56.065649'),(22,'auth','0004_alter_user_username_opts','2022-07-20 00:59:56.088041'),(23,'auth','0005_alter_user_last_login_null','2022-07-20 00:59:56.224455'),(24,'auth','0006_require_contenttypes_0002','2022-07-20 00:59:56.233092'),(25,'auth','0007_alter_validators_add_error_messages','2022-07-20 00:59:56.254775'),(26,'auth','0008_alter_user_username_max_length','2022-07-20 00:59:56.426839'),(27,'auth','0009_alter_user_last_name_max_length','2022-07-20 00:59:56.599731'),(28,'auth','0010_alter_group_name_max_length','2022-07-20 00:59:56.652363'),(29,'auth','0011_update_proxy_permissions','2022-07-20 00:59:56.679997'),(30,'auth','0012_alter_user_first_name_max_length','2022-07-20 00:59:56.847419'),(31,'sessions','0001_initial','2022-07-20 00:59:56.964670'),(32,'api','0014_lucro_remove_faturamento_pedido','2022-07-20 01:11:44.231025');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-07-19 22:43:45
