# 📚 Online Book Store

A Django REST Framework–based backend application for a virtual bookstore, where users can browse books and submit reviews.

---

## 📝 Features

- 🔐 User Registration and Login (via `dj-rest-auth` & `allauth`)
- 📚 Book listing and detail views
- 🧾 Users can submit one review per book (with rating 1–5)
- 👀 View other users' reviews on each book
- 📊 Average rating calculation per book
- ✅ Clean, secure, and optimized API with proper query handling (no N+1 problem)

---

## 🚀 Tech Stack

- **Backend**: Django, Django REST Framework
- **Auth**: dj-rest-auth, django-allauth
- **Database**: SQLite (default), easy to swap with PostgreSQL
- **Testing**: Django's `TestCase`, DRF's APIClient
- **Code Quality**: 100% unit test coverage

---

## 📦 Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/bookstore.git
cd bookstore
