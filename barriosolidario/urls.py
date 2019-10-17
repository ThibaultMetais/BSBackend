from django.urls import path
from . import views
urlpatterns = [
    path('api/user/', views.UserListCreate.as_view() ),
    path('api/news/', views.NewsPostListCreate.as_view() ),
    path('api/help/', views.HelpPostListCreate.as_view() ),
]
