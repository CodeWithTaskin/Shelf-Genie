document.addEventListener('DOMContentLoaded', () => {
  const bookGrid = document.getElementById('movie-grid');
  const searchInput = document.getElementById('search-input');
  const loader = document.getElementById('loader');
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const navLinks = document.getElementById('nav-links');

  // Initialize loader
  loader.style.display = 'flex';

  let allBooks = [];
  let currentBooks = [];

  // Mobile menu toggle
  mobileMenuBtn.addEventListener('click', () => {
    navLinks.classList.toggle('active');
    mobileMenuBtn.setAttribute(
      'aria-expanded',
      navLinks.classList.contains('active')
    );
  });

  // Close mobile menu when clicking outside
  document.addEventListener('click', e => {
    if (
      !navLinks.contains(e.target) &&
      !mobileMenuBtn.contains(e.target) &&
      navLinks.classList.contains('active')
    ) {
      navLinks.classList.remove('active');
      mobileMenuBtn.setAttribute('aria-expanded', 'false');
    }
  });

  // Fetch books with error handling
  const fetchBooks = async () => {
    try {
      const res = await fetch('http://52.186.168.197:5000/');
      if (!res.ok) throw new Error('Network response was not ok');

      const data = await res.json();
      const books = JSON.parse(data['Top-Books']);

      allBooks = Object.entries(books).map(([key, book]) => ({
        id: key,
        title: book['Book-Title'],
        author: book['Book-Author'],
        year: book['Year-Of-Publication'],
        publisher: book['Publisher'],
        rating: book['avg_of_reating']?.toFixed(1) || 'N/A',
        image: book['Image-URL-L'],
        raw: book,
      }));

      currentBooks = [...allBooks];
      renderBooks(currentBooks);
    } catch (err) {
      console.error('Error fetching books:', err);
      bookGrid.innerHTML = `
          <div class="no-results">
            <i class="fas fa-exclamation-triangle"></i>
            <h3>Failed to Load Books</h3>
            <p>Please check your connection and try again</p>
          </div>
        `;
    } finally {
      loader.style.display = 'none';
    }
  };

  // Create book card element
  const createBookCard = book => {
    const card = document.createElement('div');
    card.className = 'movie-card';
    card.innerHTML = `
        <img src="${book.image}" alt="${book.title}" class="movie-image" loading="lazy">
        <div class="movie-info">
          <h3 class="movie-title">${book.title}</h3>
          <div class="movie-meta">
            <span><i class="far fa-calendar"></i> ${book.year}</span>
            <span><i class="fas fa-star"></i> ${book.rating}</span>
            <span><i class="fas fa-user"></i> ${book.author}</span>
          </div>
        </div>
      `;

    card.addEventListener('click', () => {
      sessionStorage.setItem('selectedBook', JSON.stringify(book));
      window.location.href = `details.html`;
    });

    return card;
  };

  // Render books to the grid
  const renderBooks = books => {
    bookGrid.innerHTML = '';

    if (books.length === 0) {
      bookGrid.innerHTML = `
          <div class="no-results">
            <i class="fas fa-book"></i>
            <h3>No Books Found</h3>
            <p>Try a different search term</p>
          </div>
        `;
      return;
    }

    books.forEach(book => {
      bookGrid.appendChild(createBookCard(book));
    });
  };

  // Search function with debounce
  let searchTimeout;
  const handleSearch = searchTerm => {
    clearTimeout(searchTimeout);

    if (!searchTerm.trim()) {
      currentBooks = [...allBooks];
      renderBooks(currentBooks);
      return;
    }

    loader.style.display = 'flex';

    searchTimeout = setTimeout(() => {
      const filtered = allBooks.filter(
        book =>
          book.title.toLowerCase().includes(searchTerm.toLowerCase()) ||
          book.author.toLowerCase().includes(searchTerm.toLowerCase()) ||
          book.year.toString().includes(searchTerm)
      );

      currentBooks = filtered;
      renderBooks(currentBooks);
      loader.style.display = 'none';
    }, 300);
  };

  // Navbar scroll effect
  window.addEventListener('scroll', () => {
    document
      .querySelector('.navbar')
      .classList.toggle('scrolled', window.scrollY > 50);
  });

  // Event listeners
  searchInput.addEventListener('input', e =>
    handleSearch(e.target.value.trim())
  );

  // Initialize
  fetchBooks();
});
