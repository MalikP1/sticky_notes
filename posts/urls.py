from django.urls import path
from .views import get_all, get_one, create, update, delete


urlpatterns = [
    path('', get_all, name='posts'),
    path('<int:pk>', get_one, name='post'),
    path('new', create, name='create_post'),
    path('<int:pk>/edit', update, name='update_post'),
    path('<int:pk>/delete', delete, name='delete_post'),
]
