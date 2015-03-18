jQuery(function($){
    classMethod();
    initLightbox();
    initCarousel();
});


function classMethod () {
    var selector = $('#nav');
    activeItem = selector.find('.js-opener');
    activeItem.on('click', function(){
        $(this).next('ul').slideToggle("slow");
        $(this).parent().toggleClass("active");
        return false;
    });
    $(document).click(function(event) {
        if ($(event.target).closest(selector).length) return;
        if ($(window).width()<=767){
            $('#nav ul').slideUp("slow");
            $(selector).removeClass("active");
            event.stopPropagation();
        }

    });
}


//fancybox
function initLightbox () {
    if ($.fancybox) {
        if ($(window).width()<=480){
            $('.fancybox-thumb').unbind();
            $('.fancybox-thumb').on('click', function(){
                return false;
            });
        }else{
            $(".fancybox-thumb").fancybox({
                openEffect  : 'none',
                closeEffect : 'none',
                padding:0,
                closeBtn:false
            });
        }
    }

}


//Owl Callery
function initCarousel () {
    $('.owl-carousel').owlCarousel({
        items:1,
        responsiveRefreshRate:100,
        responsiveBaseElement:'.owl-carousel',
        autoHeight:true
    });
};