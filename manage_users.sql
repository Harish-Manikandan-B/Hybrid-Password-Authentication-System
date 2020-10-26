-- phpMyAdmin SQL Dump
-- version 4.8.5
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Sep 05, 2020 at 11:57 AM
-- Server version: 10.1.40-MariaDB
-- PHP Version: 7.3.5

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `semester-8`
--

-- --------------------------------------------------------

--
-- Table structure for table `manage_users`
--

CREATE TABLE `manage_users` (
  `username` varchar(255) NOT NULL,
  `encrypted_string` varchar(255) NOT NULL,
  `path` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `manage_users`
--

INSERT INTO `manage_users` (`username`, `encrypted_string`, `path`) VALUES
('guest1', 'gAAAAABemxmraRhDZhq51CzV8oZ1p21oHyAiNf2gzvwyKdRGV6eyzYCqZquWdE_kEH8MSXqc3DmKkK_B0_IyeJSVZFjbv84Ygq_lvv4QPGjysRdPzoXJ3rU=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT REPORT\\screenshots\\FINAL_CODE\\guest1'),
('harish', 'gAAAAABemx18AHl1U2aXUdYIM8XY2eTulvW13fgtO-4d7VD-xn2o_TaZuylu8VU9_Lx_Vjo7vRdDcZmMGgm02_5yH7T55Pbi24taFRiEzn-GuQ9qTfmRBgw=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT REPORT\\screenshots\\FINAL_CODE\\harish'),
('abisek', 'gAAAAABeu-7U5z_lezfWUfN0BEkagfGg6E_bR4DaBoRAnYmi6bL8S0FPJNCHh3nSIivAdt2QSmw2zCbmTwEvMkf29oVjH01tRAFPk7xBzsaRoKNda4iOfJE=', 'C:\\Users\\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\abisek'),
('dharmesh', 'gAAAAABeu-_-dmzpG797LgEkq0ZotacQ6iP7JF6ssGaiVXzVk_65ldd2uoY0XLZFjnw1qHjKbH0oydriU5EvHQ3PmBrLnQRyp5_QOv21GWFjjdnX2MiU5rY=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\dharmesh'),
('jack', 'gAAAAABeu_FDMw0F5JUEbJJupc_8W76gMXeNO-41YXNPiy8fy3F-t0MFxxbyrc2D20uJJ0MOUwDShlc5z32bhwHpfQmZsowGViJ-r9ced57vhFpzcmk5GbI=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\jack'),
('bill', 'gAAAAABeu_IqmBf_IY7EeXk6H6aj3pNRYPHwHQc1HFkHrSEe8gbWJJ15fOC4hoDH9WkABox7WUFUV1NqyCzfdgCIGelyLS68FePmQ7ELMMBPvZ5yvtxTX-M=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\bill'),
('guest2', 'gAAAAABeu_Nl9v_xpedaUadttKXvhiNCX3ZajU8XV_bHAD8wekVicoHly4hnt5XJzJSNBAl4FyC9PY8YJyHwvxgemh94b_0uVtslGxdXeT8sJwVc-Ol3aig=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\guest2'),
('sherlock', 'gAAAAABfS9QOlMT8FABxkcdPNoCid0AOkrkPxaVC2BqArysbqE9oYNnsME-mjXUqM5s71EqGGAz0PZrjaVhBXgCx2obqSlqdEX7r-EOtm0F06IUQA8YmKmU=', 'C:\\Users\\ABISEK\\Desktop\\PROJECT COMPLETE\\FINAL_CODE\\sherlock');
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
