from django.urls import path
from .views import BlogList, BlogCreateApi


app_name = "gp_blog_app"

urlpatterns = [
    # path("", home_api, name="home"),
    path("list/", BlogList.as_view(), name="list"),
    path("create/", BlogCreateApi.as_view(), name="create")
]