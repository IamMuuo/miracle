from django.urls import path

from mir_handler.views import Ping

urlpatterns = [
    # ping
    path("", Ping.as_view()),
]
