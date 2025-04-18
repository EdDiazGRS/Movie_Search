🎬 Movie Search Application

A full-stack application for searching and browsing movies using the TMDB API.

Overview

This project consists of a Django REST API backend and a React frontend. Users can search for movies, and the application will retrieve data from a local database. If the movie is not found locally, the backend will automatically fetch it from The Movie Database (TMDB) API, store it, and return it to the user.

Features

Search for movies by title
View movie details including title, release date, genre, user score, and overview
Automatic fetching of movie data from TMDB when not available locally
Responsive card layout for movie results
Client-side filtering by year and keywords in movie overview
Movie poster images displayed from TMDB
Tech Stack

Backend:

Django
Django REST Framework
PostgreSQL
Requests (for API calls)
Frontend:

React (Vite)
Axios (for API requests)
CSS3
Setup and Installation

Prerequisites
Python 3.x
Node.js and npm
PostgreSQL
Backend Setup
Clone the repository:
bash
Copy
Edit
git clone https://github.com/EdDiazGRS/Movie_Search.git
cd Movie_Search
Create and activate a virtual environment:
bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install backend dependencies:
nginx
Copy
Edit
pip install -r requirements.txt
Set up the PostgreSQL database:
pgsql
Copy
Edit
# Connect to PostgreSQL
psql

# In the PostgreSQL CLI
CREATE DATABASE mydatabase;
CREATE USER myuser WITH PASSWORD 'mypassword';
GRANT ALL PRIVILEGES ON DATABASE mydatabase TO myuser;
GRANT ALL ON SCHEMA public TO myuser;
\q
Configure environment variables:
Create a .env file in the Django project root and add:

ini
Copy
Edit
TMDB_API_KEY=your_tmdb_api_key
DATABASE_URL=postgres://myuser:mypassword@localhost:5432/mydatabase
Run migrations and start the backend server:
nginx
Copy
Edit
python manage.py migrate
python manage.py runserver
Frontend Setup
Navigate to the frontend directory:
bash
Copy
Edit
cd frontend
Install frontend dependencies:
nginx
Copy
Edit
npm install
Configure environment variables:
Create a .env file in the frontend/ directory and add:

bash
Copy
Edit
VITE_API_URL=http://localhost:8000/api
Start the development server:
arduino
Copy
Edit
npm run dev
Access the application at: http://localhost:5173

API Endpoints

GET /api/movies/ – List all movies or search using a query parameter (e.g. ?search=batman)
GET /api/movies/{id}/ – Retrieve a specific movie by ID
Models

Movie Model Fields:

title: Movie title
genre: Movie genre(s)
user_score: User rating score (0–100)
release_date: Movie release date
overview: Brief description of the movie
poster_path: Path to the movie poster image
External API Integration

This application uses The Movie Database (TMDB) API to fetch movie data.
You'll need to register for a TMDB API key at https://www.themoviedb.org and add it to your backend .env file.

Future Improvements

User authentication
Ability to save favorite movies
More detailed movie information
Pagination for large result sets
Enhanced filtering options
Movie recommendations
License

This project is licensed under the MIT License – see the LICENSE file for details.

Acknowledgments

The Movie Database (TMDB) for providing the movie data API
Django and React communities for their excellent documentation and support
