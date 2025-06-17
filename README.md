# Vehicles and Parts Management Web App

## Project Structure
- `backend/`: Python FastAPI API with SQLAlchemy ORM and PostgreSQL
- `frontend/`: React (JavaScript) frontend
- `db_migrations/`: Database migration scripts

## Setup Instructions

### Backend
1. Navigate to `backend/`
2. Create a virtual environment and activate it
3. Install dependencies: `fastapi`, `uvicorn`, `sqlalchemy`, `psycopg2-binary`
4. Configure database connection in `.env`
5. Run the server: `uvicorn main:app --reload`

### Frontend
1. Navigate to `frontend/`
2. Run `npx create-react-app .` (if not already set up)
3. Start the development server: `npm start`

### Database
- Use migration scripts in `db_migrations/` for schema changes

---

## Features
- Vehicle and part management (CRUD)
- Stock management
- Sales and transaction management
- Admin and user management

---

## Best Practices
- Use environment variables for secrets
- Validate all user input
- Use role-based access control
- Write unit and integration tests
- Use Docker for deployment (optional)
