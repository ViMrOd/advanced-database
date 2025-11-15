pragma foreign_keys = 1;

drop table if exists pet;
drop table if exists kind;
drop table if exists owner;

create table if not exists kind (
    id integer primary key autoincrement,
    name text not null,
    food text,
    sound text
);

insert into kind(name, food, sound) values ('dog','dogfood','bark');
insert into kind(name, food, sound) values ('cat','catfood','meow');
insert into kind(name, food, sound) values ('phoenix','fruit','music');
insert into kind(name, food, sound) values ('rabbit','carrots','squeak');
insert into kind(name, food, sound) values ('parrot','seeds','squawk');
insert into kind(name, food, sound) values ('turtle','lettuce','silent');

create table if not exists owner (
    id integer primary key autoincrement,
    name text not null,
    address text
);

insert into owner(name, address) values ('Greg','1234 Magnolia Way');
insert into owner(name, address) values ('Heather','1234 Magnolia Way');
insert into owner(name, address) values ('Chase','Dawsonville Georgia');
insert into owner(name, address) values ('Novak','Belgrade Serbia');
insert into owner(name, address) values ('Ava','42 Willow Lane');
insert into owner(name, address) values ('Liam','8 Maple Court');
insert into owner(name, address) values ('Sophia','77 Pine Road');
insert into owner(name, address) values ('Noah','910 Cedar Ave');

create table if not exists pet (
    id integer primary key autoincrement,
    name text not null,
    kind_id integer not null,
    age integer,
    owner_id integer not null,
    foreign key (kind_id) references kind(id)
      on delete RESTRICT
      on update CASCADE,
    foreign key (owner_id) references owner(id)
      on delete RESTRICT
      on update CASCADE
);

insert into pet(name, kind_id, age, owner_id) values ('Dorothy',1,0,1);
insert into pet(name, kind_id, age, owner_id) values ('Suzy',2,7,1);
insert into pet(name, kind_id, age, owner_id) values ('Casey',2,19,2);
insert into pet(name, kind_id, age, owner_id) values ('Heidi',1,1,1);
insert into pet(name, kind_id, age, owner_id) values ('Bunny',4,2,5);
insert into pet(name, kind_id, age, owner_id) values ('Thumper',4,1,6);
insert into pet(name, kind_id, age, owner_id) values ('Polly',5,3,7);
insert into pet(name, kind_id, age, owner_id) values ('Kiwi',5,2,8);
insert into pet(name, kind_id, age, owner_id) values ('Shelly',6,12,5);
insert into pet(name, kind_id, age, owner_id) values ('Speedy',6,30,6);
insert into pet(name, kind_id, age, owner_id) values ('Echo',1,4,7);
insert into pet(name, kind_id, age, owner_id) values ('Milo',2,5,8);
insert into pet(name, kind_id, age, owner_id) values ('Luna',3,3,5);
insert into pet(name, kind_id, age, owner_id) values ('Rex',1,6,6);
