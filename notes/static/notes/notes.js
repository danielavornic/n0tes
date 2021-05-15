$('.note-text').each(function(){
    $(this).html($(this).html().replace(/&amp;nbsp;/gi,''));
});

var originalSize = $(window).width() + $(window).height();
$(window).resize(function() {
    if ($(window).width() + $(window).height() != originalSize){
        $('#menu').hide();
    } else {
        $('#menu').show();
    }
});