CREATE DATABASE catalogo_musicas;
USE catalogo_musicas;

CREATE TABLE musicas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100),
    artista VARCHAR(100),
    genero VARCHAR(50),
    ano INT
);
