$('document').ready(function() {
    $('body').show();

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

    if ($(window).width() < 576) {
        var height = $(window).height();
        $(window).on('resize', function() {
            if ($(window).height() < height) {
                $('#menu').hide();
            } else {
                $('#menu').show();
            }
        })
    }
})