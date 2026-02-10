-- phpMyAdmin SQL Dump
-- version 3.3.9
-- http://www.phpmyadmin.net
--
-- Serveur: localhost
-- Généré le : Ven 11 Octobre 2013 à 13:48
-- Version du serveur: 5.5.8
-- Version de PHP: 5.3.5

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Base de données: `asterixdb`
--

-- --------------------------------------------------------

--
-- Structure de la table `absorber`
--

CREATE TABLE IF NOT EXISTS `absorber` (
  `NumPotion` int(11) NOT NULL DEFAULT '0',
  `DateA` datetime NOT NULL DEFAULT '0000-00-00 00:00:00',
  `NumHab` int(11) NOT NULL DEFAULT '0',
  `Quantite` int(11) DEFAULT NULL,
  PRIMARY KEY (`DateA`,`NumPotion`,`NumHab`),
  KEY `NumPotion` (`NumPotion`),
  KEY `DateA` (`DateA`),
  KEY `NumHab` (`NumHab`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `absorber`
--

INSERT INTO `absorber` (`NumPotion`, `DateA`, `NumHab`, `Quantite`) VALUES
(1, '2052-02-18 00:00:00', 7, 3),
(2, '2052-02-18 00:00:00', 12, 4),
(1, '2052-02-20 00:00:00', 2, 2),
(1, '2052-02-20 00:00:00', 8, 2),
(3, '2052-02-20 00:00:00', 7, 1),
(1, '2052-04-03 00:00:00', 7, 1),
(1, '2052-04-03 00:00:00', 15, 2),
(2, '2052-04-03 00:00:00', 13, 5),
(3, '2052-04-03 00:00:00', 10, 4),
(4, '2052-05-05 00:00:00', 15, 2),
(5, '2052-05-10 00:00:00', 1, 4),
(5, '2052-05-10 00:00:00', 2, 1),
(1, '2052-06-06 00:00:00', 13, 2),
(2, '2052-06-06 00:00:00', 7, 1),
(3, '2052-06-06 00:00:00', 8, 4),
(5, '2052-06-07 00:00:00', 1, 2),
(5, '2052-07-17 00:00:00', 7, 1),
(2, '2052-07-18 00:00:00', 7, 3),
(1, '2052-08-18 00:00:00', 8, 3),
(1, '2052-08-18 00:00:00', 16, 1),
(3, '2052-08-18 00:00:00', 10, 2),
(4, '2052-08-18 00:00:00', 7, 2),
(3, '2052-09-20 00:00:00', 7, 5),
(4, '2052-09-20 00:00:00', 1, 2),
(2, '2052-10-23 00:00:00', 7, 4),
(3, '2052-10-23 00:00:00', 13, 1),
(4, '2052-10-23 00:00:00', 13, 3),
(1, '2052-11-26 00:00:00', 10, 2),
(2, '2052-11-26 00:00:00', 8, 2),
(5, '2052-11-26 00:00:00', 13, 2),
(5, '2052-11-26 00:00:00', 16, 2);

-- --------------------------------------------------------

--
-- Structure de la table `categorie`
--

CREATE TABLE IF NOT EXISTS `categorie` (
  `CodeCat` char(3) NOT NULL DEFAULT '',
  `NomCateg` varchar(50) DEFAULT NULL,
  `NbPoints` int(11) DEFAULT NULL,
  PRIMARY KEY (`CodeCat`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `categorie`
--

INSERT INTO `categorie` (`CodeCat`, `NomCateg`, `NbPoints`) VALUES
('BCN', 'Bouclier de Centurion', 6),
('BDN', 'Bouclier de Décurion', 4),
('BLE', 'Bouclier de Légionnaire', 3),
('BLT', 'Bouclier de Légat', 10),
('CCN', 'Casque de Centurion', 3),
('CDN', 'Casque de Décurion', 2),
('CLE', 'Casque de Légionnaire', 1),
('CLT', 'Casque de Légat', 4);

-- --------------------------------------------------------

--
-- Structure de la table `fabriquer`
--

CREATE TABLE IF NOT EXISTS `fabriquer` (
  `NumPotion` int(11) NOT NULL DEFAULT '0',
  `NumHab` int(11) NOT NULL DEFAULT '0',
  PRIMARY KEY (`NumHab`,`NumPotion`),
  KEY `NumPotion` (`NumPotion`),
  KEY `NumHab` (`NumHab`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `fabriquer`
--

INSERT INTO `fabriquer` (`NumPotion`, `NumHab`) VALUES
(1, 4),
(2, 2),
(3, 3),
(4, 4),
(4, 6),
(5, 2),
(5, 4);

-- --------------------------------------------------------

--
-- Structure de la table `habitant`
--

CREATE TABLE IF NOT EXISTS `habitant` (
  `NumHab` int(11) NOT NULL DEFAULT '0',
  `Nom` varchar(30) DEFAULT NULL,
  `Age` int(11) DEFAULT NULL,
  `NumQualite` int(11) DEFAULT NULL,
  `NumVillage` int(11) NOT NULL,
  PRIMARY KEY (`NumHab`),
  KEY `NumQualite` (`NumQualite`),
  KEY `NumVillage` (`NumVillage`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `habitant`
--

INSERT INTO `habitant` (`NumHab`, `Nom`, `Age`, `NumQualite`, `NumVillage`) VALUES
(1, 'Abraracourcix', 65, 1, 1),
(2, 'Amnésix', 56, 2, 7),
(3, 'Barometrix', 68, 2, 3),
(4, 'Panoramix', 79, 2, 1),
(5, 'Assurancetourix', 53, 3, 1),
(6, 'Zérozérosix', 75, 2, 4),
(7, 'Astérix', 35, 4, 1),
(8, 'Bellodalix', 32, 4, 7),
(9, 'Cétyounix', 32, 4, 4),
(10, 'Homéopatix', 48, 5, 6),
(11, 'Obélix', 38, 6, 1),
(12, 'Plantaquatix', 30, 5, 5),
(13, 'Moralélastix', 67, 1, 2),
(14, 'Pneumatix', 26, 7, 1),
(15, 'Pronostix', 35, 4, 5),
(16, 'Goudurix', 38, 4, 2),
(17, 'Océanix', 40, 5, 5),
(18, 'Asdepix', 53, 1, 5),
(19, 'Eponine', 48, 8, 2),
(20, 'Falbala', 26, 9, 1),
(21, 'Gélatine', 65, NULL, 6),
(22, 'Fanzine', 21, NULL, 3);

-- --------------------------------------------------------

--
-- Structure de la table `potion`
--

CREATE TABLE IF NOT EXISTS `potion` (
  `NumPotion` int(11) NOT NULL DEFAULT '0',
  `LibPotion` varchar(40) DEFAULT NULL,
  `Formule` varchar(30) DEFAULT NULL,
  `ConstituantPrincipal` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`NumPotion`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `potion`
--

INSERT INTO `potion` (`NumPotion`, `LibPotion`, `Formule`, `ConstituantPrincipal`) VALUES
(1, 'Potion magique n°1', NULL, 'Gui'),
(2, 'Potion magique n°2', '4V3C2VA', 'Vin'),
(3, 'Potion magique n°3', '2C1B', 'Calva'),
(4, 'Potion Zen', NULL, 'Jus de Betterave'),
(5, 'Potion Anti Douleur', '5C3J1T', 'Calva');

-- --------------------------------------------------------

--
-- Structure de la table `province`
--

CREATE TABLE IF NOT EXISTS `province` (
  `NumProvince` int(11) NOT NULL DEFAULT '0',
  `NomProvince` varchar(30) DEFAULT NULL,
  `NomGouverneur` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`NumProvince`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `province`
--

INSERT INTO `province` (`NumProvince`, `NomProvince`, `NomGouverneur`) VALUES
(1, 'Armorique', 'Garovirus'),
(2, 'Averne', 'Nenpeuplus'),
(3, 'Aquitaine', 'Yenapus');

-- --------------------------------------------------------

--
-- Structure de la table `qualite`
--

CREATE TABLE IF NOT EXISTS `qualite` (
  `NumQualite` int(11) NOT NULL DEFAULT '0',
  `LibQualite` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`NumQualite`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `qualite`
--

INSERT INTO `qualite` (`NumQualite`, `LibQualite`) VALUES
(1, 'Chef'),
(2, 'Druide'),
(3, 'Barde'),
(4, 'Guerrier'),
(5, 'Chasseur'),
(6, 'Livreur de menhirs'),
(7, 'Facteur'),
(8, 'Poissonnière'),
(9, 'Serveuse');

-- --------------------------------------------------------

--
-- Structure de la table `resserre`
--

CREATE TABLE IF NOT EXISTS `resserre` (
  `NumResserre` int(11) NOT NULL DEFAULT '0',
  `NomResserre` varchar(30) DEFAULT NULL,
  `Superficie` int(11) DEFAULT NULL,
  `NumVillage` int(11) DEFAULT NULL,
  PRIMARY KEY (`NumResserre`),
  KEY `NumVillage` (`NumVillage`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `resserre`
--

INSERT INTO `resserre` (`NumResserre`, `NomResserre`, `Superficie`, `NumVillage`) VALUES
(1, 'Albinus', 720, 4),
(2, 'Vercingetorix', 500, 6),
(3, 'Sintrof', 895, 1);

-- --------------------------------------------------------

--
-- Structure de la table `trophee`
--

CREATE TABLE IF NOT EXISTS `trophee` (
  `NumTrophee` int(11) NOT NULL DEFAULT '0',
  `DatePrise` datetime DEFAULT NULL,
  `CodeCat` char(3) DEFAULT NULL,
  `NumPreneur` int(11) DEFAULT NULL,
  `NumResserre` int(11) DEFAULT NULL,
  PRIMARY KEY (`NumTrophee`),
  KEY `CodeCat` (`CodeCat`),
  KEY `NumPreneur` (`NumPreneur`),
  KEY `NumResserre` (`NumResserre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `trophee`
--

INSERT INTO `trophee` (`NumTrophee`, `DatePrise`, `CodeCat`, `NumPreneur`, `NumResserre`) VALUES
(1, '2052-04-03 00:00:00', 'BLE', 7, 3),
(2, '2052-04-03 00:00:00', 'BLT', 11, 3),
(3, '2052-05-05 00:00:00', 'CDN', 15, 1),
(4, '2052-05-05 00:00:00', 'CLE', 16, 2),
(5, '2052-06-06 00:00:00', 'CCN', 16, 2),
(6, '2052-06-06 00:00:00', 'BLT', 8, 1),
(7, '2052-08-18 00:00:00', 'CCN', 8, 1),
(8, '2052-09-20 00:00:00', 'CLT', 1, 3),
(9, '2052-10-23 00:00:00', 'CDN', 7, 2),
(10, '2052-10-23 00:00:00', 'CLE', 16, 1);

-- --------------------------------------------------------

--
-- Structure de la table `village`
--

CREATE TABLE IF NOT EXISTS `village` (
  `NumVillage` int(11) NOT NULL DEFAULT '0',
  `NomVillage` varchar(30) DEFAULT NULL,
  `NbHuttes` int(11) DEFAULT NULL,
  `NumProvince` int(11) DEFAULT NULL,
  PRIMARY KEY (`NumVillage`),
  KEY `NumProvince` (`NumProvince`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Contenu de la table `village`
--

INSERT INTO `village` (`NumVillage`, `NomVillage`, `NbHuttes`, `NumProvince`) VALUES
(1, 'Aquilona', 52, 1),
(2, 'Lutèce', 25, 2),
(3, 'Aginum', 33, 3),
(4, 'Calendes Aquae', 42, 2),
(5, 'Condate', 38, 1),
(6, 'Gergovie', 55, 3),
(7, 'Aquae Calidae', 35, 2);

--
-- Contraintes pour les tables exportées
--

--
-- Contraintes pour la table `fabriquer`
--
ALTER TABLE `fabriquer`
  ADD CONSTRAINT `fabriquer_ibfk_1` FOREIGN KEY (`NumPotion`) REFERENCES `potion` (`NumPotion`),
  ADD CONSTRAINT `fabriquer_ibfk_2` FOREIGN KEY (`NumHab`) REFERENCES `habitant` (`NumHab`);

--
-- Contraintes pour la table `habitant`
--
ALTER TABLE `habitant`
  ADD CONSTRAINT `habitant_ibfk_1` FOREIGN KEY (`NumQualite`) REFERENCES `qualite` (`NumQualite`),
  ADD CONSTRAINT `habitant_ibfk_2` FOREIGN KEY (`NumVillage`) REFERENCES `village` (`NumVillage`);

--
-- Contraintes pour la table `resserre`
--
ALTER TABLE `resserre`
  ADD CONSTRAINT `resserre_ibfk_1` FOREIGN KEY (`NumVillage`) REFERENCES `village` (`NumVillage`);

--
-- Contraintes pour la table `trophee`
--
ALTER TABLE `trophee`
  ADD CONSTRAINT `trophee_ibfk_1` FOREIGN KEY (`CodeCat`) REFERENCES `categorie` (`CodeCat`),
  ADD CONSTRAINT `trophee_ibfk_2` FOREIGN KEY (`NumPreneur`) REFERENCES `habitant` (`NumHab`),
  ADD CONSTRAINT `trophee_ibfk_3` FOREIGN KEY (`NumResserre`) REFERENCES `resserre` (`NumResserre`);

--
-- Contraintes pour la table `village`
--
ALTER TABLE `village`
  ADD CONSTRAINT `village_ibfk_1` FOREIGN KEY (`NumProvince`) REFERENCES `province` (`NumProvince`);
