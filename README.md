# Flask + PostgresSQL Stack (con pgAdmin -opcional-)

Este proyecto es un entorno de desarrollo que incluye una API basica en flask y una base de datos PostgresSQ; usando Docker Compose.

## Requisitos
    -Docker
    -Docker Compose
    -Git

## Estructura
    - `app/`: Contiene la app de flask
    - `init-db-sql`: Script de ejemplo para la base de datos
    - `docker-compose.yml`: Orquestador principal
    - `deploy.sh`: Script para levantar el entorno

## Uso
    ```bash
    chmod +x deploy.sh
    ./deploy.sh
