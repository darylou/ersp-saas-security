--CREATE USER postgres WITH SUPERUSER PASSWORD 'password';
--GRANT ALL ON SCHEMA public TO public;

CREATE TABLE pastes (
    id varchar(255) NOT NULL,
    title varchar(255) NOT NULL,
    body varchar(255)
);

INSERT INTO pastes (id, title, body) VALUES ('id-001', 'Post 1', 'This is the first post in the DB');
INSERT INTO pastes (id, title, body) VALUES ('id-002', 'Daryl Second Post', 'back again!');
INSERT INTO pastes (id, title, body) VALUES ('id-003', 'ERSP', 'We are in winter quarter of ERSP');
INSERT INTO pastes (id, title, body) VALUES ('id-004', 'BST', 'stands for binary search tree');