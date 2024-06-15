function requestBuilding(url) {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      renderProjects(data, ".projects__list-wrapper");
      projectsDetails();
    })
    .catch((error) => {
      console.log(error);
    });
}

requestBuilding(`${localStorage.getItem("url")}api/material/`);

function renderProjects(arr, className) {
  const backToProjects = document.querySelector(".projects__details-block-back");
  backToProjects.addEventListener("click", () => {
    const porjectsWrapper = document.querySelector(".projects__wrapper");
    porjectsWrapper.children[1].style.display = "none";
    porjectsWrapper.children[0].style.display = "block";
    requestBuilding(`${localStorage.getItem("url")}api/material/`);
  });
  if (typeof className !== "string") return "Error, className is not a string";
  const projectListWrapper = document.querySelector(className);
  projectListWrapper.innerHTML = "";
  for (let i of arr) {
    const div = document.createElement("div");
    div.classList.add("projects__list-building-type");
    div.innerHTML = `
                    <div class="projects__list-building-type-title">
                        ${i.material}
                    </div>
                    <ul class="projects__list">
                    ${i.house_set
                      .map((item) => {
                        return `
                        <li class="projects__list-item-wrapper">
                            <article class="projects__list-item" data-id="${item.id}">
                                <div class="projects__list-item-link">
                                    <div class="projects__list-item-img">
                                        <img src="${item.main_photo}" alt="">
                                    </div>
                                    <footer class="projects__list-item-title-wrap">
                                        <h3 class="projects__list-item-title">
                                            ${item.name}
                                        </h3>
                                        <p class="projects__list-item-square-km">
                                            ${item.square} м<sup>2</sup>
                                        </p>
                                    </footer>
                                </div>
                                <header class="projects__list-item-about-wrapper">
                                    <ul class="projects__list-item-about-list">
                                      <li class="projects__list-item-about">
                                              ${item.room}
                                      </li>
                                      <li class="projects__list-item-about">
                                              ${item.bathroom}
                                      </li>
                                      <li class="projects__list-item-about">
                                              ${item.floor}
                                      </li>
                                    </ul>
                                    <ul class="projects__list-item-about-price-list">
                                      <li>
                                          <p class="projects__list-item-about-price-text">
                                            Стройматериалы
                                          </p>
                                          <p class="projects__list-item-about-price-value">
                                            ${item.building_materials_equipment.trim()} &#8381;
                                          </p>
                                      </li>
                                      <li>
                                          <p class="projects__list-item-about-price-text">
                                              В базовой комплектации
                                          </p>
                                          <p class="projects__list-item-about-price-value">
                                              ${item.cost_of_basic_equipment.trim()} &#8381;
                                          </p>
                                      </li>
                                    </ul>
                                </header>
                            </article>
                        </li>`;
                      })
                      .join("")}
                    </ul>`;
    projectListWrapper.append(div);
  }
}

function projectsDetails() {
  const buildingListItem = document.querySelectorAll(".projects__list-item-link");
  buildingListItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      requestDetails(`${localStorage.getItem("url")}api/house_detail/${e.currentTarget.parentElement.dataset.id}/`);
    });
  });
}

function renderDetails(data) {
  console.log(data);
  const porjectsWrapper = document.querySelector(".projects__wrapper");
  porjectsWrapper.children[0].style.display = "none";
  porjectsWrapper.children[1].style.display = "block";
  document.querySelector(".projects__details-about-img img").setAttribute("src", data.main_photo);
  const projectsDetailsImg = document.querySelector(".projects__details-about-img-list");
  projectsDetailsImg.innerHTML = "";
  createProjectsDetailsImgListItem(data.main_photo, projectsDetailsImg, 'projects__detail-about-img-list-active');
  data.housephoto_set.map((photo) => {
    createProjectsDetailsImgListItem(photo.photo, projectsDetailsImg);
  });
  document.querySelector(".projects__details-title").textContent = `Проект "${data.name}"`;
  const projectDetailsOptions = document.querySelectorAll(".projects__details-options-list li");
  projectDetailsOptions[0].children[1].textContent = data.material.material;
  projectDetailsOptions[1].children[1].textContent = data.facade;
  projectDetailsOptions[2].children[1].innerHTML = `${data.square} м<sup>2</sup>`;
  projectDetailsOptions[3].children[1].textContent = `${data.room} ${data.bathroom} ${data.floor}`;
  document.querySelector(".projects__details-price-value").textContent = data.cost_of_basic_equipment + " ₽";
  document.querySelector(".projects__details-scheme-img img").setAttribute("src", data.houseplanphoto_set[0].photo);
}

function createProjectsDetailsImgListItem(src, parentElement, className) {
  const li = document.createElement("li")
  li.classList.add(className);
  li.innerHTML = `<img src="${src}">`;
  parentElement.append(li);

  li.addEventListener("click", (e) => {
    document.querySelector(".projects__details-about-img img").setAttribute("src", e.target.src);

  })
}

function requestDetails(url) {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      renderDetails(data);
    })
    .catch((error) => {
      console.log(error);
    });
}
