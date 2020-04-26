DROP TABLE IF EXISTS point;

create table point (
    id integer PRIMARY KEY autoincrement,
    happy integer,
    sad integer,
    total integer,
    timestamp text,
    notes text
);

/* insert into point (happy, sad, total, timestamp, notes) values (3, 1, 2, '2020-04-08 00:00:00', 'Good writing; Listening the first time; Good sentences; Talking back');
insert into point (happy, sad, total, timestamp, notes) values (3, 2, 1, '2020-04-09 00:00:00', 'Good work; 100 on spelling test; listening the first time; not listening; whining');
insert into point (happy, sad, total, timestamp, notes) values (6, 0, 6, '2020-04-10 00:00:00', 'Good work; eating quietly; Excellent writing');
insert into point (happy, sad, total, timestamp, notes) values (4, 2, 2, '2020-04-12 00:00:00', 'Working quietly; Helping clean up; Being nice; Talking back; Being mean; Destroying pictures');
insert into point (happy, sad, total, timestamp, notes) values (5, 1, 4, '2020-04-13 00:00:00', 'Listening the first time; Helping clean up; Excellent work; Not listening; Whining');
insert into point (happy, sad, total, timestamp, notes) values (3, 3, 0, '2020-04-14 00:00:00', 'Helping clean up; Good work; Listening the first time; Being annoying; Not listening; Messy room');
insert into point (happy, sad, total, timestamp, notes) values (6, 0, 6, '2020-04-15 00:00:00', 'Good manners; Waiting patiently; Excellent work; Playing quietly');
insert into point (happy, sad, total, timestamp, notes) values (6, 0, 6, '2020-04-16 00:00:00', 'Keeping room clean; Excellent work; Being kind'); */