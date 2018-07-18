from django.conf.urls import url

from news import views

urlpatterns = [
    url(r'movnews/', views.news_list),
    url(r'newSingle/(\d+)/', views.news_single)
]
