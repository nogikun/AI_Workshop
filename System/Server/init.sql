-- データベースの作成
CREATE DATABASE IF NOT EXISTS AI_Workshop_Management;
USE AI_Workshop_Management;
CREATE TABLE Model(
  ID INT AUTO_INCREMENT PRIMARY KEY,
  ModelName VARCHAR(50)
);
CREATE USER 'manager'@'%' IDENTIFIED BY 'managerpass';
CREATE USER 'server'@'%' IDENTIFIED BY 'serverpass';

-- Manager
GRANT SELECT ON AI_Workshop_Management.* TO 'manager'@'%';
GRANT INSERT ON AI_Workshop_Management.* TO 'manager'@'%';
GRANT UPDATE ON AI_Workshop_Management.* TO 'manager'@'%';

-- Server
GRANT SELECT ON AI_Workshop_Management.* TO 'server'@'%';

-- 初期値を追加
INSERT INTO Model(ModelName) VALUES('gpt-3.5-turbo-0613');
INSERT INTO Model(ModelName) VALUES('gpt-3.5-turbo-0613');
INSERT INTO Model(ModelName) VALUES('gpt-3.5-turbo-0613');
INSERT INTO Model(ModelName) VALUES('gpt-3.5-turbo-0613');

-- 変更を反映
FLUSH PRIVILEGES;