DROP TABLE IF EXISTS point;

create table point (
    id integer PRIMARY KEY autoincrement,
    happy integer,
    sad integer,
    total integer,
    timestamp text,
    notes text
);

insert into point (happy, sad, total, timestamp, notes) values (5, 3, 2, '2020-04-01 00:00:00', 'Listening the first time; Being rude');
insert into point (happy, sad, total, timestamp, notes) values (0, 1, 0, '2020-04-03 00:00:00', 'Being rude');
insert into point (happy, sad, total, timestamp, notes) values (3, 0, 3, '2020-04-05 00:00:00', 'Good work');