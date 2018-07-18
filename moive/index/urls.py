from django.conf.urls import url
from index import views

urlpatterns = [
    url(r'^index/', views.home, name='index'),
    url(r'^save/', views.save_movie),
    url(r'^savetype/', views.save_type),
    url(r'^savearea/', views.save_area),
    url(r'^savenews/', views.save_news),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
]
