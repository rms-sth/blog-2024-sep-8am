from django.urls import path
from blog_app import views

urlpatterns = [
    path("", views.post_list, name="post-list"),
]