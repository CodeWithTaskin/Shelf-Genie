const movieTitles = [
  'The Dark Knight',
  'Inception',
  'Pulp Fiction',
  'Forrest Gump',
  'Interstellar',
  'The Matrix',
  'Gladiator',
  'Titanic',
  'Jurassic Park',
  'Avatar',
  'The Avengers',
  'Star Wars',
  'The Godfather',
  'Fight Club',
  'Goodfellas',
  'Casablanca',
  "Schindler's List",
  'The Departed',
  'Whiplash',
  'Parasite',
];

// DOM elements
const movieGrid = document.getElementById('movie-grid');
const searchInput = document.getElementById('search-input');
const loader = document.getElementById('loader');
const mobileMenuBtn = document.getElementById('mobile-menu-btn');
const navLinks = document.getElementById('nav-links');

let allMovies = [];
let currentMovies = [];

// Toggle mobile menu
mobileMenuBtn.addEventListener('click', () => {
  navLinks.classList.toggle('active');
});

// Generate movies with more details
const generateMovies = () => {
  loader.style.display = 'block';

  // Simulate loading delay
  setTimeout(() => {
    allMovies = Array(52)
      .fill()
      .map((_, i) => {
        const title =
          movieTitles[Math.floor(Math.random() * movieTitles.length)];
        const year = 1990 + Math.floor(Math.random() * 30);
        const genre = ['Action', 'Drama', 'Comedy', 'Sci-Fi', 'Thriller'][
          Math.floor(Math.random() * 5)
        ];

        return {
          id: i + 1,
          title: title,
          year: year,
          rating: ['PG-13', 'R', '18+'][Math.floor(Math.random() * 3)],
          duration: `${Math.floor(Math.random() * 2) + 1}h ${Math.floor(
            Math.random() * 60
          )}m`,
          genre: genre,
          description: `A compelling story about adventure, friendship, and discovery. ${title} takes you on an unforgettable journey through amazing landscapes and emotional moments. Released in ${year}, this film has captivated audiences worldwide.`,
          image: `https://picsum.photos/400/600?random=${
            i + 100
          }&blur=${Math.floor(Math.random() * 2)}`,
          popularity: Math.floor(Math.random() * 100),
        };
      });

    // Sort by popularity
    allMovies.sort((a, b) => b.popularity - a.popularity);
    currentMovies = [...allMovies];

    renderMovies(currentMovies);
    loader.style.display = 'none';
  }, 1000);
};

// Movie card template
const createMovieCard = movie => {
  const card = document.createElement('div');
  card.className = 'movie-card';
  card.innerHTML = `
        <img src="${movie.image}" alt="${movie.title}" class="movie-image">
        <div class="movie-info">
            <h3 class="movie-title">${movie.title}</h3>
            <div class="movie-meta">
                <span class="movie-year"><i class="far fa-calendar"></i> ${movie.year}</span>
                <span class="movie-rating"><i class="fas fa-ticket"></i> ${movie.rating}</span>
                <span class="movie-genre"><i class="fas fa-tag"></i> ${movie.genre}</span>
            </div>
        </div>
    `;
  card.addEventListener('click', () => {
    window.location.href = `details.html?id=${movie.id}`;
  });
  return card;
};

// Render movies
const renderMovies = movies => {
  movieGrid.innerHTML = '';

  if (movies.length === 0) {
    movieGrid.innerHTML = `
            <div class="no-results">
                <i class="fas fa-film"></i>
                <h3>No Books Found</h3>
                <p>Try a different search term</p>
            </div>
        `;
    return;
  }

  movies.forEach(movie => {
    movieGrid.appendChild(createMovieCard(movie));
  });
};

// Search functionality
const handleSearch = searchTerm => {
  if (searchTerm.length === 0) {
    currentMovies = [...allMovies];
    renderMovies(currentMovies);
    return;
  }

  const filtered = allMovies.filter(
    movie =>
      movie.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
      movie.year.toString().includes(searchTerm) ||
      movie.genre.toLowerCase().includes(searchTerm.toLowerCase())
  );

  currentMovies = filtered;
  renderMovies(currentMovies);
};

// Event listeners
document.addEventListener('DOMContentLoaded', () => {
  generateMovies();

  searchInput.addEventListener('input', e => {
    handleSearch(e.target.value.trim());
  });

  // Navbar scroll effect
  window.addEventListener('scroll', () => {
    if (window.scrollY > 50) {
      document.querySelector('.navbar').classList.add('scrolled');
    } else {
      document.querySelector('.navbar').classList.remove('scrolled');
    }
  });
});
