from django.urls import path

from boards.views import index

urlpatterns = [
    path("", index, name="index"),
]
