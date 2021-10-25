CREATE TABLE user(
    userid VARCHAR(20) PRIMARY KEY,
    username VARCHAR(100) NOT NULL,
    phone VARCHAR(20) NOT NULL,
    bookid VARCHAR(20) NOT NULL
);

create table bus(
	busid VARCHAR(20) PRIMARY KEY,
	to_ VARCHAR(20) not null,
	from_ VARCHAR(20) not null,
	cost INT not null,
	duration DECIMAL(13,2) not null,
	rating DECIMAL(13,2) not null,
	depature time not null,
	arrival time not null
);

create table booking(
	booking_id VARCHAR(20) primary key,
	userid VARCHAR(20) not null,
	busid VARCHAR(20) not null,
	date_ DATE
);
 
insert into bus values('12345', 'hyderabad', 'vizag', 1299, 5.7, 4.3, '08:00:00', '12:00:00');
SELECT * FROM bus WHERE to_ = 'hyderabad' AND from_ = 'vizag';