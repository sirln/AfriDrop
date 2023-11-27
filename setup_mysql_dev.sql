-- prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS afri_dev_db;
CREATE USER IF NOT EXISTS 'afri_dev'@'localhost' IDENTIFIED BY 'afri_dev_pwd';
GRANT ALL PRIVILEDGES ON `afri_dev_db`.* TO 'afri_dev'@'localhost';
FLUSH PRIVILEGES;
