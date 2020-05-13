


mysql -u root -p
root
create user 'study'@'%' identified by 'tmxjel0001';
create database studydb default set utf8mb4;
grant all on *.* to 'study'@'localhost' identified by 'tmxjel0001!' with grant option;
grant all on *.* to 'study'@'127.0.0.1' identified by 'tmxjel0001!' with grant option;
grant all on studydb.* to 'study'@'%' identified by 'tmxjel0001!' with grant option;
flush privileges;
-----------------------------------------------------------
mysql -u study -p
tmxjel0001!

use studydb;
CREATE TABLE tbl_user
(
  `u_no`        INT              NOT NULL    AUTO_INCREMENT,
  `u_id`        VARCHAR(20)      NOT NULL,
  `u_type`      INT              NOT NULL,
  `u_password`  VARCHAR(40)      NOT NULL,
  `u_email`     VARCHAR(40)      NOT NULL ,
  `u_cards`     VARCHAR(2000)    NULL,
  PRIMARY KEY (u_no)
);



select user, host from mysql.user;
select user, host, db from mysql.db;
show tables;

INSERT INTO tbl_user VALUES (NULL, 'admin', 'admin1234', 'issell@naver.com', NULL);
commit;


"""
DB : study
TABLE : tbl_user
+------------+---------------+------+-----+---------+----------------+
| Field      | Type          | Null | Key | Default | Extra          |
+------------+---------------+------+-----+---------+----------------+
| u_no       | int(11)       | NO   | PRI | NULL    | auto_increment |
| u_id       | varchar(20)   | NO   |     | NULL    |                |
| u_type     | int(11)       | NO   |     | NULL    |                |
| u_password | varchar(40)   | NO   |     | NULL    |                |
| u_email    | varchar(40)   | NO   |     | NULL    |                |
| u_cards    | varchar(2000) | YES  |     | NULL    |                |
+------------+---------------+------+-----+---------+----------------+
"""