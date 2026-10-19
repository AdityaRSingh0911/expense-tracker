# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Development Commands
- **Run Application**: `python app.py` (runs on port 5001)
- **Install Dependencies**: `pip install -r requirements.txt`
- **Run Tests**: `pytest`

## Architecture
The project is a Flask-based expense tracker application.

### Structure
- `app.py`: Main entry point containing route definitions.
- `database/`: Contains database logic.
  - `db.py`: Intended for SQLite connection management (`get_db`, `init_db`, `seed_db`).
- `static/`: CSS and JavaScript assets.
- `templates/`: HTML templates for the frontend.

### Key Routing
- `/`: Landing page
- `/register`: User registration
- `/login`: User authentication
- `/terms` & `/privacy`: Legal pages
- `/expenses/*`: Expense management (currently placeholders)
