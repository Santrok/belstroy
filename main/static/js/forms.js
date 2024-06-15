const consultationFormBtn = document.querySelector('.excursion__form button')
const footerFormBtn = document.querySelector('.footer__form button')

console.log(consultationFormBtn);

function getCookie(name) {
    const cookie = document.cookie.split(";");
    for (let i of cookie) {
      const [cookieName, cookieValue] = i.trim().split("=");
      if (cookieName == name) {
        return cookieValue;
      }
    }
  }

consultationFormBtn.addEventListener('click', () => {
    const form = document.querySelector('.excursion__form')
    const data = new FormData(form)
    fetch(`${localStorage.getItem('url')}api/create_consultation/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: data,
    })
})


footerFormBtn.addEventListener('click', () => {
    const data = new FormData(document.querySelector('.footer__form'))
    fetch(`${localStorage.getItem('url')}api/consultation/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': getCookie('csrftoken'),
        },
        body: data,
    })
})