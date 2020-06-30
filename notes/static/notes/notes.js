$('.note-text').each(function(){
    $(this).html($(this).html().replace(/&amp;nbsp;/gi,''));
});

var menu = $('#menu');
var nav = $('nav').first();
var toggle = $('#toggle');

toggle.click(function() {
    if (menu.outerHeight() == 60) {
        menu.css('height', '100vh');
        nav.css('display', 'block');
        toggle.children().first().css('transform', 'rotate(-45deg) translate(-4px, 4px)');
        toggle.children().eq(1).css('opacity', '0');
        toggle.children().eq(2).css('transform', 'rotate(45deg) translate(-8px, -8px)');
    } else {
        menu.css('height', '60px');
        nav.css('display', 'none');
        toggle.children().removeAttr("style");
    }
})