from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
path("", views.PollList.as_view(), name="list"),
    path("<int:pk>/", views.PollDetail.as_view(), name="detail"),
    path("<int:pk>/results/", views.Results.as_view(), name="results"),
    path("<int:pk>/vote/", views.Vote.as_view(), name="vote"),
    path("choices/<int:choice_id>/", views.ChoiceDetail.as_view(), name="choice_detail"),
    ]