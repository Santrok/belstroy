$(document).ready(function() {
    
    const imgArr = [
        './img/photo_1.jpg',
        './img/photo_2.jpg',
        './img/photo_3.jpg',
        './img/photo_4.jpg',
        './img/photo_5.jpg',
        './img/photo_6.jpg',
        './img/photo_7.jpg',
        './img/photo_8.jpg',
        './img/photo_9.jpg',
        './img/photo_10.jpg',
        './img/photo_11.jpg',
    ]
    
    
    function setSliderItems(data) {
        const sliderInner = $('.about__slider');
        for (let i of data) {
            const div = document.createElement('div');
            div.classList.add('about__slider-item');
            div.innerHTML = `<img src="${i}" alt="slider${i}">`
            sliderInner.append(div)
        }
        
        $('.about__slider').slick({
            slidesToShow: 1,
            slidesToScroll: 1,
            autoplay: true,
            autoplaySpeed: 2000,
            infinite: true,
            arrows: false,
            dots: false,
            })
    }
    
    setSliderItems(imgArr)
})





