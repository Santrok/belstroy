const detailsNavListItem = document.querySelectorAll('.projects__details-nav-scheme-list-item')
const additionalItem = document.querySelector('.projects__details-scheme-img-wrapper').children
detailsNavListItem.forEach(item => {
    item.addEventListener('click', () => {
        detailsNavListItem.forEach(el => {
            el.classList.remove('projects__details-nav-scheme-list-item-active')
        })
        item.classList.add('projects__details-nav-scheme-list-item-active')
        Array.from(additionalItem).forEach(el => el.style.display = 'none')
        additionalItem[item.dataset.id].style.display = 'grid';
    })
})