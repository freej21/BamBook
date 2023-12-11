// Get references to the login button and login form
const loginButton = document.querySelector('.login-button');
const loginForm = document.querySelector('.login-form');

// Add a click event listener to the login button
loginButton.addEventListener('click', function(e) {
  e.preventDefault(); // Prevent the form from submitting (if used in a real form)
  
  // Toggle the visibility of the login form
  if (loginForm.style.display === 'block') {
    loginForm.style.display = 'none';
  } else {
    loginForm.style.display = 'block';
  }
});
