-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Mar 17, 2018 at 09:36 AM
-- Server version: 5.7.21-0ubuntu0.16.04.1
-- PHP Version: 7.0.25-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hospital`
--
CREATE DATABASE IF NOT EXISTS `hospital` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `hospital`;

-- --------------------------------------------------------

--
-- Table structure for table `asistencia`
--

CREATE TABLE `asistencia` (
  `idvisitante` int(10) UNSIGNED NOT NULL,
  `identificacion` int(15) NOT NULL,
  `idmenor` int(15) DEFAULT NULL,
  `dispositivo` int(5) NOT NULL,
  `fechahorainicio` datetime DEFAULT NULL,
  `fechahorafin` datetime DEFAULT NULL,
  `tipo` enum('mayor','menor') DEFAULT NULL,
  `numeromenores` int(1) DEFAULT NULL,
  `estado` enum('E','S') DEFAULT NULL,
  `idcama` int(10) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `asistencia`
--

INSERT INTO `asistencia` (`idvisitante`, `identificacion`, `idmenor`, `dispositivo`, `fechahorainicio`, `fechahorafin`, `tipo`, `numeromenores`, `estado`, `idcama`) VALUES
(1, 1014280452, 123456, 1, '2018-03-16 16:16:58', '2018-03-16 16:21:47', 'menor', 1, 'S', 21457),
(2, 1014280452, 123456, 1, '2018-03-16 16:22:04', '2018-03-16 16:22:21', 'menor', 1, 'S', 21457),
(3, 1014280452, 123456, 1, '2018-03-16 16:24:16', '2018-03-16 16:24:49', 'menor', 1, 'S', 21457);

-- --------------------------------------------------------

--
-- Table structure for table `cama`
--

CREATE TABLE `cama` (
  `idcama` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `idhabitacion` int(10) UNSIGNED NOT NULL,
  `iddependencia` int(10) UNSIGNED NOT NULL,
  `ocupacion` int(10) UNSIGNED NOT NULL,
  `disponibilidad` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `dependencia`
--

CREATE TABLE `dependencia` (
  `iddependencia` int(10) UNSIGNED NOT NULL,
  `nombres` varchar(45) NOT NULL,
  `hora_inicio` time NOT NULL,
  `hora_fin` time NOT NULL,
  `cupo` int(10) UNSIGNED NOT NULL,
  `menores` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `habitacion`
--

CREATE TABLE `habitacion` (
  `idhabitacion` int(10) UNSIGNED NOT NULL,
  `nombrehabitacion` varchar(45) NOT NULL,
  `piso` varchar(45) NOT NULL,
  `idtorre` int(10) UNSIGNED NOT NULL,
  `ncamas` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `menor`
--

CREATE TABLE `menor` (
  `idMenor` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `idadulto` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `operarios`
--

CREATE TABLE `operarios` (
  `idlogin` int(5) NOT NULL,
  `nombre` varchar(20) NOT NULL,
  `identificacion` int(12) NOT NULL,
  `privilegio` int(2) NOT NULL,
  `usuario` varchar(16) NOT NULL,
  `contrasena` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `torre`
--

CREATE TABLE `torre` (
  `idtorre` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `npisos` int(10) UNSIGNED NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Table structure for table `visitante`
--

CREATE TABLE `visitante` (
  `idvisitante` int(10) UNSIGNED NOT NULL,
  `nombre` varchar(45) NOT NULL,
  `idcama` int(10) UNSIGNED NOT NULL,
  `iddependencia` int(10) UNSIGNED NOT NULL,
  `NumMenores` tinyint(1) UNSIGNED DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Indexes for dumped tables
--

--
-- Indexes for table `asistencia`
--
ALTER TABLE `asistencia`
  ADD PRIMARY KEY (`idvisitante`);

--
-- Indexes for table `cama`
--
ALTER TABLE `cama`
  ADD PRIMARY KEY (`idcama`) USING BTREE,
  ADD KEY `idhabitacion` (`idhabitacion`),
  ADD KEY `iddependencia` (`iddependencia`);

--
-- Indexes for table `dependencia`
--
ALTER TABLE `dependencia`
  ADD PRIMARY KEY (`iddependencia`);

--
-- Indexes for table `habitacion`
--
ALTER TABLE `habitacion`
  ADD PRIMARY KEY (`idhabitacion`),
  ADD KEY `idtorre` (`idtorre`);

--
-- Indexes for table `menor`
--
ALTER TABLE `menor`
  ADD PRIMARY KEY (`idMenor`),
  ADD KEY `idadulto` (`idadulto`);

--
-- Indexes for table `operarios`
--
ALTER TABLE `operarios`
  ADD PRIMARY KEY (`idlogin`);

--
-- Indexes for table `torre`
--
ALTER TABLE `torre`
  ADD PRIMARY KEY (`idtorre`);

--
-- Indexes for table `visitante`
--
ALTER TABLE `visitante`
  ADD PRIMARY KEY (`idvisitante`),
  ADD KEY `idcama` (`idcama`),
  ADD KEY `iddependencia` (`iddependencia`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `asistencia`
--
ALTER TABLE `asistencia`
  MODIFY `idvisitante` int(10) UNSIGNED NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT for table `cama`
--
ALTER TABLE `cama`
  MODIFY `idcama` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `dependencia`
--
ALTER TABLE `dependencia`
  MODIFY `iddependencia` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `habitacion`
--
ALTER TABLE `habitacion`
  MODIFY `idhabitacion` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `menor`
--
ALTER TABLE `menor`
  MODIFY `idMenor` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `operarios`
--
ALTER TABLE `operarios`
  MODIFY `idlogin` int(5) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `torre`
--
ALTER TABLE `torre`
  MODIFY `idtorre` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT for table `visitante`
--
ALTER TABLE `visitante`
  MODIFY `idvisitante` int(10) UNSIGNED NOT NULL AUTO_INCREMENT;
--
-- Constraints for dumped tables
--

--
-- Constraints for table `cama`
--
ALTER TABLE `cama`
  ADD CONSTRAINT `cama_ibfk_1` FOREIGN KEY (`iddependencia`) REFERENCES `dependencia` (`iddependencia`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `cama_ibfk_2` FOREIGN KEY (`idhabitacion`) REFERENCES `habitacion` (`idhabitacion`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `habitacion`
--
ALTER TABLE `habitacion`
  ADD CONSTRAINT `habitacion_ibfk_1` FOREIGN KEY (`idtorre`) REFERENCES `torre` (`idtorre`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `menor`
--
ALTER TABLE `menor`
  ADD CONSTRAINT `menor_ibfk_1` FOREIGN KEY (`idadulto`) REFERENCES `visitante` (`idvisitante`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Constraints for table `visitante`
--
ALTER TABLE `visitante`
  ADD CONSTRAINT `visitante_ibfk_1` FOREIGN KEY (`idcama`) REFERENCES `cama` (`idcama`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `visitante_ibfk_2` FOREIGN KEY (`iddependencia`) REFERENCES `dependencia` (`iddependencia`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
