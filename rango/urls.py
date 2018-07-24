from django.urls import path, re_path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    re_path(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.show_category, name='show_category'),
#    path('register/', views.register, name='register'),
#    path('login/', views.user_login, name='login' ),
    path('restricted/', views.restricted, name='restricted'),
#    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
]