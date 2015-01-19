DROP TABLE IF EXISTS icd_us_index_diseases;

CREATE TABLE `icd_us_index_diseases` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `versionyear` enum('10-2015') NOT NULL DEFAULT '10-2015',
  `term` varchar(128) DEFAULT NULL,
  `code` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`id`)
);
