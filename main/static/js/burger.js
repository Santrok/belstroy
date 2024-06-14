const burgerBtn = document.querySelector('.main__nav-burger')
const mainNavList = document.querySelector('.main__nav-list-wrapper');

burgerBtn.addEventListener('click', () => {
    mainNavList.classList.toggle('main__nav-active')
    burgerBtn.classList.toggle('main__nav-burger-active')
})