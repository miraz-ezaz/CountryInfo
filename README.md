# Country Info App

This Django application fetches country data from the [REST Countries API](https://restcountries.com/v3.1/all), stores it in a local database, provides RESTful APIs, and displays the data via a secure web interface.

Repository: [https://github.com/miraz-ezaz/CountryInfo](https://github.com/miraz-ezaz/CountryInfo)

---

## Setup Summary

To run this project locally, follow these steps:

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
4. Apply migrations
5. **Populate the database** with country data
6. **Create a superuser**
7. **Run the development server**
8. Log in and explore the web or API interface

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/miraz-ezaz/CountryInfo.git
cd CountryInfo
````

---

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
```

Activate it:

* **Windows:**

  ```bash
  venv\Scripts\activate
  ```
* **macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

---

### 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Populate the Database with Country Data

```bash
python manage.py fetch_countries
```

This will fetch data from the REST Countries API and populate your local database.

---

### 6. Create Superuser

To log in to the admin panel or the protected country list page:

```bash
python manage.py createsuperuser
```

Follow the prompt to set a username and password.

---

### 7. Run the Development Server

```bash
python manage.py runserver
```

Visit: [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

---

## Database

This project uses Django’s **default SQLite3** database.

* The file `db.sqlite3` will be created automatically after migrations.
* No external DB configuration is required.

---

## Authentication & Security

### Login Page

Go to:

```
http://127.0.0.1:8000/login/
```

Use the superuser credentials created earlier.

---

### Secured Web Interface

The country list and detail pages are **only accessible after login**:

* Country list: `http://127.0.0.1:8000/countries/`
* Country detail (example): `http://127.0.0.1:8000/countries/34/`

Unauthenticated users will be redirected to the login page.

---

### Secured API Endpoints

All API endpoints require authentication.

You can test them using:

* Django session cookies (after login)

---

## REST API Documentation

All API endpoints are prefixed with `/api/` and are **protected by authentication**. You must be logged in to access them.

### Authentication Required

* Before accessing the APIs, log in at:
  `http://127.0.0.1:8000/login/`

* Then test authenticated routes using browser.

---

### API Endpoints

| Method | Endpoint                               | Description                  |
| ------ | -------------------------------------- | ---------------------------- |
| GET    | `/api/countries/`                      | List all countries           |
| POST   | `/api/countries/`                      | Create a new country         |
| GET    | `/api/countries/<id>/`                 | Retrieve a specific country  |
| PUT    | `/api/countries/<id>/`                 | Update an existing country   |
| DELETE | `/api/countries/<id>/`                 | Delete a country             |
| GET    | `/api/countries/search/?q=<name>`      | Search for a country by name |
| GET    | `/api/countries/region/<region_name>/` | List countries by region     |
| GET    | `/api/countries/<id>/same-region/`     | Countries in the same region |
| GET    | `/api/countries/language/<lang_code>/` | List countries by language   |

---
### Notes

- `<id>` is the numeric ID of the country (e.g., `/api/countries/34/`)
- `<region_name>` and `<lang_code>` are case-insensitive strings
- All responses are in JSON format
- Non-authenticated requests will return `403 Forbidden`

---

## Default Redirects

* Visiting the root URL `/` will redirect to `/countries/`
* After login, users are redirected to the country list page

---

## Admin Panel

Access Django's admin interface:

```
http://127.0.0.1:8000/admin/
```

Log in using the superuser credentials.

---