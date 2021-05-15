$('.note-text').each(function(){
    $(this).html($(this).html().replace(/&amp;nbsp;/gi,''));
});

var originalHeight = $(window).height();
$(window).resize(function() {
    if ($(window).height() < originalSize){
        $('#menu').hide();
    } else {
        $('#menu').show();
    }
});