const consultationBtn = document.querySelector(".excursion__form button");
const successModal = document.querySelector(".success__modal");
const successModalCross = document.querySelector(".success__modal .cross");

consultationBtn.addEventListener("click", () => {
  successModal.classList.add("success__modal-active");
  document.body.style.overflow = "hidden";
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
