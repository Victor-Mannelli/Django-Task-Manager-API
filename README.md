# Django Task Manager API

A small REST API for managing projects, tasks, and comments. Built as a proof of concept to learn Django and Django REST Framework, including JWT authentication, modular URL routing, and a PostgreSQL setup via Docker.

## Stack

- **Python 3.11** / **Django 5.1**
- **Django REST Framework** for the API layer
- **djangorestframework-simplejwt** for JWT auth (access + refresh tokens, rotation, blacklist)
- **PostgreSQL** as the database (run via `docker compose`)
- **python-dotenv** for environment configuration

## Project Structure

```
task_manager/
├── settings.py            # Django + DRF + JWT configuration
├── urls.py                # Aggregates module URL patterns
├── models.py              # Project, Task, Comment models
├── serializers.py         # DRF serializers (User, Registration, Project, Task, Comment)
├── admin.py               # Django admin registrations
└── modules/
    ├── auth/              # Register / login / logout / token refresh (CBVs)
    ├── users/             # List / retrieve / update / delete users (FBVs)
    ├── projects/          # CRUD on projects
    ├── tasks/             # CRUD on tasks
    └── comments/          # CRUD on comments
```

The codebase mixes **Class-Based Views** (auth module) and **Function-Based Views** (everything else) on purpose, as a way to compare the two styles.

## Data Model

- **User** — Django's built-in `auth.User`
- **Project** — `name`, `description`, `owner` (FK → User)
- **Task** — `title`, `description`, `due_date`, `created_at`, `project` (FK → Project), `assignees` (M2M → User)
- **Comment** — `text`, `created_at`, `task` (FK → Task), `user` (FK → User)

## API Endpoints

All endpoints (except the auth ones) require a valid JWT access token in the `Authorization: Bearer <token>` header.

### Auth (public)
| Method | Path                  | Description                          |
| ------ | --------------------- | ------------------------------------ |
| POST   | `/register`           | Create a new user                    |
| POST   | `/login`              | Obtain access + refresh tokens       |
| POST   | `/logout`             | Blacklist a refresh token            |
| POST   | `/token/refresh`      | Exchange refresh for a new access    |

### Users
| Method | Path                | Description           |
| ------ | ------------------- | --------------------- |
| GET    | `/users`            | List all users        |
| GET    | `/users/<id>`       | Retrieve a user       |
| PUT    | `/users/<id>`       | Partially update      |
| DELETE | `/users/<id>`       | Delete a user         |

### Projects / Tasks / Comments
Each resource exposes the same CRUD shape:

| Method | Path                       |
| ------ | -------------------------- |
| GET    | `/<resource>`              |
| POST   | `/<resource>`              |
| GET    | `/<resource>/<id>`         |
| PUT    | `/<resource>/<id>`         |
| DELETE | `/<resource>/<id>`         |

Where `<resource>` is `projects`, `tasks`, or `comments`.

### Admin
- `/admin/` — Django admin (requires a superuser)

## Getting Started

### 1. Clone and configure environment

```bash
git clone <repo-url>
cd django-taskmanager
cp .env.public .env
```

Edit `.env` and set at least `POSTGRES_PASSWORD` and a real `SECRET_KEY`.

### 2. Start PostgreSQL

```bash
make compose          # docker compose up --build
```

This starts a Postgres container exposing port `5430` on the host (mapped to `5432` inside the container).

### 3. Create a virtualenv and install dependencies

```bash
make venv             # python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 4. Apply migrations and (optionally) create a superuser

```bash
make migrations       # python3 manage.py makemigrations task_manager
make dbsetup          # python3 manage.py migrate
make superuser        # python3 manage.py createsuperuser
```

### 5. Run the dev server

```bash
make dev              # python3 manage.py runserver 8080
```

The API is now available at `http://localhost:8080`.

## Make Targets

| Target            | What it does                                    |
| ----------------- | ----------------------------------------------- |
| `dev`             | Run the Django dev server on port 8080          |
| `venv`            | Create a Python virtual environment             |
| `deps`            | Freeze installed packages into `requirements.txt` |
| `migrations`      | Generate migrations for the `task_manager` app  |
| `dbsetup`         | Apply migrations                                |
| `compose`         | Start the Postgres container                    |
| `restart-compose` | Tear down and rebuild the Postgres container    |
| `superuser`       | Create a Django admin superuser                 |

## Quick Smoke Test

```bash
# Register
curl -X POST http://localhost:8080/register \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","email":"alice@example.com","password":"secret123"}'

# Login
curl -X POST http://localhost:8080/login \
  -H "Content-Type: application/json" \
  -d '{"username":"alice","password":"secret123"}'

# Use the access token
curl http://localhost:8080/projects \
  -H "Authorization: Bearer <access_token>"
```

## Notes / Caveats

This is a learning project — not production-ready. Notable shortcuts:

- `DEBUG = True` and `ALLOWED_HOSTS = []` are hardcoded in `settings.py`.
- The `SECRET_KEY` falls back to whatever is in `.env`; rotate it before any real deployment.
- Project / task / comment endpoints don't enforce ownership — any authenticated user can read or modify any record.
- `User` updates are done through `UserSerializer`, which doesn't hash passwords — there's no password change endpoint yet.
- The `Dockerfile` builds the app image but `docker-compose.yml` only defines the database service, so the app is meant to be run on the host during development.

## License

See [LICENSE](LICENSE).
