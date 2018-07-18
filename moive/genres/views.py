from random import randrange

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from index.models import Movie, MovieTypes, MovieAreas


# action页面的方法
def dump(request, action):

    if request.method == 'GET':

        # 获取随机数
        num = randrange(1000)
        # body wrapper start图片
        footer_movies = Movie.objects.all()[num: num + 20]

        movies = Movie.objects.filter(type_id=action)
        # 类型
        types = MovieTypes.objects.all()
        # 获得电影分类名
        type_name = MovieTypes.objects.get(id=action).type_name
        # 分页每页显示数
        paginator = Paginator(movies, 30)
        # 获得url的后缀id
        page_id = request.GET.get('page_id', 1)
        # 表示第几页
        pages = paginator.page(int(page_id))
        areas = MovieAreas.objects.all()
        data = {
            'pages': pages,
            'action': action,
            'types': types,
            'areas': areas,
            'type_name': type_name,
            'footer_movies': footer_movies
        }
        return render(request, 'genres.html', data)
