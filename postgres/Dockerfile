# Base image
#FROM --platform=linux/amd64 postgres
FROM postgres

#SQL Dump file to create table schema
COPY create_tables.sql /docker-entrypoint-initdb.d/