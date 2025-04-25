from django.urls import path
from . import views

urlpatterns = [
    path("", views.index , name="index"),
    path("wait/", views.wait, name="wait"),
    path("wait2/", views.wait2, name="wait2"),
    path("scroll/", views.scroll, name="scroll"),
    path("repeate/", views.repeate, name="repeate"),
    path("blend/", views.blend, name="blend"),
    path("move/", views.move, name="move"),
    path("ending/", views.ending, name="ending")
]