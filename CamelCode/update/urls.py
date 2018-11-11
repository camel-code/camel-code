from django.contrib import admin
from django.urls import path, re_path
from django.conf.urls import url
from . import views

app_name = 'update'

urlpatterns = [
    # /forum/
    path('', views.index, name='index'),

    # /forum/post_id/
    path('<int:update_id>/', views.updatePage, name='updatePage'),
]