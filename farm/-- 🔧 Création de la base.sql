-- 🔧 Création de la base
DROP DATABASE IF EXISTS ferme_simulation;
CREATE DATABASE ferme_simulation CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE ferme_simulation;

-- 🧑‍🌾 Table player
CREATE TABLE player (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    pieces_or INT DEFAULT 0,
    date_creation DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- 🏬 Table stockage
CREATE TABLE stockage (
    id INT AUTO_INCREMENT PRIMARY KEY,
    capacite INT NOT NULL
);

-- 📦 Table produit
CREATE TABLE produit (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100) NOT NULL,
    quantite INT NOT NULL,
    stockage_id INT,
    FOREIGN KEY (stockage_id) REFERENCES stockage(id)
);

-- 🏭 Table usine
CREATE TABLE usine (
    id INT AUTO_INCREMENT PRIMARY KEY,
    besoin VARCHAR(255),
    resultat VARCHAR(100),
    coefficient FLOAT DEFAULT 1.0,
    est_en_cours BOOLEAN DEFAULT FALSE,
    stockage_id INT,
    FOREIGN KEY (stockage_id) REFERENCES stockage(id)
);

-- 🚜 Table machine
CREATE TABLE machine (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    cost INT,
    est_utilisee BOOLEAN DEFAULT FALSE
);

-- 🌱 Table culture
CREATE TABLE culture (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(100),
    croissance INT,
    stade INT DEFAULT 0
);

-- 🌾 Table champ
CREATE TABLE champ (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_id INT,
    FOREIGN KEY (player_id) REFERENCES player(id)
);

-- 🌿 Table intermédiaire champ_culture
CREATE TABLE champ_culture (
    champ_id INT,
    culture_id INT,
    PRIMARY KEY (champ_id, culture_id),
    FOREIGN KEY (champ_id) REFERENCES champ(id),
    FOREIGN KEY (culture_id) REFERENCES culture(id)
);

-- 🔩 Table intermédiaire champ_machine
CREATE TABLE champ_machine (
    champ_id INT,
    machine_id INT,
    PRIMARY KEY (champ_id, machine_id),
    FOREIGN KEY (champ_id) REFERENCES champ(id),
    FOREIGN KEY (machine_id) REFERENCES machine(id)
);

-- 🔗 Table player_machine
CREATE TABLE player_machine (
    player_id INT,
    machine_id INT,
    PRIMARY KEY (player_id, machine_id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    FOREIGN KEY (machine_id) REFERENCES machine(id)
);

-- 🔗 Table player_usine
CREATE TABLE player_usine (
    player_id INT,
    usine_id INT,
    PRIMARY KEY (player_id, usine_id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    FOREIGN KEY (usine_id) REFERENCES usine(id)
);

-- 🔗 Table player_champ
CREATE TABLE player_champ (
    player_id INT,
    champ_id INT,
    PRIMARY KEY (player_id, champ_id),
    FOREIGN KEY (player_id) REFERENCES player(id),
    FOREIGN KEY (champ_id) REFERENCES champ(id)
);