const burgerBtn = document.querySelector('.main__nav-burger')
const mainNavList = document.querySelector('.main__nav-list-wrapper');
const mainNavListItem = document.querySelectorAll('.main__nav-list-item')

burgerBtn.addEventListener('click', () => {
    mainNavList.classList.toggle('main__nav-active')
    burgerBtn.classList.toggle('main__nav-burger-active')
})

mainNavListItem.forEach(item => {
    item.addEventListener('click', () => {
        mainNavList.classList.remove('main__nav-active')
        burgerBtn.classList.remove('main__nav-burger-active')
    })
})
