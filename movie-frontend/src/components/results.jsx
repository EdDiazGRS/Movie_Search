// src/components/Results.jsx
import React, { useState } from 'react';

const Results = ({ movies, loading, error }) => {
  const [yearFilter, setYearFilter] = useState('');
  const [keywordFilter, setKeywordFilter] = useState('');

  // Filter movies based on year and keyword
  const filteredMovies = movies.filter(movie => {
    // Year filter
    if (yearFilter && movie.release_date) {
      const movieYear = new Date(movie.release_date).getFullYear().toString();
      if (!movieYear.includes(yearFilter)) return false;
    }
    
    // Keyword filter for overview
    if (keywordFilter && movie.overview) {
      if (!movie.overview.toLowerCase().includes(keywordFilter.toLowerCase())) {
        return false;
      }
    }
    
    return true;
  });

  if (loading) {
    return <div className="loading">Loading movies...</div>;
  }

  if (error) {
    return <div className="error">{error}</div>;
  }

  if (!movies.length) {
    return <div className="no-results">No movies found. Try searching for something else.</div>;
  }

  return (
    // In your Results.jsx component
      <div className="movie-list">
        <h2>Movie Results ({filteredMovies.length})</h2>
        {filteredMovies.length === 0 ? (
          <p>No movies match your filters.</p>
        ) : (
          filteredMovies.map((movie) => (
            <div key={movie.id} className="movie-card">
              {movie.poster_path ? (
                <img 
                  src={`https://image.tmdb.org/t/p/w500${movie.poster_path}`}
                  alt={`${movie.title} poster`}
                  className="movie-poster"
                />
              ) : (
                <div className="movie-poster-placeholder">No Image</div>
              )}
              
              <div className="movie-info">
                <h3>{movie.title}</h3>
                <p className="release-date">
                  Released: {movie.release_date ? new Date(movie.release_date).toLocaleDateString() : 'Unknown'}
                </p>
                <p className="genre-container">
                  {movie.genre.split(',').map((g, i) => (
                    <span key={i} className="genre">{g.trim()}</span>
                  ))}
                </p>
                {movie.user_score && (
                  <div className="score-badge">{movie.user_score}%</div>
                )}
                <p className="overview">{movie.overview || 'No overview available.'}</p>
              </div>
            </div>
          ))
        )}
      </div>

        
          
  );
};

export default Results;