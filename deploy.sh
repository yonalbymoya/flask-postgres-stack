#!/bin/bash


echo "Levantando el entorno de Flask + PostgresSQL con Docker Compose..."

docker-compose up --build -d

echo "Entorno desplegado de forma exitosa, Flask en http://localhost:5000"
