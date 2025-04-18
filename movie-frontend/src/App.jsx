import { useState } from 'react'
import Search from './components/search'
import Results from './components/results'
import useMovies from './hooks/useMovies'
import './App.css'

function App() {
  const [searchTerm, setSearchTerm] = useState('')
  const {movies, loading, error} = useMovies(searchTerm)

  const handleSearch = (term) => {
    setSearchTerm(term);
  };
  return (
    <div className="app">
      <header className="app-header">
        <h1>Movie Search App</h1>
      </header>
      <main>
        <Search onSearch={handleSearch} />
        <Results movies={movies} loading={loading} error={error} />
      </main>
    </div>
  );
}

export default App;
