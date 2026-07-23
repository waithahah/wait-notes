```yaml
  # The postgres database.
  db:
    image: postgres:15-alpine
    restart: always
    environment:
      PGUSER: ${PGUSER:-postgres}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-qiko300188}
      POSTGRES_DB: ${POSTGRES_DB:-qiko_plus}
      PGDATA: ${PGDATA:-/var/lib/postgresql/data/pgdata}
      TZ: Asia/Shanghai
    volumes:
      - ./volumes/db/data:/var/lib/postgresql/data
      - ./startupscripts/init.sql:/docker-entrypoint-initdb.d/init.sql
    healthcheck:
      test: [ "CMD", "pg_isready" ]
      interval: 1s
      timeout: 3s
      retries: 30
```