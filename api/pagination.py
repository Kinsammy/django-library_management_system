from rest_framework.pagination import PageNumberPagination


class DefaultPageNumberPaginaton(PageNumberPagination):
    page_size = 10
