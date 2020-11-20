
from django.contrib import admin
from django.urls import path,include
from uservotingsystem.views import PostListView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', PostListView.as_view(),name='list')
]
