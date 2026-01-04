# Superheroes API

A Flask REST API for managing superheroes, their powers, and the associations between them.

## Features

- **Heroes Management**: Create and retrieve superhero information
- **Powers Management**: Manage superpowers with validation
- **Hero-Power Associations**: Link heroes to powers with strength ratings
- **RESTful Endpoints**: Clean, standard REST API design
- **Data Validation**: Ensures data integrity with validated descriptions and strength levels

## Tech Stack

- **Framework**: Flask & Flask-RESTful
- **Database**: SQLAlchemy ORM with PostgreSQL/SQLite
- **Migrations**: Flask-Migrate
- **Dependencies**: Pipenv

## Installation

### Prerequisites

- Python 3.8+
- pipenv

### Setup

1. Install dependencies:

   ```bash
   pipenv install
   ```

2. Activate virtual environment:

   ```bash
   pipenv shell
   ```

3. Initialize database migrations:

   ```bash
   flask db init
   ```

4. Create and apply migrations:

   ```bash
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

5. Seed the database:
   ```bash
   python seed.py
   ```

### Alternative Setup (Automated)

Run the setup script for your platform:

**Linux/Mac:**

```bash
./setup.sh
```

**Windows:**

```bash
setup.bat
```

## Running the Application

Start the Flask development server:

```bash
python app.py
```

The API will be available at `http://localhost:5555`

## API Endpoints

### GET /heroes

Retrieve all heroes.

**Response:**

```json
[
  {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  }
]
```

### GET /heroes/<int:id>

Retrieve a specific hero with their powers.

**Response:**

```json
{
  "id": 1,
  "name": "Kamala Khan",
  "super_name": "Ms. Marvel",
  "hero_powers": [
    {
      "id": 1,
      "hero_id": 1,
      "power_id": 2,
      "strength": "Strong",
      "power": {
        "id": 2,
        "name": "flight",
        "description": "gives the wielder the ability to fly through the skies at supersonic speed"
      }
    }
  ]
}
```

### GET /powers

Retrieve all powers.

**Response:**

```json
[
  {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
]
```

### GET /powers/<int:id>

Retrieve a specific power.

**Response:**

```json
{
  "id": 1,
  "name": "super strength",
  "description": "gives the wielder super-human strengths"
}
```

### PATCH /powers/<int:id>

Update a power's description.

**Request Body:**

```json
{
  "description": "Your updated description (minimum 20 characters)"
}
```

**Response:**

```json
{
  "id": 1,
  "name": "super strength",
  "description": "Your updated description (minimum 20 characters)"
}
```

### POST /hero_powers

Associate a hero with a power.

**Request Body:**

```json
{
  "strength": "Strong",
  "power_id": 1,
  "hero_id": 1
}
```

**Response:**

```json
{
  "id": 11,
  "hero_id": 1,
  "power_id": 1,
  "strength": "Strong",
  "hero": {
    "id": 1,
    "name": "Kamala Khan",
    "super_name": "Ms. Marvel"
  },
  "power": {
    "id": 1,
    "name": "super strength",
    "description": "gives the wielder super-human strengths"
  }
}
```

## Database Schema

### Heroes Table

| Column     | Type        | Description |
| ---------- | ----------- | ----------- |
| id         | Integer     | Primary key |
| name       | String(100) | Real name   |
| super_name | String(100) | Hero alias  |

### Powers Table

| Column      | Type        | Description                      |
| ----------- | ----------- | -------------------------------- |
| id          | Integer     | Primary key                      |
| name        | String(100) | Power name                       |
| description | String(500) | Power description (min 20 chars) |

### HeroPowers Table (Join Table)

| Column   | Type       | Description                           |
| -------- | ---------- | ------------------------------------- |
| id       | Integer    | Primary key                           |
| strength | String(50) | Strength rating (Strong/Weak/Average) |
| hero_id  | Integer    | Foreign key to Hero                   |
| power_id | Integer    | Foreign key to Power                  |

## Validation Rules

### Power Description

- Must be present
- Must be at least 20 characters long

### HeroPower Strength

- Must be one of: `Strong`, `Weak`, `Average`

## Testing

Run the API tests:

```bash
python test_api.py
```

The test script will verify:

- GET /heroes
- GET /heroes/:id
- GET /powers
- GET /powers/:id
- POST /hero_powers
- PATCH /powers/:id

## Postman Collection

Import the `challenge-2-superheroes.postman_collection.json` file into Postman to test the API with pre-configured requests.

## Project Structure

```
superheroes-api/
├── app.py                    # Main Flask application
├── models.py                 # SQLAlchemy models
├── seed.py                   # Database seeding script
├── migrations.py             # Flask-Migrate configuration
├── test_api.py               # API test script
├── requirements.txt          # pip requirements
├── Pipfile                   # Pipenv dependencies
├── setup.sh                  # Linux/Mac setup script
├── setup.bat                 # Windows setup script
├── challenge-2-superheroes.postman_collection.json
└── migrations/               # Database migrations
```

## License

MIT
