from django.urls import path, include
from . import views

app_name = 'music'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>', views.detail, name='detail'),
    path('login', views.loginpage.as_view(), name='login'),
    path('signup', views.signup.as_view(), name='signup'),
    path('album/add', views.addalbum.as_view(), name='addalbum'),
    path('album/update/<int:pk>', views.updatealbum.as_view(), name='updatealbum'),
    path('album/delete/<int:pk>', views.deletealbum.as_view(), name='deletealbum'),
    path('logout',views.signout,name='signout'),
    path('song/add/<int:pk>',views.addsong.as_view(), name='addsong'),
    path('song/update/<int:pk>',views.updatesong.as_view(),name='updatesong'),
    path('song/delete/<int:pk>',views.deletesong.as_view(),name='deletesong'),
    path('home/',views.mainhome,name='mainhome'),
    path('search/',views.search,name='search'),
    path('search1/',views.search1,name='search1'),
]
