from django.urls import path

from . import views


urlpatterns = [
    path("chat/<int:blog_id>/", views.blog_chat, name="blog_chat"),
]