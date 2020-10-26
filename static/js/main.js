
$(document).ready(function() {
    $('.page__main__slider').slick({
        //slide: 'div',
        slidesToScroll: 1,
        slidesToShow: 1,
        mobileFirst: true,
        dots: true,
        infinite: true,
        cssEase: 'ease',
        swipe: true,
        arrows: true,
        autoplay: true,
        autoplayspeed: 1000,
        lazyLoad: 'ondemand',
        prevArrow: $('.prev'),
        nextArrow: $('.next'),
    });

    $(".comments__cards").slick({
        slidesToScroll: 1,
        slidesToShow: 1,
        // mobileFirst: true,
        infinite: true,
        cssEase: 'ease',
        swipe: true,
        arrows: true,
        autoplay: false,
        autoplayspeed: 1000,
        lazyLoad: 'ondemand',
        prevArrow: $('#comments_left'),
        nextArrow: $('#comments_right'),
    });

});





