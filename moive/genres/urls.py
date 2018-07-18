from django.conf.urls import url
from genres import views

urlpatterns = [
    url(r'^classify/(?P<action>\d+)/', views.dump)
]