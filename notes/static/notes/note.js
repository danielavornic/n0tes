tinymce.init({
    selector: 'textarea',
    height: 500,
    menubar: false,
    mobile: {
        theme: 'mobile'
    },
    plugins: [
        'advlist autoresize autosave autolink lists link charmap',
        ' visualblocks emoticons',
        'media table paste code help wordcount'
    ],
    toolbar: 'undo redo | formatselect | bold italic underline |' + 
    'alignleft aligncenter alignright alignjustify | ' + 
    ' numlist bullist | link charmap emoticons',
});


$('document').ready(function() {
    var check = $('#id_important');
    var title= $('#id_title');
    title.parent().css({
        'display': 'inline-block',
        'width': 'calc(100% - 41px)'
    })
    check.parent().css({
        'display': 'inline-block',
        'position': 'relative',
        'verticalAlign': '-11px'
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