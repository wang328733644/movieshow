
    $(".form1").submit(function (envent) {
        envent.preventDefault();
        var name = $('#Username').val();
        var password =$('#Password').val();
        $.ajax({
            'url':'/index/login/',
            'type':'POST',
            'dataType':'json',
            'data':{'name':name, 'password':password},
            success:function (data) {
                if(data.code=='200'){
                    $('#log1').text(data.name);
                    $('#log2').show();
                    $('.modal-content').hide()
                }
            },
            error:function (data) {
                alert('登录失败')
            }

    });
    return false;
});



