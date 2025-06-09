# yggdrasil
Dagster workspace managing financial analytics platform.  Prototype for lightweight, scalable execution of financial models and trading.

## Running with Docker Compose

This repository provides a `docker compose` configuration for a small Dagster
environment that follows the latest `dg` best practices and installs Python
dependencies using [uv](https://github.com/astral-sh/uv).

1. Copy `.env.example` to `.env` and edit the values if desired.
2. Build and launch the services:

   ```bash
   docker compose up --build
   ```

The stack includes a Postgres instance, an example `ip_analytics` code location,
a Dagster webserver and daemon. Once the containers are running, visit
`http://localhost:3000` to access the Dagster UI.
