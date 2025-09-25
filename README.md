# prewar-soccer-db

- A prototyped database and interactive site to view prewar soccer card information and pictures, with the intent to consolidate scattered websites and create a central source of historical information for collectors of prewar soccer cards. 

# Pre-War Soccer Card Database

A full-stack Python application for **pre-war and vintage soccer card collecting**.  
Collectors can search by player, year, or producer, view set checklists, bookmark sets, and track owned cards with notes, photos, and population report data.  

This project is both:
- A **learning tool** (computer science + Python development).  
- An **AppSec portfolio piece** (secure coding, authentication, CSRF/XSS prevention, secrets management).  

## Features (MVP to Roadmap)
- **Search**
  - Search by player, view all cards across years and sets.
  - Search by year, list all sets produced that year.
  - Search by producer, browse sets by manufacturer (Ogden’s, Panini, Gallaher, etc.).
- **Set Detail Pages**
  - Full checklist view.
  - Card-level details: player, team, photo, pop report.
- **User Collection**
  - Login / logout (bcrypt hashed passwords).
  - Mark owned cards, track grades, add notes.
  - Completion % per set.
- **Bookmarks**
  - Favorite sets for quick access.
- **Security**
  - CSRF protection, input validation, and session hardening.
  - Documented AppSec checklist.

## Tech Stack

**Backend**
- [Python 3.x](https://www.python.org/)  
- [Flask](https://flask.palletsprojects.com/) / web framework  
- [SQLAlchemy](https://www.sqlalchemy.org/) / ORM for database models  
- [Alembic](https://alembic.sqlalchemy.org/) / migrations  
- [bcrypt](https://pypi.org/project/bcrypt/) / password hashing  
- [python-dotenv](https://pypi.org/project/python-dotenv/) (optional if not using 1Password CLI)

**Frontend**
- [Jinja2](https://jinja.palletsprojects.com/) — template engine  
- [Bootstrap 5](https://getbootstrap.com/) — responsive UI components  
- Vanilla JS for small interactions (filters, search autocomplete)  

**Database**
- [SQLite](https://www.sqlite.org/) for local development  
- [PostgreSQL](https://www.postgresql.org/) for production deployment  

**Security / Secrets**
- [1Password CLI](https://developer.1password.com/docs/cli) for secrets management  
- Flask session hardening (HttpOnly, Secure, SameSite cookies)  
- CSRF protection (Flask-WTF)  

**Testing**
- [pytest](https://docs.pytest.org/) — unit + integration tests  

**Deployment (future roadmap)**
- [Render](https://render.com/) or [Heroku](https://www.heroku.com/) for hosting  
- Gunicorn WSGI server  
- TLS via Let’s Encrypt  

## Repo Structure
~~~
```plaintext
prewar-soccer-db/
├── README.md
├── requirements.txt
├── .gitignore
│
├── app/              # Flask app code
│   ├── __init__.py
│   ├── config.py
│   ├── models.py
│   ├── routes.py
│   ├── search.py
│   └── utils.py
│
├── migrations/       # DB migrations (Alembic)
├── data/             # Sample CSV data + import scripts
├── static/           # Images, CSS, JS
├── templates/        # HTML templates
├── tests/            # Unit + integration tests
└── security_checklist/
    ├── README.md
    └── appsec_basics.md
~~~
## Future improvements:
- Add modern sets

