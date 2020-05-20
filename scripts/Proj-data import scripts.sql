LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Users.csv'
INTO TABLE usr
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Profiles.csv'
INTO TABLE prfl
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Creator.csv'
INTO TABLE creator
FIELDS TERMINATED BY '|'
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/grp.csv'
INTO TABLE grp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Contented.csv'
INTO TABLE contented
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Post.csv'
INTO TABLE post
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/P_Text.csv'
INTO TABLE p_text
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Photo.csv'
INTO TABLE photo
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Album.csv'
INTO TABLE album
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Entities Data/Friend.csv'
INTO TABLE friend
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

--Relationships
LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/Register.csv'
INTO TABLE register
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/comment_on.csv'
INTO TABLE comment_on
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/create_grp.csv'
INTO TABLE create_grp
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/displayed_in.csv'
INTO TABLE displayed_in
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/generates.csv'
INTO TABLE generates
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/joined.csv'
INTO TABLE joined
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/post_in.csv'
INTO TABLE post_in
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;

LOAD DATA INFILE 'D:/Documents/UNI/YR4/Semester 2/COMP3161/Assignments/Final Project/Data/Relationships Data/Compiles.csv'
INTO TABLE compiles
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\r\n'
IGNORE 1 ROWS;