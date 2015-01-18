DROP TABLE IF EXISTS icd_us_neo;

CREATE TABLE `icd_us_neo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `versionyear` enum('10-2015') NOT NULL DEFAULT '10-2015',
  `Neo` varchar(128) NOT NULL,
  `MalignatPrim` varchar(45) DEFAULT NULL,
  `MalignatSec` varchar(45) DEFAULT NULL,
  `Ca_in_Situ` varchar(45) DEFAULT NULL,
  `Benign` varchar(45) DEFAULT NULL,
  `UncertainB` varchar(45) DEFAULT NULL,
  `UnspecifiedB` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

