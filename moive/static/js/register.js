
    $(".form2").submit(function (envent) {
        alert('asd')
        envent.preventDefault();
        var name = $('#username').val();
        var password = $('#password').val();
        var email = $('#email').val();
        var phone = $('#phone').val();
        alert(name);
        alert('abc');
        $.ajax({
            url:'/index/register/',
            type:'POST',
            dataType:'json',
            data:{'name':name, 'password':password,'email':email,'phone':phone},
            success:function (data) {
                if(data.code=='200'){
                    alert('cde');
                    location.href='/index/index/'
                }
            },
            error:function (data) {
                alert('注册失败')
            }
        })
    });


