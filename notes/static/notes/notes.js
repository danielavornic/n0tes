var $grid = $('#notes ul').isotope({
    itemSelector: '.note',
    layoutMode: 'masonry',
    percentPosition: true,
    masonry: {
      columnWidth: '.note',
      gutter: '.note-gap',
      horizontalOrder: true
    }
});

$('.note-text').each(function(){
    $(this).html($(this).html().replace(/&amp;nbsp;/gi,''));
});

const touch = matchMedia('(hover: none)').matches;
const originalHeight = $(window).height();
$(window).resize(function() {
    if (touch) {
        if ($(window).height() < originalHeight){
            $('#menu').hide();
        } else {
            $('#menu').show();
        }
    }
});