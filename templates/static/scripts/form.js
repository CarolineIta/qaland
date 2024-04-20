document.querySelectorAll('input').forEach(input => {
    input.addEventListener('focus', () => {
        input.nextElementSibling.classList.add('active');
    });
    input.addEventListener('blur', () => {
        if (input.value === '') {
            input.nextElementSibling.classList.remove('active');
        }
    });
});