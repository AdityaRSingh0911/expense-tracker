# Spec: Backend Routes for Profile Page

## Overview
This feature implements the backend logic required to populate the User Profile page. While some basic data retrieval exists, this step ensures that all profile statistics (total spent, transaction count, top category, and category breakdown) are efficiently queried from the database and passed to the frontend template. This allows users to see a high-level summary of their financial behavior.

## Depends on
- 01-database-setup
- 02-user-registration
- 03-user-authentication

## Routes
- `GET /profile` — Fetches user details and spending analytics — logged-in

## Database changes
No database changes.

## Templates
- **Modify:** `templates/profile.html` — Update to display the passed analytics data (total spent, transaction count, top category, recent transactions, and category breakdown).

## Files to change
- `app.py`

## Files to create
No new files.

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Logging in redirects the user to the profile page (if configured in `/` route).
- [ ] The profile page correctly displays the current logged-in user's username and email.
- [ ] Total spent correctly sums all expenses for the logged-in user.
- [ ] Total transaction count matches the number of records in the expenses table for that user.
- [ ] The "Top Category" correctly identifies the category with the highest total spending.
- [ ] A list of the 5 most recent transactions is displayed.
- [ ] A category-wise breakdown of all spending is correctly listed.
