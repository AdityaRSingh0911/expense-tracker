---
# Spec: Profile Page Design

## Overview
The Profile Page provides a dedicated space for logged-in users to view their account details (username and email) and manage their basic identity. This feature transitions the application from a simple authentication system to a personalized user experience, serving as a hub for user-specific settings and information.

## Depends on
- 02-registration
- 03-login-and-logout

## Routes
- `GET /profile` — Displays the user's profile information — logged-in

## Database changes
No database changes.

## Templates
- **Create:** `templates/profile.html`
- **Modify:** `templates/base.html` (to add a link to the Profile page in the navigation)

## Files to change
- `app.py` (to implement the profile route logic)

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
- [ ] Logged-in user can navigate to `/profile` and see their correct username and email.
- [ ] Unauthenticated user attempting to access `/profile` is redirected to the login page with a flash message.
- [ ] Navigation bar contains a visible and working link to the Profile page when logged in.
- [ ] The page follows the app's general design system and is responsive.
---
