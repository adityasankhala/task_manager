# FastAPI Task Management API - Daily Learning & Build Plan

This guide breaks down the User Requirements Document (URD) into a daily checklist. Use this to guide your daily pushes and prepare for your daily reviews.

## 🎯 Project Overview
- **Goal:** Build a production-grade FastAPI REST API.
- **Key Concepts:** HTTP methods (GET, POST, PUT, PATCH, DELETE), JWT & API Key authentication, Role-Based Access Control (RBAC), SQLAlchemy ORM, Alembic migrations, custom middleware, and Pytest.
- **Database:** SQLite for local dev, PostgreSQL for production.

---

## 📅 Daily Build & Push Timeline (1 Week)

### **Day 1: Environment Setup**
- [ ] Create virtual environment and install dependencies.
- [ ] Initialise FastAPI project folder structure with placeholder files.
- [ ] Set up `database.py` with SQLite.
- [ ] Create `main.py` that starts the app and loads `/docs` (Swagger UI) at `http://localhost:8000/docs`.
- [ ] Set up Alembic and run `alembic init`.

### **Day 2: Database Models & Auth Core**
- [ ] Implement SQLAlchemy ORM models (`User`, `Project`, `Task`, `Comment`, `Tag`, `RefreshToken`, `APIKey`).
- [ ] Set up relationships and cascade rules (e.g., `cascade='all, delete-orphan'`).
- [ ] Run first Alembic migration (`alembic revision --autogenerate`) to create tables.
- [ ] Implement `auth/password.py` for bcrypt hashing.
- [ ] Implement `auth/jwt_handler.py` (create/verify JWT using python-jose).
- [ ] Implement `auth/api_key_handler.py` (generate, hash to SHA-256, verify).
- [ ] Write and pass tests `MT-01` through `MT-04`.

### **Day 3: Auth Router & Dependencies**
- [ ] Build `/auth/*` endpoints in `routers/auth.py` (register, login, refresh, logout, me, API key CRUD).
- [ ] Implement FastAPI dependencies in `auth/dependencies.py`:
  - `get_current_user_jwt`
  - `get_current_user_api_key`
  - `get_current_user` (tries JWT first, falls back to API Key)
  - `require_admin` (raises HTTP 403 if not admin)
- [ ] Verify both JWT Bearer and X-API-Key header authentication works on `GET /auth/me`.
- [ ] Write and pass tests `MT-05` through `MT-12`.

### **Day 4: HTTP Methods — Projects & Tasks**
- [ ] Build `routers/projects.py` with full CRUD (GET list, POST, GET one, PUT, PATCH, DELETE).
- [ ] Build `routers/tasks.py` with full CRUD + `PATCH /status` and tag attach/detach endpoints.
- [ ] Enforce ownership checks (users only access their own projects/tasks).
- [ ] Ensure PUT replaces all fields, and PATCH updates only provided fields using `model_dump(exclude_unset=True)`.
- [ ] Write and pass tests `MT-13` through `MT-18`.

### **Day 5: Comments, Tags, Users, Health**
- [ ] Build `routers/comments.py` with author-only enforcement on PUT and DELETE.
- [ ] Build `routers/tags.py` (GET and POST for all, DELETE for admin only).
- [ ] Build `routers/users.py` with admin-only routes using `require_admin`.
- [ ] Build `routers/health.py` (`GET /health` and `GET /stats`).
- [ ] Register all 7 routers in `main.py`.
- [ ] Write and pass tests `MT-19` and `MT-20`.

### **Day 6: Middleware, Exceptions & E2E Tests**
- [ ] Implement request logging middleware (method, path, status code, response time).
- [ ] Implement rate limiting middleware (100 req/min per IP -> HTTP 429).
- [ ] Implement custom exception handlers in `utils/exceptions.py`.
- [ ] Configure `CORSMiddleware`.
- [ ] Build `tests/conftest.py` with in-memory test DB and httpx `AsyncClient`.
- [ ] Run all 10 end-to-end scenarios and fix any routing/auth failures.

### **Day 7: Polish, Deploy & README**
- [ ] Fix any remaining test failures (all 20 unit + 10 E2E must pass).
- [ ] Write `README.md` (setup guide, .env config, running server/tests).
- [ ] Check Acceptance Criteria (No secrets hardcoded, Swagger UI works, API key hashes stored correctly).
- [ ] Prepare demo walkthrough (server start -> register -> login -> create project -> full CRUD -> API key flow -> admin routes).

---

## 🏗️ Project File Structure Checklist

- [ ] `main.py`
- [ ] `config.py` (Pydantic Settings from `.env`)
- [ ] `database.py`
- [ ] `models/user.py`, `models/project.py`, `models/task.py`, `models/comment.py`, `models/tag.py`, `models/refresh_token.py`, `models/api_key.py`
- [ ] `schemas/auth.py`, `schemas/user.py`, `schemas/project.py`, `schemas/task.py`, `schemas/comment.py`, `schemas/tag.py`
- [ ] `routers/auth.py`, `routers/users.py`, `routers/projects.py`, `routers/tasks.py`, `routers/comments.py`, `routers/tags.py`, `routers/health.py`
- [ ] `auth/jwt_handler.py`, `auth/api_key_handler.py`, `auth/dependencies.py`, `auth/password.py`
- [ ] `middleware/logging.py`, `middleware/rate_limit.py`
- [ ] `utils/exceptions.py`, `utils/responses.py`
- [ ] `tests/conftest.py`, `tests/test_auth.py`, `tests/test_projects.py`, `tests/test_tasks.py`
- [ ] `.env` (Never commit!)
- [ ] `.env.example`
- [ ] `requirements.txt`
- [ ] `alembic/`
- [ ] `README.md`

---

## 🧠 Daily Test Prep (Key Concepts to Know)

1. **PUT vs PATCH:** 
   - `PUT`: Full replacement (all fields required).
   - `PATCH`: Partial update (only provided fields updated). Must use `exclude_unset=True`.
2. **JWT Lifecycle:** 
   - Know the difference between access tokens (short life, stateless) and refresh tokens (long life, stateful/rotatable).
3. **API Key Security:** 
   - Never store raw keys. Generate -> show once -> store SHA-256 hash.
4. **Dependency Injection in FastAPI:**
   - How `Depends(get_current_user)` works to extract and verify tokens/keys before route logic runs.
5. **SQLAlchemy Relationships:**
   - Understand `cascade="all, delete-orphan"` so deleting a project deletes its tasks.
