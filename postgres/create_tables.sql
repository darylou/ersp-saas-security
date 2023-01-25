--CREATE USER postgres WITH SUPERUSER PASSWORD 'password';
--GRANT ALL ON SCHEMA public TO public;

CREATE TABLE pastes (
    id varchar(255) NOT NULL,
    title varchar(255) NOT NULL,
    body varchar(255)
);

INSERT INTO pastes (id, title, body) VALUES ('id-001', 'first', 'first');
INSERT INTO pastes (id, title, body) VALUES ('id-002', 'second', 'second');
INSERT INTO pastes (id, title, body) VALUES ('id-003', 'third', 'third');
INSERT INTO pastes (id, title, body) VALUES ('id-004', 'fourth', 'fourth');