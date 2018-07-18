function logout() {

    $.ajax({
        url:'/index/logout/',
        type:'POST',
        dataType:'json',
        success:function (data) {
            if(data.code=='200'){
                location.href='/index/index/'
            }
        },
        error:function (data) {
            alert('退出失败')
        }
    })
}

