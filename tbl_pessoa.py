CREATE TABLE `tbl_user` (
  `pessoa_id` bigint(255) NOT NULL AUTO_INCREMENT,
  `pessoa_nome` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pessoa_idade` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pessoa_endereco` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pessoa_email` varchar(255) COLLATE utf8_unicode_ci DEFAULT NULL,
  `pessoa_telefone` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,
   `pessoa_cpf` varchar(25) COLLATE utf8_unicode_ci DEFAULT NULL,


  PRIMARY KEY (`pessoa_id`)
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
