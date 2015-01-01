DROP TABLE IF EXISTS `icd_us_drugs`;

CREATE TABLE `icd_us_drugs` (
  `id` INT NOT NULL AUTO_INCREMENT,
 `versionyear` enum('10-2015') NOT NULL DEFAULT '10-2015',
  `substance` varchar(128) DEFAULT NULL,
  `poisonAcc` varchar(128) DEFAULT NULL COMMENT 'Poisoning, Accidental (unintentional)',
  `poisonIsh` varchar(128) DEFAULT NULL COMMENT 'Poisoning, Intentional self-harm',
  `poisonAss` varchar(128) DEFAULT NULL COMMENT 'Poisoning, Assault',
  `poisonUnd` varchar(128) DEFAULT NULL COMMENT 'Poisoning, Undetermined',
  `effect` varchar(128) DEFAULT NULL COMMENT 'Adverse effect',
  `under` varchar(128) DEFAULT NULL COMMENT 'Underdosing',
	primary key (id)
) 
