const reviewsItem = document.querySelectorAll(".reviews__list-item");
const modals = document.querySelector(".modals");
const reviewModal = document.querySelector(".review__modal");
const cross = document.querySelector(".cross");
const modalAuthor = document.querySelector(".review__modal-author");
const modalExpertCity = document.querySelector(".review__modal-expert-city");
const modalText = document.querySelector(".review__modal-text");

if (window.innerWidth <= 992) {
  reviewsItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      const author = e.currentTarget.children[0].children[0].textContent.trim();
      const expertCity = e.currentTarget.children[0].children[1].textContent.trim();
      const text = e.currentTarget.children[1].children[0].textContent.trim();
      modalAuthor.textContent = author;
      modalExpertCity.textContent = expertCity;
      modalText.textContent = text;
      modals.classList.add("modals__active");
      reviewModal.classList.add("modals__active");
      document.body.style.overflow = "hidden";
    });
  });

  cross.addEventListener("click", () => {
    modals.classList.remove("modals__active");
    reviewModal.classList.remove("modals__active");
    document.body.style.overflow = "auto";
  });
}
