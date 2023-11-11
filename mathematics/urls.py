from django.urls import path
from . import views

urlpatterns = [
    path("", views.hello),
    path("hello/", views.hello),
    path("hello/<name>", views.hello),
    path("mathematics/<calc>/<int:a>/<int:b>", views.calculate),
]