from django.urls import path
from .views import BlogList, BlogCreateApi, BlogDetail, BlogUpdate, BlogDelete, CreateCommentAPI, CreateLikeAPI


app_name = "gp_blog_app"

urlpatterns = [
    path("list/", BlogList.as_view(), name="list"),
    path("create/", BlogCreateApi.as_view(), name="create"),
    path("detail/<str:slug>/", BlogDetail.as_view(), name="detail"),
    path("update/<str:slug>/", BlogUpdate.as_view(), name="update"),
    path("delete/<str:slug>/", BlogDelete.as_view(), name="delete"),
    path("comment/<str:slug>/", CreateCommentAPI.as_view(), name="comment"),
    path("like/<str:slug>/", CreateLikeAPI.as_view(), name="like"),
]