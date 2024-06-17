const consultationFormBtn = document.querySelector(".excursion__form button");
const footerFormBtn = document.querySelector(".footer__form button");
const consultationBtn = document.querySelector(".excursion__form button");
const successModal = document.querySelector(".success__modal");
const successModalCross = document.querySelector(".success__modal .cross");

function getCookie(name) {
  const cookie = document.cookie.split(";");
  for (let i of cookie) {
    const [cookieName, cookieValue] = i.trim().split("=");
    if (cookieName == name) {
      return cookieValue;
    }
  }
}

consultationFormBtn.addEventListener("click", () => {
  const form = document.querySelector(".excursion__form");
  const data = new FormData(form);
  fetch(`${localStorage.getItem("url")}api/create_consultation/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: data,
  }).then((resp) => {
    console.log(resp);
    if (resp.status === 200 || resp.status === 201) {
      successModal.classList.add("success__modal-active");
      document.body.style.overflow = "hidden";
    }
  });
});


successModal.addEventListener("click", (e) => {
  if (e.target === successModal) {
    document.body.style.overflow = "auto";
    successModal.classList.remove("success__modal-active");
  }
});

successModalCross.addEventListener("click", () => {
  successModal.classList.remove("success__modal-active");
  document.body.style.overflow = "auto";
});

footerFormBtn.addEventListener("click", () => {
  const data = new FormData(document.querySelector(".footer__form"));
  fetch(`${localStorage.getItem("url")}api/consultation/`, {
    method: "POST",
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
    body: data,
  });
});
