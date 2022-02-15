-- phpMyAdmin SQL Dump
-- version 4.7.4
-- https://www.phpmyadmin.net/
--
-- Hôte : 127.0.0.1:3306
-- Généré le :  jeu. 16 mai 2019 à 15:32
-- Version du serveur :  5.7.19
-- Version de PHP :  5.6.31

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de données :  `icaredb`
--

-- --------------------------------------------------------

--
-- Structure de la table `analyse`
--

DROP TABLE IF EXISTS `analyse`;
CREATE TABLE IF NOT EXISTS `analyse` (
  `idanalyse` int(11) NOT NULL,
  `ordonnance_medecin_idmedecin` int(11) NOT NULL,
  `date` varchar(45) NOT NULL,
  `description` varchar(150) NOT NULL,
  `resultats` varchar(45) NOT NULL,
  PRIMARY KEY (`idanalyse`,`ordonnance_medecin_idmedecin`),
  UNIQUE KEY `idanalyse_UNIQUE` (`idanalyse`),
  KEY `fk_analyse_ordonnance1_idx` (`ordonnance_medecin_idmedecin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `disponibilite`
--

DROP TABLE IF EXISTS `disponibilite`;
CREATE TABLE IF NOT EXISTS `disponibilite` (
  `iddisponibilite` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  `medecin_idmedecin` int(11) NOT NULL,
  PRIMARY KEY (`iddisponibilite`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `disponibilite`
--

INSERT INTO `disponibilite` (`iddisponibilite`, `date`, `heure`, `medecin_idmedecin`) VALUES
(1, '2019-06-10', '15:00:00', 1),
(2, '2019-06-05', '17:00:00', 2),
(3, '2019-06-01', '17:00:00', 2);

-- --------------------------------------------------------

--
-- Structure de la table `medecin`
--

DROP TABLE IF EXISTS `medecin`;
CREATE TABLE IF NOT EXISTS `medecin` (
  `idmedecin` int(11) NOT NULL,
  `nom` varchar(45) NOT NULL,
  `prenom` varchar(75) NOT NULL,
  `mail` varchar(75) NOT NULL,
  `numero` varchar(45) NOT NULL,
  `specialite` varchar(75) NOT NULL,
  `genre` varchar(45) NOT NULL,
  PRIMARY KEY (`idmedecin`),
  UNIQUE KEY `idmedecin_UNIQUE` (`idmedecin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `medecin`
--

INSERT INTO `medecin` (`idmedecin`, `nom`, `prenom`, `mail`, `numero`, `specialite`, `genre`) VALUES
(1, 'Diop', 'Ibrahima Bara', '', '338210313', 'Cardiologue', 'Homme'),
(2, 'Ghozayel', 'Farid', '', '338215051', 'Cardiologue', 'Homme'),
(3, 'Colaser', '', '', '', 'Ophtalmologue ', ''),
(4, 'Attye', 'Talal', '', '338210586', 'Ophtalmologue', 'Homme'),
(5, 'Mevo', 'Elwin', 'elwinmevo@gmail.com', '771234566', 'Cardiologue', 'Homme');

-- --------------------------------------------------------

--
-- Structure de la table `medicament`
--

DROP TABLE IF EXISTS `medicament`;
CREATE TABLE IF NOT EXISTS `medicament` (
  `nom` varchar(45) NOT NULL,
  `posologie` varchar(100) NOT NULL,
  `ordonnance_medecin_idmedecin` int(11) NOT NULL,
  `idmedicament` int(11) NOT NULL,
  PRIMARY KEY (`ordonnance_medecin_idmedecin`,`idmedicament`),
  UNIQUE KEY `idmedicament_UNIQUE` (`idmedicament`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `ordonnance`
--

DROP TABLE IF EXISTS `ordonnance`;
CREATE TABLE IF NOT EXISTS `ordonnance` (
  `medecin_idmedecin` int(11) NOT NULL,
  `date` date NOT NULL,
  PRIMARY KEY (`medecin_idmedecin`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `rdv`
--

DROP TABLE IF EXISTS `rdv`;
CREATE TABLE IF NOT EXISTS `rdv` (
  `medecin_idmedecin` int(11) NOT NULL,
  `idrdv` int(11) NOT NULL,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  PRIMARY KEY (`medecin_idmedecin`,`idrdv`),
  UNIQUE KEY `idrdv_UNIQUE` (`idrdv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Structure de la table `tension`
--

DROP TABLE IF EXISTS `tension`;
CREATE TABLE IF NOT EXISTS `tension` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `heure` time NOT NULL,
  `diastole` int(100) NOT NULL,
  `systole` int(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `id` (`id`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `tension`
--

INSERT INTO `tension` (`id`, `date`, `heure`, `diastole`, `systole`) VALUES
(1, '2019-05-08', '14:23:31', 12, 6),
(2, '2019-05-08', '15:00:30', 12, 3),
(3, '2019-05-08', '15:49:49', 6, 12),
(4, '2019-05-08', '16:03:04', 9, 11),
(5, '2019-05-08', '18:03:28', 10, 17),
(6, '2019-05-08', '18:05:51', 97, 17),
(7, '2019-05-08', '18:07:06', 97, 16),
(8, '2019-05-08', '18:07:57', 97, 17),
(9, '2019-05-08', '18:31:08', 5, 12),
(10, '2019-05-15', '16:15:53', 0, 0),
(11, '2019-05-15', '20:28:58', 9, 13),
(12, '2019-05-16', '11:35:27', 0, 0),
(13, '2019-05-16', '15:12:57', 9, 10);

-- --------------------------------------------------------

--
-- Structure de la table `utilisateur`
--

DROP TABLE IF EXISTS `utilisateur`;
CREATE TABLE IF NOT EXISTS `utilisateur` (
  `idutilisateur` int(11) NOT NULL AUTO_INCREMENT,
  `prenom` varchar(100) NOT NULL,
  `genre` varchar(45) NOT NULL,
  `poids` varchar(45) NOT NULL,
  `taille` varchar(45) NOT NULL,
  `allergie` varchar(125) NOT NULL,
  PRIMARY KEY (`idutilisateur`),
  UNIQUE KEY `idutilisateur_UNIQUE` (`idutilisateur`)
) ENGINE=InnoDB AUTO_INCREMENT=64 DEFAULT CHARSET=utf8;

--
-- Déchargement des données de la table `utilisateur`
--

INSERT INTO `utilisateur` (`idutilisateur`, `prenom`, `genre`, `poids`, `taille`, `allergie`) VALUES
(63, 'Amy', 'Femme', '45.0', '167', 'rien');

--
-- Contraintes pour les tables déchargées
--

--
-- Contraintes pour la table `analyse`
--
ALTER TABLE `analyse`
  ADD CONSTRAINT `fk_analyse_ordonnance1` FOREIGN KEY (`ordonnance_medecin_idmedecin`) REFERENCES `ordonnance` (`medecin_idmedecin`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `medicament`
--
ALTER TABLE `medicament`
  ADD CONSTRAINT `fk_medicament_ordonnance1` FOREIGN KEY (`ordonnance_medecin_idmedecin`) REFERENCES `ordonnance` (`medecin_idmedecin`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `ordonnance`
--
ALTER TABLE `ordonnance`
  ADD CONSTRAINT `fk_ordonnance_medecin` FOREIGN KEY (`medecin_idmedecin`) REFERENCES `medecin` (`idmedecin`) ON DELETE NO ACTION ON UPDATE NO ACTION;

--
-- Contraintes pour la table `rdv`
--
ALTER TABLE `rdv`
  ADD CONSTRAINT `fk_rdv_medecin1` FOREIGN KEY (`medecin_idmedecin`) REFERENCES `medecin` (`idmedecin`) ON DELETE NO ACTION ON UPDATE NO ACTION;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
