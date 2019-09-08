from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.index),
    path('api/', views.API_URL),
    url(r'^(?P<short_link>\w+)/$', views.redirect_link),
]
