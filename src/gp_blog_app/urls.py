from django.urls import path
from .views import home_api, post_list_create_api

app_name = "gp_blog_app"

urlpatterns = [
    path("", home_api, name="home"),
    path("list-create-api/", post_list_create_api, name="list-create")
]