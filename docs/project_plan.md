# Extended outline & dev notes

# Project Plan — Pre-War Soccer Card Database

## 1. Project Overview
The **Pre-War Soccer Card Database** is a full-stack Python application designed to catalog, search, and track ownership of vintage soccer card sets (1880–1979).  

The app serves two purposes:
1. **Collector Utility**: A tool for searching by player, year, or producer, browsing sets, and tracking personal collections.
2. **Learning Platform**: A structured solo development project to reinforce computer science fundamentals, software engineering practices, and application security (AppSec).

---

## 2. Goals
- **Functional MVP**: Enable users to search sets by year/player and view checklists.
- **Collector Features**: Track ownership, bookmark sets, and calculate collection completion.
- **Security Practices**: Implement authentication, CSRF/XSS protection, and secure session management.
- **Scalable Foundation**: Start with CSV-based seed data, transition to database-driven queries, and support image hosting.

---

## 3. Scope
### In-Scope (Phase 1–3)
- Flask application with SQLAlchemy ORM.
- Database schema for `CardSet`, `Card`, `User`, and `UserCollection`.
- Search logic (player, year, producer).
- Jinja2 + Bootstrap frontend (tables, search results, set views).
- User authentication and collection tracking.
- Local static image hosting (migratable to cloud/CDN).
- Security hardening (hashed passwords, CSRF protection, cookie settings).

### Out-of-Scope (for MVP)
- Real-time market/pricing data.
- Automated population report scraping (manual entry supported).
- Modern SPA frontend (React/Vue). Can be considered later.
- Public multi-user scaling (focus on single collector use case first).

---

## 4. Architecture
- **Backend**: Flask (Python), SQLAlchemy ORM, Alembic migrations.
- **Frontend**: Jinja2 templates, Bootstrap 5, minimal JavaScript.
- **Database**: SQLite (dev), PostgreSQL (production).
- **Static Assets**: Local `static/images/` in prototype; extensible to S3/CDN.
- **Secrets Management**: Environment variables via 1Password CLI or `.env` (dev only).
- **Deployment**: Local Flask dev server → Gunicorn + Render/Heroku (prod).

---

## 5. Deliverables
- **MVP App** (search + browse by year/player).
- **Collector Features** (login, collection tracking, bookmarks).
- **Documentation**:
  - `README.md`: Overview, setup, stack.
  - `docs/project_plan.md`: This plan.
  - `security_checklist/`: Applied AppSec practices.
  - `docs/static_images.md`: Image hosting strategy.
- **Demo Dataset**: Seed data (e.g., 1958 Alifabolaget Pelé, 1934 Ogden’s).
- **Deployed Prototype** (optional stretch goal).

---

## 6. Milestones & Timeline

### Phase 1 — Core Setup (Weeks 1–2)
- Repo scaffold with `.gitignore`, `requirements.txt`, and `README.md`.
- Flask app factory (`__init__.py`).
- Database models: `CardSet`, `Card`.
- Alembic migrations + seed with demo CSVs.
- Basic routes + templates (search by player, year).

### Phase 2 — Collector Features (Weeks 3–5)
- Add `User` and `UserCollection` models.
- Authentication (bcrypt, sessions).
- Collection tracking + completion %.
- Bookmarking favorite sets.

### Phase 3 — Enrichment & Security (Weeks 6–8)
- Add card photos (static hosting).
- Add population report field.
- Security hardening: CSRF, input validation, secure cookies.
- Document AppSec practices in `security_checklist/`.

### Phase 4 — Deployment & Scale (Stretch Goal, Weeks 9–12)
- Migrate to PostgreSQL.
- Deploy with Gunicorn on Render/Heroku.
- Seed more sets via CSV imports.
- Explore cloud image hosting (S3/Imgur API).

---

## 7. Risks & Mitigation
- **Data entry burden**: Mitigate with CSV import scripts, start small (1–2 sets).
- **Security pitfalls**: Track with `security_checklist/`, use defensive defaults.
- **Scope creep**: Keep MVP limited; new features go to backlog.
- **Frontend complexity**: Stick to Jinja2/Bootstrap for prototype; defer React.

---

## 8. Success Criteria
- A user (collector) can:
  - Search Pelé → see all his cards across sets.
  - Search 1934 → see all sets released that year.
  - Bookmark a set.
  - Mark cards as owned and see collection %.
- App passes basic AppSec hygiene (hashed passwords, CSRF protection).
- Repo shows professional structure, documentation, and security awareness.

---

✅ **Bottom Line**: This project blends **collecting utility** with **real-world software engineering**. It demonstrates database design, backend/frontend integration, and secure coding practices — making it a valuable learning experience and a strong AppSec portfolio artifact.
