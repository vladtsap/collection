from django.urls import path
from django.views.decorators.cache import cache_page

from boards.views import index, board
from infomate import settings

urlpatterns = [
    path("", index, name="index"),

    path("<slug:board_slug>/", board, name="board"),
]
