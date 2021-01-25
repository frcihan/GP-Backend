from rest_framework.pagination import PageNumberPagination


class BlogPageNumberPagination(PageNumberPagination):
    page_size = 6
