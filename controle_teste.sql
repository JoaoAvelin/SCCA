-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 08-Dez-2022 às 14:32
-- Versão do servidor: 10.4.24-MariaDB
-- versão do PHP: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `controle_teste`
--

-- --------------------------------------------------------

--
-- Estrutura da tabela `beneficio`
--

CREATE TABLE `beneficio` (
  `id` int(10) NOT NULL,
  `NUMERO_BENEFICIO` text NOT NULL,
  `TIPO_DE_ACONTECIMENTO` text NOT NULL,
  `FONTE_DE_ACAO` text NOT NULL,
  `ESPECIE` text NOT NULL,
  `NUMERO_PROTOCOLO` text NOT NULL,
  `NOME_SEGURADO` text NOT NULL,
  `CPF_SEGURADO` text NOT NULL,
  `NIT` text NOT NULL,
  `CEP` text NOT NULL,
  `RUA` text NOT NULL,
  `BAIRRO` text NOT NULL,
  `ESTADO` text NOT NULL,
  `MUNICIPIO` text NOT NULL,
  `NOME_RESPONSAVEL` text NOT NULL,
  `CPF_CNPJ_RESPONSAVEL` text NOT NULL,
  `VALOR_DIVIDA` text NOT NULL,
  `VALOR_CALCULADO` text NOT NULL,
  `VALOR_DE_ENTRADA` text NOT NULL,
  `PARCELAS_PAGAS` text NOT NULL,
  `TOTAL_DE_PARCELAS` text NOT NULL,
  `DATA_DA_COBRANÇA` text NOT NULL,
  `DATA_DO_CALCULO` text NOT NULL,
  `REGRESSIVA` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Estrutura da tabela `login`
--

CREATE TABLE `login` (
  `id` int(10) NOT NULL,
  `matricula` text NOT NULL,
  `password` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Índices para tabelas despejadas
--

--
-- Índices para tabela `beneficio`
--
ALTER TABLE `beneficio`
  ADD PRIMARY KEY (`id`);

--
-- Índices para tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `beneficio`
--
ALTER TABLE `beneficio`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `id` int(10) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
