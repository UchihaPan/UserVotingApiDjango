from django.contrib import admin
from django.urls import path, include
from uservotingsystem.views import PostListView, VoteListView, PostDestroy

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='list'),
    path('posts/<int:pk>/', PostDestroy.as_view(), name='delete_posts'),

    path('vote/<int:pk>/', VoteListView.as_view(), name='vote'),
    path('api-auth/', include('rest_framework.urls')),

]
