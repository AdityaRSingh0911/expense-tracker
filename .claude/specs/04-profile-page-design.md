# Spec: Profile Page Design

## Overview
The Profile Page provides a dedicated space for users to view and manage their account information. At this stage of the Spendly roadmap, it serves as a primary navigation hub for the logged-in user, displaying their username and email, and providing a clear path to managing their expenses. This enhances the user experience by confirming identity and providing a central landing spot for account-related activity.

## Depends on
- User Registration and Login (Steps 1-3)

## Routes
- `GET /profile` — Displays the user's profile information — logged-in

## Database changes
No database changes.

## Templates
- **Create:** `templates/profile.html`
- **Modify:** `templates/base.html` (to add a link to the profile page in the navigation)

## Files to change
- `app.py` (implement the `/profile` route logic)

## Files to create
- `templates/profile.html`

## New dependencies
No new dependencies.

## Rules for implementation
- No SQLAlchemy or ORMs
- Parameterised queries only
- Passwords hashed with werkzeug
- Use CSS variables — never hardcode hex values
- All templates extend `base.html`

## Definition of done
- [ ] Navigating to `/profile` while logged in displays the correct username and email of the current session user.
- [ ] Navigating to `/profile` while logged out redirects the user to the login page with a flash message.
- [ ] The profile page is styled consistently with the rest of the application using CSS variables.
- [ ] A link to the Profile page is visible and functional in the navigation bar of `base.html` when the user is logged in.
