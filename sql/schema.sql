CREATE DATABASE IF NOT EXISTS WIDGETTOOL_DEV_SCHEMA;
USE WIDGETTOOL_DEV_SCHEMA;

DROP TABLE IF EXISTS `Publisher`;

CREATE TABLE `Publisher` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `description` varchar(1000) DEFAULT NULL,
    `domain` varchar(100) DEFAULT NULL,
    `mail` varchar(50) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Gender`;

CREATE TABLE `Gender` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `User`;

CREATE TABLE `User` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `firstName` varchar(100) DEFAULT NULL,
    `lastName` varchar(100) DEFAULT NULL,
    `email` varchar(100) DEFAULT NULL,
    `password` varchar(128) DEFAULT NULL,
    `authToken` varchar(256) DEFAULT NULL,
    `admin` bit(1) NOT NULL DEFAULT b'0',
    `registrationDate` datetime DEFAULT NULL,
    `lastLogin` timestamp NULL DEFAULT NULL,
    `fkPublisher` bigint(20) NOT NULL,
    `fkGender` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkPublisher` (`fkPublisher`),
    KEY `fkGender` (`fkGender`),
    CONSTRAINT `User_ibfk_1` FOREIGN KEY (`fkPublisher`) REFERENCES `Publisher` (`id`),
    CONSTRAINT `User_ibfk_2` FOREIGN KEY (`fkGender`) REFERENCES `Gender` (`id`) 
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CompetionType`;

CREATE TABLE `CompetionType` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `fkGender` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkGender` (`fkGender`),
    CONSTRAINT `CompetionType_ibfk_1` FOREIGN KEY (`fkGender`) REFERENCES `Gender` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Competion`;

CREATE TABLE `Competion` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `shortName` varchar(100) DEFAULT NULL,
    `fkCompetionType` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetionType` (`fkCompetionType`),
    CONSTRAINT `Competion_ibfk_1` FOREIGN KEY (`fkCompetionType`) REFERENCES `CompetionType` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CompetionRound`;

CREATE TABLE `CompetionRound` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `fkCompetion` bigint(20) NOT NULL,
    `count` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetion` (`fkCompetion`),
    CONSTRAINT `CompetionRound_ibfk_1` FOREIGN KEY (`fkCompetion`) REFERENCES `Competion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CompetionGroup`;

CREATE TABLE `CompetionGroup` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    `fkCompetionRound` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetionRound` (`fkCompetionRound`),
    CONSTRAINT `CompetionGroup_ibfk_1` FOREIGN KEY (`fkCompetionRound`) REFERENCES `CompetionRound` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `PublisherCompetionMap`;

CREATE TABLE `PublisherCompetionMap` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkPublisher` bigint(20) NOT NULL,
    `fkCompetion` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkPublisher` (`fkPublisher`),
    KEY `fkCompetion` (`fkCompetion`),
    CONSTRAINT `PublisherCompetionMap_ibfk_1` FOREIGN KEY (`fkPublisher`) REFERENCES `Publisher` (`id`),
    CONSTRAINT `PublisherCompetionMap_ibfk_2` FOREIGN KEY (`fkCompetion`) REFERENCES `Competion` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Season`;

CREATE TABLE `Season` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `current` bit(1) NOT NULL,
    `year` int(11) NOT NULL,
    `dfbNetKey` varchar(20) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CompetionSeasonMap`;

CREATE TABLE `CompetionSeasonMap` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkCompetion` bigint(20) NOT NULL,
    `fkSeason` bigint(20) NOT NULL,
    `placesPromotion` tinyint(4) DEFAULT NULL,
    `placesPromotionExpul` tinyint(4) DEFAULT NULL,
    `placesRelegation` tinyint(4) DEFAULT NULL,
    `placesRelegationExpul` tinyint(4) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetion` (`fkCompetion`),
    KEY `fkSeason` (`fkSeason`),
    CONSTRAINT `CompetionSeasonMap_ibfk_1` FOREIGN KEY (`fkCompetion`) REFERENCES `Competion` (`id`),
    CONSTRAINT `CompetionSeasonMap_ibfk_2` FOREIGN KEY (`fkSeason`) REFERENCES `Season` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `SportType`;

CREATE TABLE `SportType` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `TeamType`;

CREATE TABLE `TeamType` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(255) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Team`;

CREATE TABLE `Team` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `fkSportType` bigint(20) NOT NULL,
    `fkTeamType` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkSportType` (`fkSportType`),
    KEY `fkTeamType` (`fkTeamType`),
    CONSTRAINT `Team_ibfk_1` FOREIGN KEY (`fkSportType`) REFERENCES `SportType` (`id`),
    CONSTRAINT `Team_ibfk_2` FOREIGN KEY (`fkTeamType`) REFERENCES `TeamType` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `CompetionTeamMap`;

CREATE TABLE `CompetionTeamMap` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkCompetion` bigint(20) NOT NULL,
    `fkTeam` bigint(20) NOT NULL,
    `fkSeason` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetion` (`fkCompetion`),
    KEY `fkTeam` (`fkTeam`),
    KEY `fkSeason` (`fkSeason`),
    CONSTRAINT `CompetionTeamMap_ibfk_1` FOREIGN KEY (`fkCompetion`) REFERENCES `Competion` (`id`),
    CONSTRAINT `CompetionTeamMap_ibfk_2` FOREIGN KEY (`fkTeam`) REFERENCES `Team` (`id`),
    CONSTRAINT `CompetionTeamMap_ibfk_3` FOREIGN KEY (`fkSeason`) REFERENCES `Season` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `ResultCode`;

CREATE TABLE `ResultCode` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `name` varchar(100) NOT NULL,
    `shortName` varchar(100) NOT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Match`;

CREATE TABLE `Match` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkCompetion` bigint(20) NOT NULL,
    `fkSeason` bigint(20) NOT NULL,
    `fkTeamHome` bigint(20) NOT NULL,
    `fkTeamAway` bigint(20) NOT NULL,
    `fkResultCode` bigint(20) unsigned DEFAULT NULL,
    `goalsHome` int(11) DEFAULT NULL,
    `goalsAway` int(11) DEFAULT NULL,
    `goalsAgainstHome` int(11) DEFAULT NULL,
    `goalsAgainstAway` int(11) DEFAULT NULL,
    `goalsHomeHalftime` int(11) DEFAULT NULL,
    `goalsAwayHalftime` int(11) DEFAULT NULL,
    `matchDate` datetime NOT NULL,
    `matchDay` tinyint(4) NOT NULL,
    `location` varchar(200) DEFAULT NULL,
    `referee` varchar(100) DEFAULT NULL,
    `visitors` int(11) DEFAULT NULL,
    `liveGoalsHome` int(11) DEFAULT NULL,
    `liveGoalsAway` int(11) DEFAULT NULL,
    PRIMARY KEY (`id`),
    KEY `fkCompetion` (`fkCompetion`),
    KEY `fkSeason` (`fkSeason`),
    KEY `fkTeamHome` (`fkTeamHome`),
    KEY `fkTeamAway` (`fkTeamAway`),
    KEY `fkResultCode` (`fkResultCode`),
    CONSTRAINT `Match_ibfk_1` FOREIGN KEY (`fkCompetion`) REFERENCES `Competion` (`id`),
    CONSTRAINT `Match_ibfk_2` FOREIGN KEY (`fkSeason`) REFERENCES `Season` (`id`),
    CONSTRAINT `Match_ibfk_3` FOREIGN KEY (`fkTeamHome`) REFERENCES `Team` (`id`),
    CONSTRAINT `Match_ibfk_4` FOREIGN KEY (`fkTeamAway`) REFERENCES `Team` (`id`),
    CONSTRAINT `Match_ibfk_5` FOREIGN KEY (`fkResultCode`) REFERENCES `ResultCode` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Referee`;

CREATE TABLE `Referee` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `firstName` varchar(100) DEFAULT NULL,
    `lastName` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Player`;

CREATE TABLE `Player` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `firstName` varchar(100) DEFAULT NULL,
    `lastName` varchar(100) DEFAULT NULL, 
    PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Card`;

CREATE TABLE `Card` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkMatch` bigint(20) NOT NULL,
    `fkPlayer` bigint(20) NOT NULL,
    `fkTeam` bigint(20) NOT NULL,
    `minute` bigint(20) NOT NULL,
    `cardType` varchar(100) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkMatch` (`fkMatch`),
    KEY `fkPlayer` (`fkPlayer`),
    KEY `fkTeam` (`fkTeam`),
    CONSTRAINT `Card_ibfk_1` FOREIGN KEY (`fkMatch`) REFERENCES `Match` (`id`),
    CONSTRAINT `Card_ibfk_2` FOREIGN KEY (`fkPlayer`) REFERENCES `Player` (`id`),
    CONSTRAINT `Card_ibfk_3` FOREIGN KEY (`fkTeam`) REFERENCES `Team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;



CREATE TABLE `Goal` (
    `id` bigint(20) NOT NULL AUTO_INCREMENT,
    `fkMatch` bigint(20) NOT NULL,
    `fkPlayer` bigint(20) NOT NULL,
    `fkTeam` bigint(20) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkMatch` (`fkMatch`),
    KEY `fkPlayer` (`fkPlayer`),
    KEY `fkTeam` (`fkTeam`),
    CONSTRAINT `Goal_ibfk_1` FOREIGN KEY (`fkMatch`) REFERENCES `Match` (`id`),
    CONSTRAINT `Goal_ibfk_2` FOREIGN KEY (`fkPlayer`) REFERENCES `Player` (`id`),
    CONSTRAINT `Goal_ibfk_3` FOREIGN KEY (`fkTeam`) REFERENCES `Team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Lineup`;

CREATE TABLE `Lineup` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `fkMatch` bigint(20) NOT NULL,
    `fkPlayer` bigint(20) NOT NULL,
    `fkTeam` bigint(20) NOT NULL,
    `isStarting` bit(1),
    `isCaptain` bit(1),
    `shirtNumber` tinyint(4),
    PRIMARY KEY (`id`),
    KEY `fkMatch` (`fkMatch`),
    KEY `fkPlayer` (`fkPlayer`),
    KEY `fkTeam` (`fkTeam`),
    CONSTRAINT `Lineup_ibfk_1` FOREIGN KEY (`fkMatch`) REFERENCES `Match` (`id`),
    CONSTRAINT `Lineup_ibfk_2` FOREIGN KEY (`fkPlayer`) REFERENCES `Player` (`id`),
    CONSTRAINT `Lineup_ibfk_3` FOREIGN KEY (`fkTeam`) REFERENCES `Team` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;

DROP TABLE IF EXISTS `Substitution`;

CREATE TABLE `Substitution` (
    `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
    `fkLineup_out` bigint(20) unsigned NOT NULL,
    `fkLineup_in` bigint(20) unsigned NOT NULL,
    `minute` tinyint(4) NOT NULL,
    `isOvertime` bit(1) NOT NULL,
    PRIMARY KEY (`id`),
    KEY `fkLineup_out` (`fkLineup_out`),
    KEY `fkLineup_in` (`fkLineup_in`),
    CONSTRAINT `Substitution_ibfk_1` FOREIGN KEY (`fkLineup_out`) REFERENCES `Lineup` (`id`),
    CONSTRAINT `Substitution_ibfk_2` FOREIGN KEY (`fkLineup_in`) REFERENCES `Lineup` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=0 DEFAULT CHARSET=utf8;
