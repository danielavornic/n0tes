$('.note-text').each(function(){
    $(this).html($(this).html().replace(/&amp;nbsp;/gi,''));
});

var isTouch = ('ontouchstart' in document.documentElement);
var originalHeight = $(window).height();
$(window).resize(function() {
    if (isTouch) {
        if ($(window).height() < originalSize){
            $('#menu').hide();
        } else {
            $('#menu').show();
        }
    }
});