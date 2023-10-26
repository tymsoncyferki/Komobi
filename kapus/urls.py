from django.urls import *
from . import views
from django.contrib import admin

app_name = 'kapus'
urlpatterns = [
    path('', views.index, name='index'),
    path("admin/", admin.site.urls),
    path('map/', views.map, name='map'),
    path('history/', views.history, name='history'),
    path('map/form/', views.issue_form, name='form'),
    path('issue/<int:issue_id>', views.issue, name='issue'),
    path('registration/login', views.login_view, name='login'),
    path('registration/logout', views.logout_view, name='logout'),
    path('registration/register', views.register_view, name='register'),
    path('account', views.account, name='account')
]
