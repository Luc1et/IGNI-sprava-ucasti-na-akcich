# IGNI – Správa účasti na akcích

IGNI is a web application for managing attendance at events.  
It is developed as a practical tool for a small Czech community group (FAJRáci) and as a portfolio project to showcase fullstack development skills.

---

## 🎯 Vision

IGNI aims to be a professional-looking PWA for tracking and managing event attendance.  
Primary use case:

- An organizer creates an event.
- Members receive a notification.
- Each member sets their status: **Going / Not going / Maybe**.
- The system displays a clear overview of participation and a history of changes.

---

## 👥 Target audience

- **Primary:** members of FAJRáci → need a simple and clear tool.
- **Secondary:** recruiters → should see a polished, professional app with a demo guest account in later waves.

---

## 🛠️ Technology stack

**Backend**

- Python (FastAPI)
- SQLAlchemy + Pydantic
- Async engine + async sessions (even though a sync setup would be sufficient for such a small app, I deliberately chose async to learn the modern standard and demonstrate experience with non-blocking architecture)
- JWT (httpOnly cookies) for authentication
- bcrypt for password hashing

**Frontend**

- HTML, CSS, vanilla JavaScript
- Fetch API
- DOM manipulation
- PWA features (service worker for push notifications)

**Database**

- Local: PostgreSQL
- Deployment (PythonAnywhere free): MySQL

**Deployment**

- Local dev: Docker (FastAPI + PostgreSQL)
- Free hosting: PythonAnywhere (FastAPI + MySQL, HTTPS on igni.pythonanywhere.com)
- Integration with existing group website (Endora): redirect link to IGNI app

**Notifications**

- Web Push via pywebpush
- Cron jobs (PythonAnywhere Tasks) for reminders and bulk notifications

---

## 🔑 User roles

- **Admin**
  - Manage users
  - Create/delete events
  - Manage logs and notifications
- **User**
  - Respond to event participation
  - Add/remove participants
  - Cannot delete events or manage users
- **Guest (Wave 4)**
  - Safe demo account for recruiters

---

## 🧱 Database model (Wave 1 – MVP)

users

- id (PK)
- name
- email (unique)
- password_hash
- role ('admin'|'user')
- created_at

events

- id (PK)
- title
- description
- location
- starts_at (UTC)
- created_by (FK -> users.id)
- created_at
- deleted (bool, default false)

event_participants

- id (PK)
- event_id (FK -> events.id)
- user_id (FK -> users.id)
- status ('going'|'not_going'|'maybe')
- added_by (FK -> users.id)
- created_at
- UNIQUE(event_id, user_id)

event_logs

- id (PK)
- event_id (FK -> events.id)
- actor_user_id (FK -> users.id)
- target_user_id (FK -> users.id, nullable)
- action_type ('ADDED'|'REMOVED'|'STATUS_CHANGED'|'RESET')
- from_status (nullable)
- to_status (nullable)
- created_at

---

## 🌊 Roadmap

### Wave 1 – MVP

- Authentication (JWT, bcrypt)
- Admin-only user creation
- Roles (admin, user)
- Event dashboard (CRUD, delete only for admin)
- Event details with 3 participation columns (going / not going / maybe)
- Participation toggle
- Add/remove participants with logs
- Logboard under each event

### Wave 2 – Useful extensions

- Web Push notifications (new event, participation changes)
- Reminders for “Maybe” users
- Bulk notification one week before event
- Opt-out from notifications

### Wave 3 – Nice-to-have

- Participation history (reports from logs)
- Exports (CSV via pandas, PDF via reportlab)
- Participation statistics (Chart.js)
- User profiles (attendance count)
- Supersaas integration (new reservations become IGNI events, ignoring test ones)

### Wave 4 – Professional version

- Guest account (for recruiters)
- OAuth login (Google, Facebook)
- Calendar integration (ICS export, Google API)
- Extended roles (superadmin, moderator)
- UX polish (mobile optimization, dark mode, skeleton loaders)
- Security improvements (rate limiting, CSRF protection)

---

## ✅ What this project delivers

- A working app for FAJRáci group
- Professional features (roles, logs, notifications)
- Learning experience: FastAPI, SQLAlchemy, MySQL, cron, web push
- Portfolio value: recruiters can try a safe demo guest account
- Runs completely free on PythonAnywhere

---

## 👩‍💻 Author

Developed by **Lucie Talašová** as a junior fullstack portfolio project.  
The app aims to be both functional for a real community and professional-looking for recruiters.

---

## ⚖️ License

Copyright (c) 2025 Lucie  
All rights reserved.

This repository is provided for educational and portfolio purposes only.  
Use, reproduction, or distribution of this code without explicit permission from the author is prohibited.

---

> **Note:** The project name and user interface are in Czech,  
> because the app is designed for a Czech fire group (FAJRáci).  
> The repository description and documentation are provided in English for clarity.
