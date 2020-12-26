from django.urls import path

from boards.views import index, board

urlpatterns = [
    path("", index, name="index"),

    path("<slug:board_slug>/", board, name="board"),
]
