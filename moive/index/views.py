import random
import time
from datetime import datetime, timedelta

from django.contrib.auth.hashers import check_password, make_password
from django.shortcuts import render
from django.http.response import HttpResponseRedirect, HttpResponse, JsonResponse
from django.urls import reverse

from index.models import Movie, MovieTypes, User, UserTicket, MovieAreas, News, Event

import pymongo


# Create your views here.
# 连接mongdb的函数
def mongdb():
    client = pymongo.MongoClient('mongodb://47.106.96.225:27017')
    db = client.doumovie

    return db


# 获取汉字首字母
def single_get_first(str):
    str1 = str.encode('gbk')
    try:
        ord(str1)
        return str1
    except:
        asc = str1[0] * 256 + str1[1] - 65536
        if asc >= -20319 and asc <= -20284:
            return 'a'
        if asc >= -20283 and asc <= -19776:
            return 'b'
        if asc >= -19775 and asc <= -19219:
            return 'c'
        if asc >= -19218 and asc <= -18711:
            return 'd'
        if asc >= -18710 and asc <= -18527:
            return 'e'
        if asc >= -18526 and asc <= -18240:
            return 'f'
        if asc >= -18239 and asc <= -17923:
            return 'g'
        if asc >= -17922 and asc <= -17418:
            return 'h'
        if asc >= -17417 and asc <= -16475:
            return 'j'
        if asc >= -16474 and asc <= -16213:
            return 'k'
        if asc >= -16212 and asc <= -15641:
            return 'l'
        if asc >= -15640 and asc <= -15166:
            return 'm'
        if asc >= -15165 and asc <= -14923:
            return 'n'
        if asc >= -14922 and asc <= -14915:
            return 'o'
        if asc >= -14914 and asc <= -14631:
            return 'p'
        if asc >= -14630 and asc <= -14150:
            return 'q'
        if asc >= -14149 and asc <= -14091:
            return 'r'
        if asc >= -14090 and asc <= -13119:
            return 's'
        if asc >= -13118 and asc <= -12839:
            return 't'
        if asc >= -12838 and asc <= -12557:
            return 'w'
        if asc >= -12556 and asc <= -11848:
            return 'x'
        if asc >= -11847 and asc <= -11056:
            return 'y'
        if asc >= -11055 and asc <= -10247:
            return 'z'
        return str[0]


# 将mongodb数据库中的movie数据导入到mysql中
def save_movie(request):
    if request.method == 'GET':
        db = mongdb()
        score = db.score
        tables = score.find()
        for movie in tables:
            name = movie['name'].split(' ')[0].split('：')[0]
            des = movie['des']
            if len(des) < 60:
                des = des
            else:
                des = des[:60] + '...'
            actors = movie['actor'].split(' ')[0]
            letter = single_get_first(name)
            area = movie['area'].split(' ')[1]
            if not Movie.objects.filter(name=name):
                Movie.objects.create(
                    name=name,
                    img=movie['img'],
                    des=des,
                    actors=actors,
                    year=movie['year'].split('(')[0],
                    score=movie['score'],
                    url=movie['url'],
                    status=1,
                    letter=letter,
                    type_id=MovieTypes.objects.get(type_name=movie['types']).id,
                    area_id=MovieAreas.objects.get(area_name=area).id
                )

        return HttpResponse('keke')


# 保存电影区域
def save_area(request):
    if request.method == 'GET':
        db = mongdb()
        score = db.score
        tables = score.find()
        areas = []
        for table in tables:
            area = table['area'].split(' ')[1]
            areas.append(area)
        areas = list(set(areas))

        for area in areas:
            if not MovieAreas.objects.filter(area_name=area):
                MovieAreas.objects.create(
                    area_name=area
                )

        return HttpResponse('ok')


# 保存电影类型
def save_type(request):
    if request.method == 'GET':
        db = mongdb()
        score = db.score
        tables = score.find()
        types = []
        for table in tables:
            type = table['types']
            types.append(type)
        types = list(set(types))
        for type in types:
            if not MovieTypes.objects.filter(type_name=type):
                MovieTypes.objects.create(
                    type_name=type
                )

        return HttpResponse('ok')


def save_news(request):
    if request.method == 'GET':
        db = mongdb()
        news_db = db.news
        tables = news_db.find()
        for table in tables:
            title = table['title']
            if not News.objects.filter(title=title):
                News.objects.create(
                    img=table['img'],
                    title=table['title'],
                    short_content=table['short_content'],
                    long_content=table['long_content'],
                    time=table['time'],
                    view=table['view']
                )
        return HttpResponse('OK')


# 导航栏的方法
def home(request):
    if request.method == 'GET':

        # 所有电影类型
        types = MovieTypes.objects.all()
        areas = MovieAreas.objects.all()
        movies = Movie.objects.filter(type_id=5)[0:8]

        # 经典电影
        all_movies = Movie.objects.all()[0:40]

        # 高评分的电影
        top_score_movies = Movie.objects.order_by('-score')

        # 最受欢迎的电影
        n = random.randrange(500)
        m = random.randrange(300)
        popular_movies = Movie.objects.filter(type_id=3)[m:m+3]
        many_populars = Movie.objects.all()[n:]

        # 查看高收视的电影
        top_events = Event.objects.order_by('-click_counts')[0:12]
        top_view_movies = []
        for top_event in top_events:
            top_view_movie = top_event.id
            top_view_movies.append(top_view_movie)

        # 新加电影，是对年份最新的
        new_movies = Movie.objects.filter(year='2018')[0:12]

        data = {
            'types': types,
            'areas': areas,
            'movies': movies,
            'allmovies': all_movies,
            'top_score_movies': top_score_movies,
            'top_view_movies': top_view_movies,
            'popular_movies': popular_movies,
            'many_populars': many_populars,
            'new_movies': new_movies,

        }
        return render(request, 'index.html', data)


# 注册
def register(request):
    if request.method == 'POST':
        data = {
            'msg': '请求成功',
            'code': '200'
        }
        name = request.POST.get('name')
        password = request.POST.get('password')
        password = make_password(password)
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        User.objects.create(
            name=name,
            password=password,
            email=email,
            tel=phone,
        )
        return JsonResponse(data)


# 登录
def login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        if all((phone, password)):
            if User.objects.filter(tel=phone).exists():
                user = User.objects.get(tel=phone)
                if check_password(password, user.password):
                    s = 'qwertyuiiiopasdfghjklzxcvbnm1234567890'
                    ticket = ''
                    for _ in range(15):
                        ticket += random.choice(s)
                    now_time = int(time.time())
                    ticket = 'TK' + ticket + str(now_time)
                    response = HttpResponseRedirect(reverse('movie:index'))
                    out_time = datetime.now() + timedelta(days=1)
                    response.set_cookie('ticket', ticket, expires=out_time)
                    UserTicket.objects.create(
                        user_id=user.id,
                        ticket=ticket,
                        out_time=out_time
                    )

                    return response


# 注销
def logout(request):
    if request.method == 'POST':
        data = {
            'msg': '请求成功',
            'code': '200'
        }
        response = HttpResponseRedirect('/index/index/')
        response.delete_cookie('ticket')
        ticket = request.COOKIES.get('ticket')
        UserTicket.objects.filter(ticket=ticket).delete()

        return JsonResponse(data)
