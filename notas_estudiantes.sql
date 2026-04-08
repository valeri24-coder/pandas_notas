-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 16-03-2026 a las 15:50:48
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `notas_estudiantes`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `estudiantes`
--

CREATE TABLE `estudiantes` (
  `id_estudiantes` int(11) NOT NULL,
  `nombre_estu` varchar(40) NOT NULL,
  `edad_estu` int(11) NOT NULL,
  `carrera` varchar(40) NOT NULL,
  `nota1` decimal(10,0) NOT NULL,
  `nota2` decimal(10,0) NOT NULL,
  `nota3` decimal(10,0) NOT NULL,
  `promedio` decimal(10,0) NOT NULL,
  `desempeno` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `estudiantes`
--

INSERT INTO `estudiantes` (`id_estudiantes`, `nombre_estu`, `edad_estu`, `carrera`, `nota1`, `nota2`, `nota3`, `promedio`, `desempeno`) VALUES
(1, 'Paula', 21, 'Fisica', 4, 4, 3, 3, 'Bueno'),
(2, 'Ana', 18, 'Ingenieria', 2, 5, 3, 3, 'Regular'),
(3, 'Maria', 23, 'Ingenieria', 5, 4, 3, 4, 'Bueno'),
(4, 'Luis', 22, 'Matematicas', 2, 3, 4, 3, 'Regular'),
(5, 'Ana', 21, 'Ingenieria', 5, 5, 5, 5, 'Excelente'),
(6, 'Maria', 23, 'Ingenieria', 4, 3, 3, 3, 'Regular'),
(7, 'Ana', 20, 'Fisica', 2, 3, 3, 2, 'Regular'),
(8, 'Luis', 20, 'Ingenieria', 4, 2, 4, 3, 'Bueno'),
(9, 'Luis', 23, 'Fisica', 4, 3, 2, 3, 'Regular'),
(10, 'Luis', 22, 'Ingenieria', 3, 3, 2, 2, 'Regular'),
(11, 'Ana', 20, 'Fisica', 5, 3, 2, 3, 'Regular'),
(12, 'Carlos', 19, 'Fisica', 4, 2, 2, 2, 'Regular'),
(13, 'Luis', 21, 'Fisica', 2, 5, 5, 4, 'Bueno'),
(14, 'Maria', 22, 'Fisica', 5, 2, 2, 3, 'Regular'),
(15, 'Jose', 18, 'Fisica', 4, 3, 2, 3, 'Regular'),
(16, 'Paula', 21, 'Fisica', 5, 4, 2, 3, 'Bueno'),
(17, 'Luis', 22, 'Ingenieria', 2, 3, 2, 2, 'Deficiente'),
(18, 'Maria', 22, 'Matematicas', 5, 5, 2, 4, 'Bueno'),
(19, 'Luis', 20, 'Matematicas', 5, 4, 5, 4, 'Excelente'),
(20, 'Ana', 22, 'Ingenieria', 2, 3, 4, 3, 'Regular'),
(21, 'Ana', 20, 'Fisica', 3, 5, 2, 3, 'Bueno'),
(22, 'Carlos', 20, 'Ingenieria', 2, 4, 5, 3, 'Bueno'),
(23, 'Luis', 23, 'Fisica', 3, 2, 5, 3, 'Bueno'),
(24, 'Ana', 21, 'Ingenieria', 3, 5, 4, 4, 'Bueno'),
(25, 'Carlos', 19, 'Matematicas', 4, 3, 3, 3, 'Regular'),
(26, 'Maria', 18, 'Fisica', 3, 3, 5, 3, 'Bueno'),
(27, 'Carlos', 22, 'Matematicas', 3, 4, 2, 3, 'Regular'),
(28, 'Luis', 21, 'Ingenieria', 2, 3, 5, 3, 'Regular'),
(29, 'Jose', 20, 'Matematicas', 4, 3, 3, 3, 'Regular'),
(30, 'Ana', 19, 'Ingenieria', 3, 2, 3, 3, 'Regular'),
(31, 'Maria', 18, 'Ingenieria', 5, 4, 4, 4, 'Excelente'),
(32, 'Maria', 23, 'Fisica', 2, 3, 4, 3, 'Regular'),
(33, 'Jose', 18, 'Matematicas', 5, 3, 4, 4, 'Bueno'),
(34, 'Ana', 18, 'Matematicas', 5, 2, 5, 4, 'Bueno'),
(35, 'Jose', 20, 'Fisica', 2, 2, 2, 2, 'Deficiente'),
(36, 'Paula', 23, 'Fisica', 5, 5, 3, 4, 'Bueno'),
(37, 'Jose', 18, 'Fisica', 4, 3, 3, 3, 'Bueno'),
(38, 'Ana', 21, 'Fisica', 5, 3, 5, 4, 'Excelente'),
(39, 'Ana', 22, 'Ingenieria', 3, 5, 2, 3, 'Bueno'),
(40, 'Ana', 23, 'Fisica', 3, 2, 2, 2, 'Regular'),
(41, 'Luis', 18, 'Fisica', 3, 3, 4, 3, 'Bueno'),
(42, 'Luis', 23, 'Fisica', 3, 4, 3, 3, 'Bueno'),
(43, 'Ana', 22, 'Fisica', 2, 5, 3, 3, 'Regular'),
(44, 'Maria', 21, 'Fisica', 5, 5, 4, 4, 'Excelente'),
(45, 'Paula', 20, 'Matematicas', 2, 3, 2, 2, 'Deficiente'),
(46, 'Ana', 18, 'Fisica', 5, 2, 2, 3, 'Regular'),
(48, 'carlita', 18, 'Ingenieria', 3, 5, 3, 3, 'Bueno'),
(50, 'Maria Lopez', 35, 'Administracion Empresas', 4, 1, 3, 3, 'Bajo'),
(51, 'Valentina Mora', 28, 'Derecho', 1, 1, 3, 2, 'Bajo'),
(52, 'Andres Torres', 27, 'Derecho', 5, 1, 5, 4, 'Regular'),
(53, 'Valentina Mora', 24, 'Contaduria', 3, 3, 1, 3, 'Bajo'),
(54, 'Juan Perez', 24, 'Psicologia', 0, 3, 1, 1, 'Bajo'),
(55, 'Andres Torres', 30, 'Arquitectura', 0, 4, 2, 2, 'Bajo'),
(56, 'Sofia Herrera', 22, 'Medicina', 3, 1, 3, 3, 'Bajo'),
(57, 'Felipe Vargas', 23, 'Arquitectura', 1, 4, 0, 2, 'Bajo'),
(58, 'Felipe Vargas', 15, 'Administracion Empresas', 3, 1, 2, 2, 'Bajo'),
(59, 'Daniela Cruz', 13, 'Derecho', 1, 1, 4, 2, 'Bajo'),
(60, 'Jose Castro', 17, 'Medicina', 5, 1, 4, 3, 'Regular'),
(61, 'Ana Rodriguez', 17, 'Ingenieria Sistemas', 4, 3, 4, 4, 'Regular'),
(62, 'Laura Gutierrez', 21, 'Ingenieria Industrial', 2, 2, 1, 2, 'Bajo'),
(63, 'Daniela Cruz', 25, 'Administracion Empresas', 4, 5, 3, 4, 'Bueno'),
(64, 'Felipe Vargas', 27, 'Contaduria', 1, 3, 5, 3, 'Regular'),
(65, 'Valentina Mora', 0, 'Ingenieria Industrial', 4, 3, 5, 4, 'Bueno'),
(66, 'Maria Lopez', 17, 'Ingenieria Industrial', 4, 0, 2, 2, 'Bajo'),
(67, 'Luis Martinez', 15, 'Arquitectura', 1, 1, 3, 2, 'Bajo'),
(68, 'Laura Gutierrez', 24, 'Ingenieria Sistemas', 2, 3, 3, 3, 'Bajo'),
(69, 'Laura Gutierrez', 6, 'Psicologia', 4, 3, 0, 2, 'Bajo'),
(70, 'Sebastian Ruiz', 29, 'Ingenieria Industrial', 5, 2, 2, 3, 'Bajo'),
(72, 'Maria Lopez', 35, 'Administracion Empresas', 4, 1, 3, 3, 'Bajo'),
(73, 'Valentina Mora', 28, 'Derecho', 1, 1, 3, 2, 'Bajo'),
(74, 'Andres Torres', 27, 'Derecho', 5, 1, 5, 4, 'Regular'),
(75, 'Valentina Mora', 24, 'Contaduria', 3, 3, 1, 3, 'Bajo'),
(76, 'Juan Perez', 24, 'Psicologia', 0, 3, 1, 1, 'Bajo'),
(77, 'Andres Torres', 30, 'Arquitectura', 0, 4, 2, 2, 'Bajo'),
(78, 'Sofia Herrera', 22, 'Medicina', 3, 1, 3, 3, 'Bajo'),
(79, 'Felipe Vargas', 23, 'Arquitectura', 1, 4, 0, 2, 'Bajo'),
(80, 'Felipe Vargas', 15, 'Administracion Empresas', 3, 1, 2, 2, 'Bajo'),
(81, 'Daniela Cruz', 13, 'Derecho', 1, 1, 4, 2, 'Bajo'),
(82, 'Jose Castro', 17, 'Medicina', 5, 1, 4, 3, 'Regular'),
(83, 'Ana Rodriguez', 17, 'Ingenieria Sistemas', 4, 3, 4, 4, 'Regular'),
(84, 'Laura Gutierrez', 21, 'Ingenieria Industrial', 2, 2, 1, 2, 'Bajo'),
(85, 'Daniela Cruz', 25, 'Administracion Empresas', 4, 5, 3, 4, 'Bueno'),
(86, 'Felipe Vargas', 27, 'Contaduria', 1, 3, 5, 3, 'Regular'),
(87, 'Valentina Mora', 0, 'Ingenieria Industrial', 4, 3, 5, 4, 'Bueno'),
(88, 'Maria Lopez', 17, 'Ingenieria Industrial', 4, 0, 2, 2, 'Bajo'),
(89, 'Luis Martinez', 15, 'Arquitectura', 1, 1, 3, 2, 'Bajo'),
(90, 'Laura Gutierrez', 24, 'Ingenieria Sistemas', 2, 3, 3, 3, 'Bajo'),
(91, 'Laura Gutierrez', 6, 'Psicologia', 4, 3, 0, 2, 'Bajo'),
(92, 'Sebastian Ruiz', 29, 'Ingenieria Industrial', 5, 2, 2, 3, 'Bajo'),
(93, 'Maria Lopez', 35, 'Administracion Empresas', 4, 1, 3, 3, 'Bajo'),
(94, 'Valentina Mora', 28, 'Derecho', 1, 1, 3, 2, 'Bajo'),
(95, 'Andres Torres', 27, 'Derecho', 5, 1, 5, 4, 'Regular'),
(96, 'Valentina Mora', 24, 'Contaduria', 3, 3, 1, 3, 'Bajo'),
(97, 'Juan Perez', 24, 'Psicologia', 0, 3, 1, 1, 'Bajo'),
(98, 'Andres Torres', 30, 'Arquitectura', 0, 4, 2, 2, 'Bajo'),
(99, 'Sofia Herrera', 22, 'Medicina', 3, 1, 3, 3, 'Bajo'),
(100, 'Felipe Vargas', 23, 'Arquitectura', 1, 4, 0, 2, 'Bajo'),
(101, 'Felipe Vargas', 15, 'Administracion Empresas', 3, 1, 2, 2, 'Bajo'),
(102, 'Daniela Cruz', 13, 'Derecho', 1, 1, 4, 2, 'Bajo'),
(103, 'Jose Castro', 17, 'Medicina', 5, 1, 4, 3, 'Regular'),
(104, 'Ana Rodriguez', 17, 'Ingenieria Sistemas', 4, 3, 4, 4, 'Regular'),
(105, 'Laura Gutierrez', 21, 'Ingenieria Industrial', 2, 2, 1, 2, 'Bajo'),
(106, 'Daniela Cruz', 25, 'Administracion Empresas', 4, 5, 3, 4, 'Bueno'),
(107, 'Felipe Vargas', 27, 'Contaduria', 1, 3, 5, 3, 'Regular'),
(108, 'Valentina Mora', 0, 'Ingenieria Industrial', 4, 3, 5, 4, 'Bueno'),
(109, 'Maria Lopez', 17, 'Ingenieria Industrial', 4, 0, 2, 2, 'Bajo'),
(110, 'Luis Martinez', 15, 'Arquitectura', 1, 1, 3, 2, 'Bajo'),
(111, 'Laura Gutierrez', 24, 'Ingenieria Sistemas', 2, 3, 3, 3, 'Bajo'),
(112, 'Laura Gutierrez', 6, 'Psicologia', 4, 3, 0, 2, 'Bajo'),
(113, 'Sebastian Ruiz', 29, 'Ingenieria Industrial', 5, 2, 2, 3, 'Bajo'),
(114, 'Maria Lopez', 35, 'Administracion Empresas', 4, 1, 3, 3, 'Bajo'),
(115, 'Valentina Mora', 28, 'Derecho', 1, 1, 3, 2, 'Bajo'),
(116, 'Andres Torres', 27, 'Derecho', 5, 1, 5, 4, 'Regular'),
(117, 'Valentina Mora', 24, 'Contaduria', 3, 3, 1, 3, 'Bajo'),
(118, 'Juan Perez', 24, 'Psicologia', 0, 3, 1, 1, 'Bajo'),
(119, 'Andres Torres', 30, 'Arquitectura', 0, 4, 2, 2, 'Bajo'),
(120, 'Sofia Herrera', 22, 'Medicina', 3, 1, 3, 3, 'Bajo'),
(121, 'Felipe Vargas', 23, 'Arquitectura', 1, 4, 0, 2, 'Bajo'),
(122, 'Felipe Vargas', 15, 'Administracion Empresas', 3, 1, 2, 2, 'Bajo'),
(123, 'Daniela Cruz', 13, 'Derecho', 1, 1, 4, 2, 'Bajo'),
(124, 'Jose Castro', 17, 'Medicina', 5, 1, 4, 3, 'Regular'),
(125, 'Ana Rodriguez', 17, 'Ingenieria Sistemas', 4, 3, 4, 4, 'Regular'),
(126, 'Laura Gutierrez', 21, 'Ingenieria Industrial', 2, 2, 1, 2, 'Bajo'),
(127, 'Daniela Cruz', 25, 'Administracion Empresas', 4, 5, 3, 4, 'Bueno'),
(128, 'Felipe Vargas', 27, 'Contaduria', 1, 3, 5, 3, 'Regular'),
(129, 'Valentina Mora', 0, 'Ingenieria Industrial', 4, 3, 5, 4, 'Bueno'),
(130, 'Maria Lopez', 17, 'Ingenieria Industrial', 4, 0, 2, 2, 'Bajo'),
(131, 'Luis Martinez', 15, 'Arquitectura', 1, 1, 3, 2, 'Bajo'),
(132, 'Laura Gutierrez', 24, 'Ingenieria Sistemas', 2, 3, 3, 3, 'Bajo'),
(133, 'Laura Gutierrez', 6, 'Psicologia', 4, 3, 0, 2, 'Bajo'),
(134, 'Sebastian Ruiz', 29, 'Ingenieria Industrial', 5, 2, 2, 3, 'Bajo');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `usuarios`
--

CREATE TABLE `usuarios` (
  `id_usuario` int(11) NOT NULL,
  `username` varchar(40) NOT NULL,
  `passworduser` varchar(255) NOT NULL,
  `rolusu` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `usuarios`
--

INSERT INTO `usuarios` (`id_usuario`, `username`, `passworduser`, `rolusu`) VALUES
(1, 'valerin', '12345', 'administrador'),
(2, 'dayana', '123', 'usuario');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  ADD PRIMARY KEY (`id_estudiantes`);

--
-- Indices de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  ADD PRIMARY KEY (`id_usuario`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `estudiantes`
--
ALTER TABLE `estudiantes`
  MODIFY `id_estudiantes` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=136;

--
-- AUTO_INCREMENT de la tabla `usuarios`
--
ALTER TABLE `usuarios`
  MODIFY `id_usuario` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
