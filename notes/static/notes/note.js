$(document).ready(function() {
	var saveBtn = $('button#saveBtn');
    var saveBtnWidth = saveBtn.width();
    var titleEl = $('#id_title');
    var bookmarkEl = $('#id_important');
    var initBookmark = bookmarkEl.is(":checked");
    var initTitle = titleEl.val();
    var initText;

    function toggleSaveBtn() {
        var title = titleEl.val();
        var text = tinyMCE.activeEditor.getContent();
        var bookmark = bookmarkEl.is(":checked");
        if (title == initTitle && text == initText && bookmark == initBookmark) {
            saveBtn.html('Saved');
            saveBtn.removeClass('saveBtnChange');
        } else {
            saveBtn.html('Save!');
            saveBtn.addClass('saveBtnChange');
        }
        saveBtn.width(saveBtnWidth);
    }

    titleEl.focus();
    titleEl.on('input change', toggleSaveBtn);
    $("#id_important").on('change', toggleSaveBtn);

    tinymce.init({
        selector: '#id_text',
        placeholder: 'Start typing…',
        menubar: false,
        entity_encoding: 'raw',
        force_br_newlines : true,
        force_p_newlines : false,
        forced_root_block : '',
        plugins: [
            'advlist autoresize autosave autolink lists link charmap',
            ' visualblocks emoticons',
            'media table paste code'
        ],
        toolbar: 'undo redo | bold italic underline strikethrough |' + 
        'alignleft aligncenter alignright alignjustify | ' + 
        ' numlist bullist | link charmap emoticons',
        setup: function(editor) {
            editor.on('init', function() {
                initText = tinyMCE.activeEditor.getContent();
            });
            editor.on('input ExecCommand', toggleSaveBtn);
        },
        mobile: {
            plugins: 'advlist autoresize autosave autolink lists charmap',
            toolbar: 'undo redo | bold italic underline strikethrough | numlist bullist'
        },
        content_style: 'body { margin: 1rem 0; line-height: 1.5}' + 
        'ul, ol { padding-inline-start: 18px; margin: 0 auto}'
    });

    bookmarkEl.parent().css({
        'display': 'inline-block',
        'position': 'relative',
        'float': 'right',
        'margin-top': '4px'
    })

    //resize title textarea based on content length
    titleEl.height(titleEl.prop('scrollHeight'));
    titleEl.on('input', function () {
        $(this).height('auto');
        $(this).height($(this).prop('scrollHeight'));
    });

    function toggleBookmark() {
        var mark = $('#bookmark');
        if (mark) {
            mark.remove();
        }
        mark = $('<span class="iconify" id="bookmark"></span>');
        if (bookmarkEl.is(':checked')) {
            mark.attr('data-icon', 'mdi:bookmark');
        } else {
            mark.attr('data-icon', 'mdi:bookmark-outline');
        }
        bookmarkEl.parent().append(mark);
    }
    toggleBookmark();
    bookmarkEl.on('change', toggleBookmark);
})