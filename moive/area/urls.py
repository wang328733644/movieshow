from django.conf.urls import url

from area import views

urlpatterns = [
    url(r'^area/(\d+)/', views.area_list)
]
