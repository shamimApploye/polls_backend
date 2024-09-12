from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
path("", views.poll_list, name="list"),
    path("<int:pk>/", views.poll_detail, name="detail"),
    path("<int:pk>/results/", views.results, name="results"),
    path("<int:pk>/vote/", views.vote, name="vote"),
    path("<int:pk>/choices/", views.choices_list, name="choices_list"),
    path("choices/<int:choice_id>/", views.choice_detail, name="choice_detail"),
    ]