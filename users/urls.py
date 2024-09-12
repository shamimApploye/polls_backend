from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.UsersList.as_view() ),
    path('<int:id>/', views.UsersDetail.as_view() ),
]
