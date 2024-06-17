const urls = [`${localStorage.getItem("url")}api/material/`, `${localStorage.getItem("url")}api/improvement/`];
/**
 * Request projects data from multiple URLs and render the projects on the webpage.
 *
 * @return {void} No return value
 */
async function  requestProjects() {
  const arrFetchData = urls.map((url) => fetch(url).then((response) => response.json()));
  await Promise.allSettled(arrFetchData)
    .then((data) => {
      for (let i of data) {
        renderProjects(i.value);
      }
    })
    .catch((error) => {
      new Error(error);
    });
}

requestProjects();

function backToProjectsFunc(event) {
  if(event.currentTarget.parentElement.parentElement.classList.contains('projects__wrapper') 
    || event.currentTarget.parentElement.parentElement.classList.contains('projects__landscaping-wrapper')) {
    event.currentTarget.parentElement.parentElement.children[1].style.display = "none";
    event.currentTarget.parentElement.parentElement.children[0].style.display = "block";
    requestProjects();
  }
}

/**
  * Renders project lists based on the type of projects provided in the array.
 * Sets up event listeners for elements to navigate back to project details.
 *
 * @param {Array} arr - An array of project objects. Each object in the array
 * should represent a project and may contain a 'material' property.
 */
const backToProjects = document.querySelectorAll(".projects__details-block-back");
backToProjects.forEach((item) => {
  item.addEventListener("click", e => backToProjectsFunc(e));
});
function renderProjects(arr) {
  if (arr[0].material) {
    document.querySelector(".projects__list-wrapper").innerHTML = "";
    renderHouses(arr, ".projects__list-wrapper");
  } else {
    document.querySelector(".projects__landscaping-list-wrapper").innerHTML = "";
    renderLandscaping(arr, ".projects__landscaping-list-wrapper");
  }
}

/**
 * Renders a list of houses with their details on the webpage.
 *
 * @param {Array} arr - An array of house objects containing information about each house.
 * @param {string} className - The CSS class name of the element to append the houses to.
 * @return {void} This function does not return a value, it renders the houses on the webpage.
 */

function renderHouses(arr, className) {
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
    projectsDetails("api/house_detail/", ".projects__houses");
  }
}

/**
 * Renders landscaping projects on the webpage.
 *
 * @param {Array} arr - Array of landscaping project objects
 * @param {String} className - CSS class name of the element to append the projects to
 * @return {void} No return value, renders the Landscape projects
 */
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
  projectsDetails("api/improvement_detail/", ".porjects__landscaping");
}

/**
 * Attaches a click event listener to each element with the specified class name and triggers a request for project details when clicked.
 *
 * @param {string} url - The base URL for the project details endpoint.
 * @param {string} className - The class name of the elements to attach the event listener to.
 * @return {void} This function does not return anything.
 */
function projectsDetails(url, className) {
  if (typeof className !== "string" && typeof url !== "string") return 
  const buildingListItem = document.querySelectorAll(className);
  buildingListItem.forEach((item) => {
    item.addEventListener("click", (e) => {
      requestDetails(`${localStorage.getItem("url")}${url}${e.currentTarget.parentElement.dataset.id}/`);
    });
  });
}

/**
 * Renders the details of a project on the page.
 *
 * @param {Object} data - The data object containing the project details.
 * @param {boolean} [isLandscaping=false] - Indicates whether the project is related to landscaping.
 * @return {void}
 */
function renderDetails(data, isLandscaping = false) {
  const projectsWrapper = document.querySelector(`.${isLandscaping ? "projects__landscaping-wrapper" : "projects__wrapper"}`);
  const projectWrapperClass = projectsWrapper.classList.value;
  projectsWrapper.children[0].style.display = "none";
  projectsWrapper.children[1].style.display = "block";
  const detailsAboutImgList = document.querySelector(`.${projectWrapperClass} .projects__details-about-img-list`);
  detailsAboutImgList.innerHTML = "";
  document.querySelector('.projects__details-description').innerText = data.description;
  document.querySelector(`.${projectWrapperClass} .projects__details-about-img img`).setAttribute("src", data.main_photo);
  createProjectsDetailsImgListItem(data.main_photo, detailsAboutImgList, "projects__detail-about-img-list-active");
  document.querySelector(`.${projectWrapperClass} .projects__details-title`).textContent = `Проект "${isLandscaping ? data.title : data.name}"`;
  if (isLandscaping) {
    data.improvementphoto_set.forEach((photo) => {
      createProjectsDetailsImgListItem(photo.photo, detailsAboutImgList, "projects__detail-about-img-list-item");
    });
  } else {
    data.housephoto_set.forEach((photo) => {
      createProjectsDetailsImgListItem(photo.photo, detailsAboutImgList, "projects__detail-about-img-list-item");
    });
    const dataOptions = [data.material.material, data.facade, `${data.square} m<sup>2</sup>`, `${data.room} ${data.bathroom} ${data.floor}`];
    for (let i = 0; i <= 3; i++) {
      document.querySelectorAll(".projects__details-options-list li")[i].children[1].innerHTML = dataOptions[i];
    }
    document.querySelector(".projects__details-price-value").textContent = data.cost_of_basic_equipment + " ₽";
    const housePlanPhoto = data.houseplanphoto_set[0]?.photo || "";
    document.querySelector(".projects__details-scheme-img img").setAttribute("src", housePlanPhoto);
    for(let i of data.housefacadephoto_set) {
      const li = document.createElement("li");
      li.innerHTML = `<img src="${i.photo}">`;
      document.querySelector('.projects__details-facade').append(li)
    }
  }
}

/**
 * Creates a new list item element with an image and appends it to the specified parent element.
 *
 * @param {string} src - The source URL for the image
 * @param {parentElement} parentElement - The parent element to append the new list item to
 * @param {string} className - The class name to add to the new list item
 * @return {void} No return value
 */
function createProjectsDetailsImgListItem(src, parentElement, className) {
  const li = document.createElement("li");
  li.classList.add(className);
  li.innerHTML = `<img src="${src}">`;
  parentElement.append(li);
  li.addEventListener("click", (e) => {
    document.querySelector(".projects__details-about-img img").setAttribute("src", e.target.src);
    Array.from(e.currentTarget.parentElement.children).forEach((item) => {
      item.classList.remove("projects__detail-about-img-list-active")
    })
    e.currentTarget.classList.add("projects__detail-about-img-list-active");
  });
}

/**
 * Request details from a specified URL, then render the details on the webpage.
 *
 * @param {string} url - The URL to fetch details from
 * @return {void} No return value
 */
function requestDetails(url) {
  fetch(url)
    .then((response) => response.json())
    .then((data) => {
      if (url.split("/").includes("improvement_detail")) {
        renderDetails(data, true);
      } else {
        renderDetails(data);
      }
    })
    .catch((error) => {
      new Error(error);
    });
}
