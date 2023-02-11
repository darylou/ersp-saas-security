--CREATE USER postgres WITH SUPERUSER PASSWORD 'password';
--GRANT ALL ON SCHEMA public TO public;

CREATE TABLE pastes (
    id varchar(255) NOT NULL,
    title varchar(255) NOT NULL,
    body varchar(255)
);


CREATE TABLE accounts (
    username varchar(255) NOT NULL,
    passw varchar(255) NOT NULL
);

INSERT INTO accounts (username, passw) VALUES ('Sparkles', 'Sparkles');
