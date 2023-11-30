let currentRating = 0;

function rate(rating) {
    currentRating = rating;
    updateStars();
}

function updateStars() {
    const stars = document.querySelectorAll('.rating-star');
    stars.forEach((star, index) => {
        star.classList.toggle('active', index < currentRating);
    });
}
