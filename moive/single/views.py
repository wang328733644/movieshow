from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse

from index.models import Movie, MovieTypes, Event, Comments, MovieAreas
from random import randrange


# 点击一部电影的页面渲染
def movie_single(request, movie_id):
    if request.method == 'GET':
        try:
            count = Event.objects.filter(movie_id=movie_id)[0]
            # 请求一次页面次数加一
            if count:
                counts = count.click_counts + 1
                # 更新数据库
                count.click_counts = counts
                count.save()
        except:
            Event.objects.create(
                movie_id=movie_id,
                click_counts=1
            )

        areas = MovieAreas.objects.all()

        types = MovieTypes.objects.all()

        # 得到点击的图片
        one_movie = Movie.objects.get(id=movie_id)

        # 获取随机数
        num = randrange(1000)

        # body wrapper start图片
        footer_movies = Movie.objects.all()[num: num + 20]

        # up_newt图片
        up_next_movies = Movie.objects.all()[num: num + 8]

        # 展示评论
        movie_comments = Comments.objects.filter(mov_id=movie_id)

        data = {
            'types': types,
            'one_movie': one_movie,
            'up_next_movies': up_next_movies,
            'footer_movies': footer_movies,
            'movie_comments': movie_comments,
            'areas': areas
        }

        return render(request, 'single.html', data)


# 用户对某部电影添加评论的接口
def commnent(request):
    if request.method == 'POST':
        data = {
            'code': 200,
            'msg': '成功',
        }
        user = request.user
        if user and user.id:
            movie_comment = request.POST.get('movie_comment')
            movie_id = request.POST.get('movie_id')
            Comments.objects.create(
                user_id=user.id,
                mov_id=movie_id,
                content=movie_comment
            )
            data['user_name'] = user.name
            data['mov_comment'] = movie_comment
            return JsonResponse(data)
