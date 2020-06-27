tinymce.init({
    selector: 'textarea',
    height: 500,
    menubar: false,
    plugins: [
        'advlist autoresize autosave autolink lists checklist link charmap',
        ' visualblocks emoticons',
        'media table paste code help wordcount'
    ],
    toolbar: 'undo redo | formatselect | bold italic underline |' + 
    'alignleft aligncenter alignright alignjustify | ' + 
    ' numlist bullist checklist  | charmap emoticons | link table | ',
});


$('document').ready(function() {
    var check = $('#id_important');
    var title= $('#id_title');
    title.parent().css('display', 'inline-block')
    check.parent().css({
        'display': 'inline-block',
        'position': 'relative',
        'verticalAlign': '-8px'
    })

    function bookmark() {
        var mark = $('#bookmark');
        if (mark) {
            mark.remove();
        }
        mark = $('<span class="iconify" id="bookmark"></span>')
        if (check.is(':checked')) {
            mark.attr('data-icon', 'mdi:bookmark');
        } else {
            mark.attr('data-icon', 'mdi:bookmark-outline');
        }
        check.parent().append(mark);
    }
    bookmark();
    check.on('change', bookmark)

    setTimeout(function() {
        var titleWidth = $('#form').width() - $('#id_important').width() - 5;
        $('#id_title').parent().css('width', titleWidth + 'px')
    }, 900)

    title.parent().next().css({
        'box-shadow': '2px 5px 25px rgba(0, 0, 0, 0.12)',
    })

    var somethingChanged = false;
    $('#form').change(function() { 
        somethingChanged = true; 
    }); 
    $('#form').submit(function(e) {
        somethingChanged = false;
    });

    $(window).bind('beforeunload', function(e) {
        if (somethingChanged)
            return "You made some changes and it's not saved?";
        else 
            e = null; 
    });
})