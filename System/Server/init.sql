-- データベースの作成
CREATE DATABASE IF NOT EXISTS test;
USE AI_Workshop_Management;
CREATE TABLE ModelName (
  ID INT AUTO_INCREMENT PRIMARY KEY,
  ModelName VARCHAR(50)
);
CREATE USER 'Manager'@'%' IDENTIFIED BY 'managerpass';
CREATE USER 'Server'@'%' IDENTIFIED BY 'serverpass';

-- Manager
GRANT SELECT ON AI_Workshop_Management.* TO 'Manager'@'%';
GRANT INSERT ON AI_Workshop_Management.* TO 'Manager'@'%';

-- Server
GRANT SELECT ON AI_Workshop_Management.* TO 'Server'@'%';

-- 変更を反映
FLUSH PRIVILEGES;