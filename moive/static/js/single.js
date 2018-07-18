


$("#forms_comment").submit(function (event) {
    event.preventDefault();
    movie_comment = $('#movie_comment').val();
    movie_id = $('#movie_id').html();

    $.ajax({
        url: '/single/comment/',
        type: 'POST',
        data: {'movie_comment': movie_comment,'movie_id':movie_id},
        dataType: 'json',
        success: function (msg) {
            alert('ok');
            if (msg.code == '200'){
                var comment_list = '<div class="media">';
                comment_list += '<h5>'+ msg.user_name+'</h5>';
                comment_list += '<div class="media-left">';
                comment_list += '<a href="#"> <img src="/static/images/user.jpg" title="One movies" alt=" "/> </a>';
                comment_list += '</div>';
                comment_list += '<div class="media-body">';
                comment_list += ' <p>'+ msg.mov_comment+'</p>';
                comment_list += ' <span>View all posts by :<a href="#"> Admin </a></span>';
                comment_list += '</div>';
                comment_list += '</div>';
                $('#new_comment').prepend(comment_list);

            }
        },
        error: function (msg) {
            alert('请先登录');
        }
    });
});



