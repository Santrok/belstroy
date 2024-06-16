const urls = [`${localStorage.getItem("url")}api/material/`, `${localStorage.getItem("url")}api/improvement/`];
function requestProjects() {
  const arrFetchData = urls.map((url) => fetch(url).then((response) => response.json()));
  
  Promise.allSettled(arrFetchData)
    .then((data) => {
      for (let i of data) {
        renderProjects(i.value);
      }
    })
    .catch((error) => {
      console.log(error);
    });
}

requestProjects()

function backToProjectsFunc() {
  const porjectsWrapper = document.querySelector(".projects__wrapper");
  const projectLandscapingWrapper = document.querySelector('.projects__landscaping-wrapper')
  projectLandscapingWrapper.children[1].style.display = "none";
  porjectsWrapper.children[1].style.display = "none";
  porjectsWrapper.children[0].style.display = "block";
  projectLandscapingWrapper.children[0].style.display = "block";
  requestProjects()
}

function renderProjects(arr) {
  const backToProjects = document.querySelectorAll(".projects__details-block-back");
  backToProjects.forEach((item) => {
    item.addEventListener("click", backToProjectsFunc);
  });
  if(arr[0].material) {
    document.querySelector('.projects__list-wrapper').innerHTML = ''
    renderHouses(arr, '.projects__list-wrapper');
  }else {
    document.querySelector('.projects__landscaping-list-wrapper').innerHTML = ''
    renderLandscaping(arr, '.projects__landscaping-list-wrapper');
  }
}

function renderHouses(arr,className) {
  const projectListWrapper = document.querySelector(className);
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
                                <div class="projects__list-item-link projects__houses">
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
    projectsDetails('api/house_detail/', '.projects__houses')
  }
}

function renderLandscaping(arr, className) {
  const projectListWrapper = document.querySelector(className);
  const ul = document.createElement("ul");
  ul.classList.add("projects__list");
  for (let i of arr) {
    ul.innerHTML += `
    <li class="projects__list-item-wrapper">
      <article class="projects__list-item" data-id="${i.id}">
          <div class="projects__list-item-link porjects__landscaping">
              <div class="projects__list-item-img">
                  <img src="${i.main_photo}" alt="">
              </div>
              <footer class="projects__list-item-title-wrap">
                  <h3 class="projects__list-item-title">
                      ${i.title}
                  </h3>
              </footer>
          </div>
          <header class="projects__list-item-about-wrapper">
          <p class="projects__list-item-about-wrapper-description">
            ${i.description}
          </p>
          </header>
      </article>
  </li>`;
  }
    projectListWrapper.append(ul);
    projectsDetails('api/improvement_detail/', '.porjects__landscaping')
}

function projectsDetails(url, className) {
  if (typeof className !== "string" && typeof url !== "string") return console.log("Error, check your arguments");    
  const buildingListItem = document.querySelectorAll(className);
  buildingListItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      requestDetails(`${localStorage.getItem("url")}${url}${e.currentTarget.parentElement.dataset.id}/`);
    });
  });
}

function renderDetails(data, landscaping = false) {
  if(landscaping) {
    const porjectsWrapper = document.querySelector(".projects__landscaping-wrapper");
    porjectsWrapper.children[0].style.display = "none";
    porjectsWrapper.children[1].style.display = "block";
    document.querySelector(".projects__landscaping-wrapper .projects__details-about-img img").setAttribute("src", data.main_photo);
    const projectsDetailsImg = document.querySelector(".projects__landscaping-wrapper .projects__details-about-img-list");
    projectsDetailsImg.innerHTML = "";
    createProjectsDetailsImgListItem(data.main_photo, projectsDetailsImg, "projects__detail-about-img-list-active");
    data.improvementphoto_set.map((photo) => {
      createProjectsDetailsImgListItem(photo.photo, projectsDetailsImg, 'projects__detail-about-img-list-item');
    });
    document.querySelector(".projects__landscaping-wrapper .projects__details-title").textContent = `Проект "${data.title}"`;
  }else {
    const porjectsWrapper = document.querySelector(".projects__wrapper");
    porjectsWrapper.children[0].style.display = "none";
    porjectsWrapper.children[1].style.display = "block";
    document.querySelector(".projects__details-about-img img").setAttribute("src", data.main_photo);
    const projectsDetailsImg = document.querySelector(".projects__details-about-img-list");
    projectsDetailsImg.innerHTML = "";
    createProjectsDetailsImgListItem(data.main_photo, projectsDetailsImg, "projects__detail-about-img-list-active");
    data.housephoto_set.map((photo) => {
      createProjectsDetailsImgListItem(photo.photo, projectsDetailsImg, 'projects__detail-about-img-list-item');
    });
    document.querySelector(".projects__details-title").textContent = `Проект "${data.name}"`;
    const projectDetailsOptions = document.querySelectorAll(".projects__details-options-list li");
    const dataOptions = [`${data.material.material}`, `${data.facade}`, `${data.square} м<sup>2</sup>`, `${data.room} ${data.bathroom} ${data.floor}`]
    for(let i = 0; i <= 3; i++) {
      projectDetailsOptions[i].children[1].innerHTML = dataOptions[i]
    }
    document.querySelector(".projects__details-price-value").textContent = data.cost_of_basic_equipment + " ₽";
    document.querySelector(".projects__details-scheme-img img").setAttribute("src", data.houseplanphoto_set[0]?.photo ? data.houseplanphoto_set[0].photo : "");
  }
}

function createProjectsDetailsImgListItem(src, parentElement, className) {
  const li = document.createElement("li");
  li.classList.add(className);
  li.innerHTML = `<img src="${src}">`;
  parentElement.append(li);

  li.addEventListener("click", (e) => {
    document.querySelector(".projects__details-about-img img").setAttribute("src", e.target.src);
  });
}

function requestDetails(url) {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      if (url.split('/').includes('improvement_detail')) {
        renderDetails(data, true)
      }else {
        renderDetails(data);
      }
    })
    .catch((error) => {
      console.log(error);
    });
}
