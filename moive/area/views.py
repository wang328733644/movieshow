from random import randrange

from django.core.paginator import Paginator
from django.shortcuts import render


# Create your views here.
from index.models import MovieAreas, Movie, MovieTypes


def area_list(request, action):
    if request.method == 'GET':
        # 获取随机数
        num = randrange(1000)
        # body wrapper start图片
        footer_movies = Movie.objects.all()[num: num + 20]

        movies = Movie.objects.filter(area_id=action)
        # 类型
        types = MovieTypes.objects.all()
        # 分页每页显示数
        paginator = Paginator(movies, 30)
        # 获得电影分类名
        area_name = MovieAreas.objects.get(id=action).area_name
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
            'area_name': area_name,
            'footer_movies': footer_movies
        }
        return render(request, 'area.html', data)