from django.urls import path
from.import views

app_name = 'post'

urlpatterns = [
    path('profile/<str:username>/', views.profile ,name ='profile'),
    path('posts/<int:post_id>/', views.post_detail ,name ='post_detail'),
    
    path('', views.index ,name ='index'),
    path('group/<slug:slug>/',views.group_posts ,name ='group_posts'),
]