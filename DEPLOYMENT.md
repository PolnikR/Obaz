# Deployment

Projekt je pripravený na deploy cez GitHub Actions, Docker image v GitHub Container Registry a `docker compose` na serveri.

## Čo pipeline robí

1. Pri pushi do `master` alebo `develop` spustí Django testy.
2. Buildne Docker image.
3. Pushne image do `ghcr.io/<owner>/obaz-app`.
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

Workflow používa rovnaký naming ako existujúce Docker deploye:

- `DEPLOY_HOST` - IP alebo doména servera, napríklad `62.238.36.64`
- `DEPLOY_USER` - SSH používateľ
- `DEPLOY_SSH_PRIVATE_KEY` - existujúci privátny SSH kľúč pre deploy
- `GHCR_USERNAME` - GitHub používateľ alebo organization účet pre GHCR
- `GHCR_TOKEN` - GitHub token s právom `read:packages`
- `HEALTHCHECK_URL` - napríklad `http://obaz.polnik.sk`
- `APP_ENV_FILE` - celý runtime env súbor pre Django aplikáciu

Minimálny obsah `APP_ENV_FILE` pre prvý HTTP deploy:

```env
SECRET_KEY=sem-daj-dlhy-django-secret
DEBUG=False
ALLOWED_HOSTS=obaz.polnik.sk,62.238.36.64
CSRF_TRUSTED_ORIGINS=http://obaz.polnik.sk,http://62.238.36.64
DATABASE_NAME=/app/data/db.sqlite3
STATIC_ROOT=/app/staticfiles
MEDIA_ROOT=/app/media
HTTP_PORT=80
```

`APP_IMAGE` do `APP_ENV_FILE` nepíš. Workflow ho doplní automaticky podľa buildu.

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
