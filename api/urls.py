from django.urls import path
from . import views

urlpatterns = [
    path('books/', views.BookCreateApiView.as_view())
    # todo Below paths are for function based view
    # path('books/', views.book_List),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.author_list),
    # path('author/<int:pk>/', views.author_detail)
]