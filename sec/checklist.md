# AppSec Basics Checklist

## Secrets & Config
- [x] `.gitignore` includes `.env` and `*.db`.
- [ ] Rotate keys periodically.

## Authentication
- [ ] Passwords hashed with bcrypt/argon2.
- [ ] Session cookies set with:
  - HttpOnly = True
  - Secure = True (in prod)
  - SameSite = Lax/Strict

## Web Security
- [ ] CSRF protection enabled (`Flask-WTF` or middleware).
- [ ] Input validation (WTForms or Marshmallow).
- [ ] Autoescaping enabled in Jinja2 templates.
- [ ] No use of `| safe` unless absolutely necessary.

## Database Security
- [ ] Use SQLAlchemy ORM (prevents raw SQL injection).
- [ ] Apply DB migrations via Alembic (avoid ad-hoc changes).
- [ ] Principle of least privilege on DB user.

## Logging & Monitoring
- [ ] Sanitize logs (no sensitive info like passwords).
- [ ] Error handling doesn’t expose stack traces in production.

## Deployment
- [ ] Use HTTPS in production (TLS).
- [ ] Set Flask `DEBUG=False` in production.
- [ ] Regularly patch dependencies (`pip-audit` / `safety`).


