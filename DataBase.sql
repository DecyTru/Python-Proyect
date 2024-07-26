-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS ParkingLotDB;

-- Usar la base de datos
USE ParkingLotDB;

-- Crear la tabla de usuarios
CREATE TABLE IF NOT EXISTS usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    password VARCHAR(50) NOT NULL
);

-- Crear la tabla de vehículos
CREATE TABLE IF NOT EXISTS vehiculos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    placa VARCHAR(10) NOT NULL UNIQUE,
    tipo ENUM('moto', 'Carro', 'mula') NOT NULL,
    hora INT NOT NULL,
    minuto INT NOT NULL,
    total_a_pagar DECIMAL(10, 2) NOT NULL,
    usuario_id INT,
    fecha_registro TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);

-- Crear la tabla de tarifas
CREATE TABLE IF NOT EXISTS tarifas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    tipo ENUM('moto', 'Carro', 'mula') NOT NULL,
    tarifa_por_hora DECIMAL(10, 2) NOT NULL
);

-- Insertar tarifas iniciales
INSERT INTO tarifas (tipo, tarifa_por_hora) VALUES 
('moto', 2000), 
('Carro', 12000), 
('mula', 18000);

-- (Opcional) Insertar usuarios iniciales para pruebas
INSERT INTO usuarios (username, password) VALUES
('admin', 'admin123'),
('user1', 'password1');
