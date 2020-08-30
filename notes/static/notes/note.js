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
        'width': '100%',
        'margin-top': '28px'
    })
    check.parent().css({
        'display': 'inline-block',
        'position': 'relative',
        'float': 'right',
        'margin-top': '11px',
        'margin-right': '24px'
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
})