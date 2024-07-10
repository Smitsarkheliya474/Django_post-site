from django.urls import path
from . import views

urlpatterns = [
    #path('home/', views.home, name='home'),
    path('home/', views.my_view, name='home'),
    path('home/newpost/', views.newpost, name='newpost'),
    path("home/newpost/insertdata/", views.insertdata, name="insertdata"),
    path('home/newpost/showall/', views.showall, name='showall'),
    path("home/showall/", views.showall, name="showall"),
    path("my_view/showall/", views.showall, name="showall"),
    path('search/', views.searchbar, name='search'),
]