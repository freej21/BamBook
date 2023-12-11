// Success message
setTimeout(function() {
    var successMessages = document.querySelectorAll('.alert-success');
    successMessages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000);

// Error message
setTimeout(function() {
    var errorMessages = document.querySelectorAll('.alert-danger');
    errorMessages.forEach(function(message) {
        message.style.display = 'none';
    });
}, 5000);
