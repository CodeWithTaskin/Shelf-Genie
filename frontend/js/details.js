const movies = Array(30)
  .fill()
  .map((_, i) => {
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
    const actorNames = [
      'Christian Bale',
      'Tom Hardy',
      'Leonardo DiCaprio',
      'Matthew McConaughey',
      'Morgan Freeman',
      'Anne Hathaway',
      'Brad Pitt',
      'Samuel L. Jackson',
      'Robert De Niro',
      'Meryl Streep',
      'Cate Blanchett',
      'Denzel Washington',
      'Emma Stone',
      'Ryan Gosling',
      'Jennifer Lawrence',
    ];
    const roles = [
      'Lead Actor',
      'Supporting Actor',
      'Lead Actress',
      'Director',
      'Producer',
      'Screenwriter',
      'Cinematographer',
      'Composer',
      'Cameo',
      'Voice Actor',
    ];

    const castCount = 4 + Math.floor(Math.random() * 3);
    const cast = [];
    for (let j = 0; j < castCount; j++) {
      cast.push({
        name: actorNames[Math.floor(Math.random() * actorNames.length)],
        role: roles[Math.floor(Math.random() * roles.length)],
        img: `https://i.pravatar.cc/150?img=${Math.floor(Math.random() * 70)}`,
      });
    }

    return {
      id: i + 1,
      title: movieTitles[Math.floor(Math.random() * movieTitles.length)],
      year: 1990 + Math.floor(Math.random() * 30),
      rating: ['PG-13', 'R', '18+'][Math.floor(Math.random() * 3)],
      duration: `${Math.floor(Math.random() * 2) + 1}h ${Math.floor(
        Math.random() * 60
      )}m`,
      description:
        'A compelling story about adventure, friendship, and discovery. This movie will take you on an unforgettable journey through amazing landscapes and emotional moments.',
      image: `https://picsum.photos/400/600?random=${i + 100}&blur=${Math.floor(
        Math.random() * 2
      )}`,
      cast: cast,
    };
  });

document.addEventListener('DOMContentLoaded', () => {
  const urlParams = new URLSearchParams(window.location.search);
  const movieId = parseInt(urlParams.get('id')) || 1;
  const movie = movies.find(m => m.id === movieId) || movies[0];

  // Back button functionality
  document.getElementById('back-button').addEventListener('click', () => {
    window.history.back();
  });

  // Set movie details
  document.getElementById('detail-poster').src = movie.image;
  document.getElementById('movie-title').textContent = movie.title;
  document.getElementById(
    'year'
  ).innerHTML = `<i class="far fa-calendar"></i> ${movie.year}`;
  document.getElementById(
    'rating'
  ).innerHTML = `<i class="fas fa-ticket"></i> ${movie.rating}`;
  document.getElementById(
    'duration'
  ).innerHTML = `<i class="far fa-clock"></i> ${movie.duration}`;
  document.getElementById('description').textContent = movie.description;

  // Set cast
  const castContainer = document.getElementById('cast');
  castContainer.innerHTML = '';
  movie.cast.forEach(actor => {
    const div = document.createElement('div');
    div.className = 'cast-member';
    div.innerHTML = `
            <img src="${actor.img}" alt="${actor.name}" class="cast-img">
            <div class="cast-name">${actor.name}</div>
            <div class="cast-role">${actor.role}</div>
        `;
    castContainer.appendChild(div);
  });

  // Generate recommendations
  const recommendations = document.getElementById('recommendations');
  recommendations.innerHTML = '';
  const recommendedMovies = movies
    .filter(m => m.id !== movie.id)
    .sort(() => 0.5 - Math.random())
    .slice(0, 5);

  recommendedMovies.forEach(movie => {
    const card = document.createElement('div');
    card.className = 'recommendation-card';
    card.innerHTML = `
            <img src="${movie.image}" alt="${movie.title}">
            <div class="recommendation-info">
                <h4 class="recommendation-title">${movie.title}</h4>
                <span class="recommendation-year">${movie.year}</span>
            </div>
        `;
    card.addEventListener('click', () => {
      window.location.href = `details.html?id=${movie.id}`;
    });
    recommendations.appendChild(card);
  });
});
