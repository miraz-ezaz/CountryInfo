# Country Info App

This Django application fetches country data from the [REST Countries API](https://restcountries.com/v3.1/all), stores it in a local database, provides RESTful APIs, and displays the data via a secure web interface.

Repository: [https://github.com/miraz-ezaz/CountryInfo](https://github.com/miraz-ezaz/CountryInfo)

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/miraz-ezaz/CountryInfo.git
cd CountryInfo
````

### 2. Create and Activate Virtual Environment

Create a virtual environment named `venv`:

```bash
python -m venv venv
```

Activate the virtual environment:

* **On Windows:**

  ```bash
  venv\Scripts\activate
  ```

* **On macOS/Linux:**

  ```bash
  source venv/bin/activate
  ```

### 3. Install Requirements

Install all necessary dependencies:

```bash
pip install -r requirements.txt
```

---

### 4. Apply Migrations

After setting up models, run the following commands to initialize the database:

```bash
python manage.py makemigrations
python manage.py migrate
```

---

### 5. Populate the Database with Country Data

Run the custom management command to fetch and store data from the REST Countries API:

```bash
python manage.py fetch_countries
```

You’ll see logs for each country as it’s being added.

---

## Database

This project uses Django’s **default SQLite3 database**, as it’s sufficient for assignment/demo purposes and doesn’t require additional configuration.

The database file will be created automatically as `db.sqlite3` in the project root after running migrations.

---
