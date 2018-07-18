from django.conf.urls import url

from list import views

urlpatterns = [
    url(r'^list/', views.list_html),
    url(r'^lista/(\w+)/', views.list_html_views),
    url(r'^search/', views.search)
]