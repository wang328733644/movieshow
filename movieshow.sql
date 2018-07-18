/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2018/7/4 12:00:56                            */
/*==============================================================*/


drop table if exists Nav;

drop table if exists comments;

drop table if exists event;

drop table if exists movie;

drop table if exists movie_typename;

drop table if exists movie_types;

drop table if exists permission;

drop table if exists user;

drop table if exists user_status;

drop table if exists user_ticket;

/*==============================================================*/
/* Table: Nav                                                   */
/*==============================================================*/
create table Nav
(
   id                   int not null auto_increment,
   huge_pic             varchar(128) not null,
   movie_name           varchar(10),
   movie_desc           varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: comments                                              */
/*==============================================================*/
create table comments
(
   id                   int not null auto_increment,
   user_id          int not null,
   mov_id               int not null,
   content              varchar(10000) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: event                                                 */
/*==============================================================*/
create table event
(
   id                   int not null auto_increment,
   movie_id          int not null,
   click_counts         bigint not null default 0,
   primary key (id)
);

/*==============================================================*/
/* Table: movie                                                 */
/*==============================================================*/
create table movie
(
   id                   int not null auto_increment,
   name                 varchar(128) not null,
   img                   varchar(256) not null,
   des                  varchar(10000) not null,
   area_id             int not null,
   actors               varchar(1024) not null,
   year                 varchar(16) not null,
   type_id             int not null,
   score                varchar(64) not null,
   status               bool default 0,
   letter             varchar(4) not null,
   url                  varchar(256) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: movie_areas                                           */
/*==============================================================*/



/*==============================================================*/
/* Table: movie_areas                                           */
/*==============================================================*/

create table movie_areas
(
   id                   int not null auto_increment,
   area_name            varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: movie_types                                           */
/*==============================================================*/
create table movie_types
(
   id                   int not null auto_increment,
   type_name            varchar(64),
   primary key (id)
);

/*==============================================================*/
/* Table: permission                                            */
/*==============================================================*/
create table permission
(
   id                   int not null auto_increment,
   name                 varchar(4) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   id                   int not null auto_increment,
   name                 varchar(64) not null,
   password             varchar(256) not null,
   tel                  varchar(11) not null unique,
   email         varchar(256) not null,
   primary key (id)
);

/*==============================================================*/
/* Table: user_status                                           */
/*==============================================================*/
create table user_status
(
   id                   int not null auto_increment,
   status               bool not null,
   primary key (id)
);

/*==============================================================*/
/* Table: user_ticket                                           */
/*==============================================================*/
create table user_ticket
(
   id                   int not null auto_increment,
   user_id              int not null,
   ticket                varchar(64) not null,
   out_time          datetime not null,
   primary key (id)
);

/*==============================================================*/
/* Table: super_user                                        */
/*==============================================================*/

create table super_user
(
id                   int not null auto_increment,
name            varchar(64) not null,
password     varchar(64) not null,
tel                  varchar(16) not null unique,
email             varchar(64) not null,
primary key (id)
);

/*==============================================================*/
/* Table: news                                        */
/*==============================================================*/

create table news
(
id                           int not null auto_increment,
img                        varchar(256) not null,
title                        varchar(512) not null,
short_content       varchar(10000) not null,
long_content         text not null,
time                       varchar(128) not null,
view                       int not null,
primary key (id)   
);


alter table comments add constraint FK_Relationship_2 foreign key (user_id)
      references user (id) on delete restrict on update restrict;

alter table comments add constraint FK_Relationship_8 foreign key (mov_id)
      references movie (id) on delete restrict on update restrict;

alter table event add constraint FK_movie_event foreign key (movie_id)
      references movie (id) on delete restrict on update restrict;

alter table movie add constraint FK_type_movie foreign key (type_id)
      references movie_types (id) on delete restrict on update restrict;

alter table movie add constraint FK_area_movie foreign key (area_id)
      references movie_areas (id) on delete restrict on update restrict;

alter table permission add constraint FK_Relationship_1 foreign key (id)
      references user (id) on delete restrict on update restrict;

alter table user_ticket add constraint FK_user_ticket foreign key (user_id)
      references user (id) on delete restrict on update restrict;

alter table user_status add constraint FK_Relationship_3 foreign key (id)
      references user (id) on delete restrict on update restrict;

