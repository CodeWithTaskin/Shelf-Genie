document.addEventListener('DOMContentLoaded', async () => {
  const backButton = document.getElementById('back-button');
  const poster = document.getElementById('detail-poster');
  const titleEl = document.getElementById('movie-title');
  const yearEl = document.getElementById('year');
  const ratingEl = document.getElementById('rating');
  const authorEl = document.getElementById('author');
  const descriptionEl = document.getElementById('description');
  const recommendationsEl = document.getElementById('recommendations');

  // Back button functionality
  backButton.addEventListener('click', () => window.history.back());

  // Get selected book from session storage
  const selectedBookJSON = sessionStorage.getItem('selectedBook');
  if (!selectedBookJSON) {
    document.body.innerHTML = `
        <div class="no-results" style="text-align:center; padding:5rem">
          <h2>Book not found</h2>
          <p>Please go back and select a book</p>
          <button onclick="window.history.back()" style="margin-top:1rem">
            Go Back
          </button>
        </div>
      `;
    return;
  }

  const book = JSON.parse(selectedBookJSON);

  // Display book details
  poster.src = book.image;
  poster.alt = `${book.title} cover`;
  titleEl.textContent = book.title;
  yearEl.innerHTML = `<i class="far fa-calendar"></i> ${book.year}`;
  ratingEl.innerHTML = `<i class="fas fa-star"></i> ${book.rating}`;
  authorEl.innerHTML = `<i class="fas fa-user"></i> ${book.author}`;
  descriptionEl.textContent = `Published by ${book.publisher}. ${book.title} by ${book.author} has received positive reviews from readers.`;

  // Fetch recommendations
  try {
    const res = await fetch('http://52.186.168.197:5000/recommendation', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ name: book.title }),
    });

    if (!res.ok) throw new Error('Recommendations failed');

    const data = await res.json();
    const recommendedBooks = Object.values(
      JSON.parse(data['Recommended-Books'])
    );

    recommendationsEl.innerHTML = '';

    recommendedBooks.forEach(rec => {
      const card = document.createElement('div');
      card.className = 'recommendation-card';
      card.innerHTML = `
          <img src="${rec['Image-URL-L']}" alt="${rec['Book-Title']}" loading="lazy">
          <div class="recommendation-info">
            <h4 class="recommendation-title">${rec['Book-Title']}</h4>
            <span class="recommendation-year">${rec['Year-Of-Publication']}</span>
          </div>
        `;

      card.addEventListener('click', () => {
        sessionStorage.setItem(
          'selectedBook',
          JSON.stringify({
            id: rec['Unnamed: 0'],
            title: rec['Book-Title'],
            author: rec['Book-Author'],
            year: rec['Year-Of-Publication'],
            publisher: rec['Publisher'],
            rating: rec['avg_of_reating']?.toFixed(1) || 'N/A',
            image: rec['Image-URL-L'],
          })
        );
        window.location.reload();
      });

      recommendationsEl.appendChild(card);
    });
  } catch (err) {
    console.error('Failed to fetch recommendations', err);
    recommendationsEl.innerHTML = `
        <div class="no-results">
          <i class="fas fa-exclamation-circle"></i>
          <p>Failed to load recommendations</p>
        </div>
      `;
  }
});
