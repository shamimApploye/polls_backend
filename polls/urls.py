from django.urls import path

from . import views

app_name = "polls"

urlpatterns = [
    # ex: /polls/
    path("", views.poll_list, name="list"),
    # ex: /polls/5/
    path("<pk>/", views.poll_detail, name="detail"),
    # ex: /polls/5/results/
    # path("<pk>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    # path("<pk>/vote/", views.vote, name="vote"),
]