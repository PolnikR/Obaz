# Deployment

Projekt je pripravený na deploy cez GitHub Actions, Docker image v GitHub Container Registry a `docker compose` na serveri.

## Čo pipeline robí

1. Pri pushi do `master` spustí Django testy.
2. Buildne Docker image.
3. Pushne image do `ghcr.io/<owner>/<repo>`.
4. Ak sú nastavené serverové GitHub Secrets, prihlási sa cez SSH na server.
5. Skopíruje `docker-compose.prod.yml`, `deploy/nginx.conf` a vytvorí serverový `.env`.
6. Na serveri spustí `docker compose pull` a `docker compose up -d`.

## Server prerequisites

Na serveri musí byť nainštalované:

- Docker
- Docker Compose plugin (`docker compose`)
- SSH prístup pre deploy používateľa

Deploy používateľ musí mať právo spúšťať Docker.

## GitHub Secrets

Nastav v GitHub repozitári `Settings -> Secrets and variables -> Actions`:

- `SERVER_HOST` - IP alebo doména servera
- `SERVER_USER` - SSH používateľ
- `SERVER_SSH_KEY` - privátny SSH kľúč pre deploy
- `SERVER_PORT` - voliteľné, default je `22`
- `SERVER_PATH` - voliteľné, default je `/opt/erik-project`
- `DJANGO_SECRET_KEY` - produkčný Django secret key
- `DJANGO_ALLOWED_HOSTS` - napríklad `obaz.sk,www.obaz.sk`
- `DJANGO_CSRF_TRUSTED_ORIGINS` - napríklad `https://obaz.sk,https://www.obaz.sk`
- `GHCR_USER` - voliteľné, default je owner repozitára
- `GHCR_TOKEN` - GitHub token s právom `read:packages`
- `HTTP_PORT` - voliteľné, default je `80`

## Persistent data

Produkčný compose používa Docker volumes:

- `app_data` pre SQLite databázu
- `app_media` pre uploadnuté obrázky
- `app_static` pre vyzbierané statické súbory

Tieto volumes nemaž bez zálohy.

## Lokálny produkčný smoke test

Po doplnení lokálneho `.env` podľa `.env.example`:

```bash
docker compose -f docker-compose.prod.yml up --build
```

Potom otvor aplikáciu na `http://localhost`.
