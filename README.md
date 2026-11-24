# Piazza API

Piazza is a discussion platform backend. Registered users publish posts under
the topics **Politics, Health, Sport and Tech**, like or dislike other users'
posts and comment on them. Every post has an expiry time: expired posts stay
readable but accept no new reactions or comments.

**Technologies:** Python 3.12, FastAPI, Pydantic, SQLAlchemy 2, SQLite,
JWT bearer authentication (PyJWT, bcrypt), pytest with FastAPI `TestClient`,
Docker / Docker Hub, Google Kubernetes Engine.

Docker Hub image: `DOCKERHUB_USERNAME/piazza:1.0.0` (update with your username, tags and digests)

---

## 1. Prerequisites

- Python 3.12 and `pip`
- Docker (for the container steps)
- Google Cloud SDK (`gcloud`) and `kubectl` (for GKE)

## 2. Install dependencies

```bash
python -m venv .venv
source .venv/bin/activate            # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt  # runtime + test dependencies
```

## 3. Configuration

| Variable | Required | Default | Purpose |
|----------|----------|---------|---------|
| `PIAZZA_JWT_SECRET` | yes | – | HMAC key for signing JWTs (min. 32 characters) |
| `PIAZZA_DATABASE_PATH` | no | `./data/piazza.db` (container: `/data/piazza.db`) | SQLite database file |
| `PIAZZA_JWT_EXPIRE_MINUTES` | no | `30` | Access-token lifetime |

`.env.example` contains placeholders only. Copy it to `.env` (git-ignored) and
generate a secret:

```bash
cp .env.example .env
python -c "import secrets; print(secrets.token_hex(32))"   # paste into .env
```

## 4. Run locally

```bash
set -a; source .env; set +a
uvicorn app.main:create_app --factory --reload
```

- API documentation (Swagger UI): http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc
- Health: http://127.0.0.1:8000/health

In Swagger UI, call `POST /auth/login`, click **Authorize** and paste the
`access_token`.

