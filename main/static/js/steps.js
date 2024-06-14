const tabItems = document.querySelectorAll('.steps__tab-list-item');
const stepsItems = document.querySelectorAll('.steps__list-item');

tabItems.forEach(item => {
    item.addEventListener('click', (e) => {
        stepsItems.forEach(el => {
            el.classList.remove('steps__list-item-active')
        })
        stepsItems[e.currentTarget.dataset.stepIndex].classList.add('steps__list-item-active')
        tabItems.forEach(el => {
            el.classList.remove('steps__tab-list-item-active')
        })
        e.currentTarget.classList.add('steps__tab-list-item-active')
    })
})