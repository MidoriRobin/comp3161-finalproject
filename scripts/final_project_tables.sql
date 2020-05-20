drop database if exists socialdb;
create database socialdb;
use socialdb;

--Entities
create table usr(
    u_id int not null auto_increment,
    lname varchar(20),
    fname varchar(20),
    email varchar(100),
    dob date,
    pword varchar(20),
    primary key (u_id)
);


create table prfl(
    p_id int not null auto_increment,
    p_pic varchar(10),
    bio varchar(100),
    u_name varchar(20) not null,
    num_of_friends int(10),
    primary key (p_id)
);


create table creator(
    c_id int not null auto_increment,
    u_id int not null,
    p_id int not null,
    primary key (c_id,u_id,p_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (p_id) references prfl(p_id) on update cascade on delete cascade
);


create table friend(
    u_id int not null,
	f_id int not null,
    p_id int not null,
    f_type varchar(10),

    primary key (u_id, p_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
	foreign key (f_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (p_id) references prfl(p_id) on update cascade on delete cascade
);


create table contentEd(
    ce_id int not null auto_increment,
    u_id int not null,
    p_id int not null,
    primary key (ce_id, u_id, p_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (p_id) references prfl(p_id) on update cascade on delete cascade
);


create table grp(
    grp_id int not null auto_increment,
    grp_name varchar(20) not null,
    num_members int(10),
    primary key (grp_id)
);


create table post(
    post_id int not null auto_increment,
    num_likes int(10),
    primary key (post_id)
);


create table p_text(
    t_id int not null auto_increment,
    post_id int not null,
    content varchar(200) not null,
    primary key (t_id, post_id),
    foreign key (post_id) references post(post_id) on update cascade on delete cascade
);


create table photo(
    photo_id int not null auto_increment,
    post_id int not null,
    photo_loc varchar(20),
    descrip varchar(50),
    photo_content varchar(20),
    primary key(photo_id, post_id),
    foreign key (post_id) references post(post_id) on update cascade on delete cascade
);


create table album(
    album_id int not null auto_increment,
	album_name varchar(20) not null,
    num_of_photos int(10),
    primary key(album_id)
);

--Relationships

create table register(
    p_id int not null,
    u_id int not null,
    dateRegistered datetime,
    primary key (u_id, p_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (p_id) references prfl(p_id) on update cascade on delete cascade
);

--for a user that makes a post
create table generates(
    post_id int not null,
	u_id int not null,
	datePosted datetime,
	primary key (post_id, u_id),
	foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
	foreign key (post_id) references post(post_id) on update cascade on delete cascade
);

--for a user that posts in a group
create table post_in(
	grp_id int not null,
	ce_id int not null,
	date_added datetime,
	primary key(grp_id,ce_id),
	foreign key (grp_id) references grp(grp_id) on update cascade on delete cascade,
	foreign key (ce_id) references contentEd(ce_id) on update cascade on delete cascade
);

--user making a comment on a post
create table comment_on(
    post_id int not null,
	  u_id int not null,
    content varchar(100),
  	dateMade datetime,
    primary key (post_id),
    foreign key (post_id) references post(post_id) on update cascade on delete cascade,
	foreign key (u_id) references usr(u_id) on update cascade on delete cascade
);


--For posts to be displayed in a group
create table displayed_in(
    post_id int not null,
    grp_id int not null,
    datePosted datetime,
    primary key (u_id, post_id),
    foreign key (grp_id) references grp(grp_id) on update cascade on delete cascade,
    foreign key (post_id) references post(post_id) on update cascade on delete cascade
);

--Table for the group created and the user that creates it
create table create_grp(
    u_id int not null,
	grp_id int not null,
    dateCreated datetime,
    primary key (u_id, grp_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (grp_id) references grp(grp_id) on update cascade on delete cascade
);

create table designates(
	c_id int not null,
	ce_id int not null,
	primary key (c_id, ce_id),
	foreign key (c_id) references creator(c_id) on update cascade on delete cascade,
	foreign key (ce_id) references contentEd(ce_id) on update cascade on delete cascade
);

--Reference joining a group
create table joined(
    p_id int not null,
    u_id int not null,
	grp_id int not null,
    dateJoined datetime,
    primary key (u_id, p_id),
    foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
    foreign key (grp_id) references grp(grp_id) on update cascade on delete cascade,
    foreign key (p_id) references prfl(p_id) on update cascade on delete cascade
);

create table contained_in(
	photo_id int not null,
	album_id int not null,
	primary key (photo_id, album_id),

	foreign key (photo_id) references photo(photo_id) on update cascade on delete cascade,
	foreign key (album_id) references album(album_id) on update cascade on delete cascade
);

create table compiles(
	u_id int not null,
	album_id int not null,
	primary key (u_id, album_id),

	foreign key (u_id) references usr(u_id) on update cascade on delete cascade,
	foreign key (album_id) references album(album_id) on update cascade on delete cascade
);
