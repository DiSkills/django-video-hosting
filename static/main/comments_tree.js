// comment tree
$(document).ready(function(){
    let slug = $('#create_comment').attr("action").split('/')[4];
    $('.reply').on('click', function(){
        let parentId = $(this).attr('data-id');
        $('#form-' + parentId).fadeToggle();
    });
    $('.submit-reply').on('click', function(e){
        e.preventDefault();
        let parentId = $(this).attr('data-submit-reply');
        let id = $(this).attr('data-id');
        let text = $('#form-' + id).find('textarea[name="comment-text"]').val();
        data = {
            parentId: parentId,
            text: text,
            id: id,
            slug: slug,
            csrfmiddlewaretoken: csrftoken
        };
        $.ajax({
            method: 'POST',
            data: data,
            url: "/comments/comments/child/create/",
            success: function(){
                location.reload();
            }
        });
    });
});
