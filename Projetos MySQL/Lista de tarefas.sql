CREATE DATABASE tarefas_db;
USE tarefas_db;

CREATE TABLE tarefas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    descricao VARCHAR(255),
    status ENUM('pendente', 'concluída') DEFAULT 'pendente'
);
