FROM mysql/mysql-server:latest

ENV MYSQL_ROOT_PASSWORD=password123

EXPOSE 3307

COPY ./data/*.sql /docker-entrypoint-initdb.d/

CMD ["mysqld", "--port=3307"]
