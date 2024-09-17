document.addEventListener("DOMContentLoaded", function() {
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.classList.add('hide');
        }, 3000);
    });
});