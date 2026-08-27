# 📚 Library Management API

<p align="center">
  <strong>🚀 Modern Library Management REST API</strong>
</p>

<p align="center">
  Python • FastAPI • SQLAlchemy • SQLite • Pydantic
</p>

<p align="center">
  <strong>📖 Books &nbsp; | &nbsp; 👨‍💼 Authors &nbsp; | &nbsp; 👤 Users &nbsp; | &nbsp; 🔄 Loans</strong>
</p>

---

## ✨ About The Project

**Library Management API** — kutubxona jarayonlarini boshqarish uchun ishlab chiqilgan REST API loyihasi.

Loyiha yordamida kutubxonadagi:

* 📚 Kitoblarni boshqarish
* ✍️ Mualliflarni boshqarish
* 👤 Foydalanuvchilarni boshqarish
* 🔄 Kitob berish va qaytarish jarayonlarini boshqarish
* 🏷️ Foydalanuvchi rollarini ajratish
* 📊 Kitoblarning umumiy va mavjud sonini nazorat qilish

mumkin.

Loyiha **Python + FastAPI + SQLAlchemy + SQLite** texnologiyalari asosida qurilgan va modulga ajratilgan arxitekturadan foydalanadi.

---

## 🎯 Project Goal

Ushbu loyiha FastAPI bilan backend yaratish, REST API arxitekturasi, SQLAlchemy ORM, Pydantic schemas, CRUD operatsiyalar, relationship va database bilan ishlashni amaliyotda mustahkamlash uchun ishlab chiqilgan.

---

# 🛠️ Tech Stack

<p align="center">

| Technology          | Purpose                      |
| ------------------- | ---------------------------- |
| 🐍 **Python**       | Backend programming language |
| ⚡ **FastAPI**       | REST API framework           |
| 🗄️ **SQLite**      | Relational database          |
| 🔗 **SQLAlchemy**   | ORM                          |
| ✅ **Pydantic**      | Data validation & schemas    |
| 🚀 **Uvicorn**      | ASGI server                  |
| 🧰 **Git & GitHub** | Version control              |

</p>

FastAPI avtomatik ravishda OpenAPI asosidagi interaktiv API documentation yaratadi va `/docs` orqali endpointlarni browser ichidan test qilish imkonini beradi.

---

# 📂 Project Structure

```text
library-fastapi-project/
│
├── 📁 app/
│   │
│   ├── 📁 authors_app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   ├── 📁 books_app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   ├── 📁 loans_app/
│   │   ├── __init__.py
│   │   ├── models.py
│   │   ├── router.py
│   │   ├── schemas.py
│   │   └── services.py
│   │
│   └── 📁 users_app/
│       ├── __init__.py
│       ├── models.py
│       ├── router.py
│       ├── schemas.py
│       └── services.py
│
├── 🗄️ database.py
├── 🚀 main.py
├── 📦 requirements.txt
├── 📝 README.md
└── ⚙️ .gitignore
```

Ushbu modular struktura repository'dagi amaldagi `app` tuzilmasiga moslashtirilgan.

---

# 🧩 Application Modules

## 👤 `users_app`

Foydalanuvchilarni boshqarish uchun javobgar modul.

```text
users_app/
├── models.py
├── schemas.py
├── router.py
├── services.py
└── __init__.py
```

### User Model

`Users` modeli quyidagi asosiy maydonlarga ega:

| Field       | Type    | Description              |
| ----------- | ------- | ------------------------ |
| `id`        | Integer | Unique user ID           |
| `username`  | String  | Foydalanuvchi login nomi |
| `password`  | String  | Foydalanuvchi paroli     |
| `full_name` | String  | To‘liq ism               |
| `role`      | Enum    | User role                |
| `status`    | Boolean | Foydalanuvchi aktivligi  |

### User Roles

```text
ADMIN
  │
  ├── 👑 Admin
  │
  ├── 📚 Librarian
  │
  └── 👤 User
```

Modelda uchta asosiy role mavjud:

* 👑 `admin`
* 📚 `librarian`
* 👤 `user`

`Users` modeli `Loans` bilan relationship orqali bog‘langan.

---

# ✍️ `authors_app`

Kutubxonadagi mualliflarni boshqaradi.

```text
authors_app/
├── models.py
├── schemas.py
├── router.py
├── services.py
└── __init__.py
```

### Author Model

```text
Authors
│
├── id
├── name
├── surname
└── bio
```

| Field     | Type    | Description             |
| --------- | ------- | ----------------------- |
| `id`      | Integer | Author ID               |
| `name`    | String  | Muallif ismi            |
| `surname` | String  | Muallif familiyasi      |
| `bio`     | Text    | Muallif haqida ma'lumot |

Muallif va kitoblar o‘rtasida relationship mavjud.

```text
Author
   │
   │ 1
   │
   └──────────────< Books
                     N
```

Ya'ni bitta muallifning bir nechta kitobi bo‘lishi mumkin.

---

# 📚 `books_app`

Kutubxonaning asosiy moduli.

```text
books_app/
├── models.py
├── schemas.py
├── router.py
├── services.py
└── __init__.py
```

### Book Model

```text
Books
│
├── id
├── title
├── author_id
├── year
├── description
├── quantity
└── available_quantity
```

| Field                | Type       | Description                |
| -------------------- | ---------- | -------------------------- |
| `id`                 | Integer    | Book ID                    |
| `title`              | String     | Kitob nomi                 |
| `author_id`          | ForeignKey | Muallif ID                 |
| `year`               | Integer    | Nashr yili                 |
| `description`        | Text       | Kitob haqida ma'lumot      |
| `quantity`           | Integer    | Jami kitoblar soni         |
| `available_quantity` | Integer    | Hozir mavjud kitoblar soni |

`author_id` `authors.id` ga ForeignKey orqali bog‘langan. Kitoblar `Authors` va `Loans` bilan relationshipga ega.

---

# 🔄 `loans_app`

Kitoblarni foydalanuvchilarga berish va qaytarish jarayonlarini boshqaradi.

```text
loans_app/
├── models.py
├── schemas.py
├── router.py
├── services.py
└── __init__.py
```

### Loan Model

```text
Loans
│
├── id
├── user_id
├── book_id
├── borrowed_at
├── returned_at
└── status
```

| Field         | Type       | Description        |
| ------------- | ---------- | ------------------ |
| `id`          | Integer    | Loan ID            |
| `user_id`     | ForeignKey | Kitobni olgan user |
| `book_id`     | ForeignKey | Olingan kitob      |
| `borrowed_at` | DateTime   | Olingan vaqt       |
| `returned_at` | DateTime   | Qaytarilgan vaqt   |
| `status`      | Enum       | Loan holati        |

### Loan Status

```text
📚 BOOK BORROWED
       │
       ▼
   🔄 borrowed
       │
       │
       ▼
📖 BOOK RETURNED
       │
       ▼
   ✅ returned
```

Modelda:

```text
BORROWED = "borrowed"
RETURNED = "returned"
```

statuslari mavjud. `Loans` modeli `Users` va `Books` bilan ForeignKey va relationship orqali bog‘langan.

---

# 🗄️ Database Architecture

Loyiha **SQLite** database'dan foydalanadi.

Database fayli:

```text
library.db
```

SQLAlchemy engine quyidagi SQLite connection orqali yaratiladi:

```text
sqlite:///./library.db
```

Database session `SessionLocal` orqali boshqariladi va `get_db()` dependency har bir request uchun database session yaratib, request tugagach uni yopadi.

---

# 🔗 Database Relationship

Loyihaning database modeli quyidagicha:

```text
                 ┌─────────────────┐
                 │     USERS       │
                 │─────────────────│
                 │ id              │
                 │ username        │
                 │ password        │
                 │ full_name       │
                 │ role            │
                 │ status          │
                 └────────┬────────┘
                          │
                          │ 1
                          │
                          │ N
                 ┌────────▼────────┐
                 │      LOANS      │
                 │─────────────────│
                 │ id              │
                 │ user_id         │
                 │ book_id         │
                 │ borrowed_at     │
                 │ returned_at     │
                 │ status          │
                 └────────┬────────┘
                          │
                          │ N
                          │
                          │ 1
                 ┌────────▼────────┐
                 │      BOOKS      │
                 │─────────────────│
                 │ id              │
                 │ title           │
                 │ author_id       │
                 │ year            │
                 │ description     │
                 │ quantity        │
                 │ available_qty   │
                 └────────┬────────┘
                          │
                          │ N
                          │
                          │ 1
                 ┌────────▼────────┐
                 │     AUTHORS     │
                 │─────────────────│
                 │ id              │
                 │ name            │
                 │ surname         │
                 │ bio             │
                 └─────────────────┘
```

### Relationship Summary

```text
👤 Users
   │
   └── 1 : N ── 🔄 Loans

📚 Books
   │
   └── 1 : N ── 🔄 Loans

✍️ Authors
   │
   └── 1 : N ── 📚 Books
```

---

# 🧱 Models vs Schemas

Loyihada `models.py` va `schemas.py` alohida vazifalarni bajaradi.

## 🗄️ Models

`models.py` database strukturasini ifodalaydi.

```text
models.py
    ↓
SQLAlchemy ORM
    ↓
SQLite Tables
```

Masalan:

```text
Users     → users
Authors   → authors
Books     → books
Loans     → loans
```

---

## ✅ Schemas

`schemas.py` API orqali keladigan va qaytadigan ma'lumotlarni validatsiya qilish uchun ishlatiladi.

```text
Client
   │
   ▼
Pydantic Schema
   │
   ▼
Validation
   │
   ▼
Service
   │
   ▼
SQLAlchemy Model
   │
   ▼
Database
```

Bu yondashuv API request/response ma'lumotlarini database modelidan ajratishga yordam beradi.

---

# 🧠 Services Layer

Har bir application modulida:

```text
services.py
```

mavjud.

Services qatlamining vazifasi — asosiy business logic'ni routerlardan ajratish.

```text
Router
   │
   ▼
Service
   │
   ▼
Database
```

Bu arxitektura routerlarni juda katta bo‘lib ketishidan saqlaydi va kodni qayta ishlatishni osonlashtiradi.

---

# 🌐 API Architecture

API quyidagi asosiy modullarga bo‘lingan:

```text
                    ┌──────────────────┐
                    │    FastAPI App   │
                    └────────┬─────────┘
                             │
          ┌──────────────────┼──────────────────┐
          │                  │                  │
          ▼                  ▼                  ▼
     👤 Users          ✍️ Authors          📚 Books
          │                  │                  │
          └──────────────────┼──────────────────┘
                             │
                             ▼
                         🔄 Loans
                             │
                             ▼
                       🗄️ SQLite
```

`main.py` barcha routerlarni FastAPI application'ga ulaydi va application ishga tushganda `Base.metadata.create_all()` orqali modellar asosidagi jadvallarni yaratadi.

---

# ⚡ Getting Started

## 1️⃣ Clone repository

```bash
git clone https://github.com/javlonbeksaidov-developer/library-fastapi-project.git
```

## 2️⃣ Project folderga kiring

```bash
cd library-fastapi-project
```

## 3️⃣ Virtual environment yarating

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 4️⃣ Dependencies o‘rnating

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Serverni ishga tushiring

```bash
uvicorn main:app --reload
```

---

# 📖 API Documentation

Server ishga tushgandan keyin FastAPI tomonidan yaratiladigan interaktiv documentation'dan foydalanishingiz mumkin:

```text
Swagger UI
    ↓
/docs

ReDoc
    ↓
/redoc
```

Swagger UI orqali endpointlarni bevosita browserdan test qilish mumkin.

---

# 🔥 API Workflow

### 👤 User

```text
Create User
     ↓
Validate Schema
     ↓
Service
     ↓
SQLAlchemy
     ↓
SQLite
```

### 📚 Book

```text
Create Book
     ↓
Select Author
     ↓
Store author_id
     ↓
Save Book
```

### 🔄 Loan

```text
User
  │
  ▼
Select Book
  │
  ▼
Check available_quantity
  │
  ▼
Create Loan
  │
  ▼
Update Book Quantity
  │
  ▼
Book Borrowed 📚
```

---

# 🧪 Main Concepts Practiced

Ushbu loyiha davomida quyidagi backend tushunchalari amaliyotda qo‘llangan:

* 🐍 Python
* ⚡ FastAPI
* 🗄️ SQLite
* 🔗 SQLAlchemy ORM
* ✅ Pydantic
* 🧩 Modular Architecture
* 🌐 REST API
* 🔀 APIRouter
* 🏗️ SQLAlchemy Models
* 🔐 ForeignKey
* 🔗 Relationship
* 🏷️ Enum
* 📦 CRUD
* 🧠 Service Layer
* 💉 FastAPI Dependency Injection
* 🗃️ Database Sessions
* 📖 Swagger Documentation

---

# 👨‍💻 Author

<p align="center">

### Javlonbek Saidov

🐍 Python Backend Developer

</p>

<p align="center">

**Python • FastAPI • Django • SQLAlchemy • SQLite • PostgreSQL**

</p>

---


