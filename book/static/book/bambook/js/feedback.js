// JavaScript for star rating interaction
document.addEventListener("DOMContentLoaded", function () {
  const stars = document.querySelectorAll(".rating input[type='radio']");
  
  stars.forEach((star) => {
    star.addEventListener("change", function () {
      // Update the rating_input hidden field with the selected rating
      const selectedRating = this.value;
      document.getElementById("rating_input").value = selectedRating;
    });
  });
});


