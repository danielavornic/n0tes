tinymce.init({
    selector: '#id_text',
    placeholder: 'Start typing…',
    menubar: false,
    mobile: {
        theme: 'mobile'
    },
    plugins: [
        'advlist autoresize autosave autolink lists link charmap',
        ' visualblocks emoticons',
        'media table paste code wordcount'
    ],
    toolbar: 'undo redo | formatselect | bold italic underline |' + 
    'alignleft aligncenter alignright alignjustify | ' + 
    ' numlist bullist | link charmap emoticons',
});

$('document').ready(function() {
    $('#id_title').height($('#id_title').prop('scrollHeight'));
    $('#id_title').on('input', function () {
        $(this).height('auto');
        $(this).height($(this).prop('scrollHeight'));
    });

    var check = $('#id_important');
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
    check.on('change', bookmark);
})