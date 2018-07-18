from random import randrange

from django.core.paginator import Paginator
from django.shortcuts import render

from index.models import News, Movie, MovieAreas, MovieTypes


def news_list(request):
    if request.method == 'GET':
        news = News.objects.all()
        paginator = Paginator(news, 16)

        page_id = request.GET.get('page_id', 1)
        # 表示第几页
        pages = paginator.page(int(page_id))

        update_news = news[5:13]

        top_news = news[10:18]

        areas = MovieAreas.objects.all()

        types = MovieTypes.objects.all()

        data = {
            # 左1电影展示
            'pages1': pages[:8],
            # 左2电影展示
            'pages2': pages[8:],
            'pages': pages,
            'update_news': update_news,
            'top_news': top_news,
            'areas': areas,
            'types': types
        }

        return render(request, 'news.html', data)


def news_single(request, news_id):

    if request.method == 'GET':
        # 观看数加1
        news = News.objects.get(id=news_id)
        news.view += 1
        news.save()

        # 更新新闻信息加载
        n = randrange(50)
        update_news = News.objects.order_by('-time')[n: n+8]

        # 热点电影加载
        top_news = News.objects.order_by('-view')[n: n+4]

        # 相关新闻加载
        m = randrange(200)
        title = news.title[:4]
        related_news = News.objects.filter(title__contains=title)
        if len(related_news) >= 2:
            related_news = related_news
        else:
            related_news = News.objects.all()[m: m+2]
        related_news_left = related_news[0]
        related_news_right = related_news[1]

        # 下方电影加载
        footer_movies = Movie.objects.all().order_by('-year')[n: n+6]

        areas = MovieAreas.objects.all()

        types = MovieTypes.objects.all()

        data = {
            'news': news,
            'update_news': update_news,
            'top_news': top_news,
            'footer_movies': footer_movies,
            'related_news_left': related_news_left,
            'related_news_right': related_news_right,
            'areas': areas,
            'types': types
        }

        return render(request, 'news-single.html', data)
