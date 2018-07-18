from django.conf.urls import url

from  single import views
urlpatterns = [
    url(r'^single/(\d+)/',views.movie_single,name='movie_single'),
    url(r'^comment/', views.commnent)
]