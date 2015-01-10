Drop TABLE IF EXISTS `icd_10_desc`;

Create TABLE `icd_10_desc` (
	`id` varchar(10) NOT NULL ,
 	`versionyear` enum('10-2015') NOT NULL DEFAULT '10-2015',
  	`code` varchar(128) DEFAULT NULL COMMENT 'ICD10 Code' ,
	`description` varchar(300) DEFAULT NULL COMMENT 'The Description of the Code',
		primary key(id)
)
