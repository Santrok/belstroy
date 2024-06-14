const faqItems = document.querySelectorAll('.faq__list-footer');

faqItems.forEach(item => {
    item.addEventListener('click', (e) => {
        e.currentTarget.parentElement.classList.toggle('faq__active')
    })
})