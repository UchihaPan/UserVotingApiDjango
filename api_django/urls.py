from django.contrib import admin
from django.urls import path, include
from uservotingsystem.views import PostListView, VoteListView, PostRetrieveUpdate

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(), name='list'),
    path('posts/<int:pk>/', PostRetrieveUpdate.as_view(), name='delete_posts'),

    path('<int:pk>/', VoteListView.as_view(), name='vote'),
    path('api-auth/', include('rest_framework.urls')),

]
