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