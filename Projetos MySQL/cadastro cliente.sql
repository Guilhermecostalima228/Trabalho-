CREATE DATABASE cadastro_clientes;

USE cadastro_clientes;

CREATE TABLE clientes (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    telefone VARCHAR(20),
    cidade VARCHAR(50)
);
