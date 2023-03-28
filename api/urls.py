from django.urls import path, include
from . import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('authors', views.AuthorViewSet)
router.register('books', views.BookViewSet)

urlpatterns = [
    # todo Model View set
    path('', include(router.urls)),
    # todo class based paths or view
    # todo author paths
    # path('books/', views.BookListApiView.as_view()),
    # # path('books/create/', views.CreateBookApiView.as_view()),
    # path('books/<int:pk>/', views.BookDetailApiView.as_view(), name='detail'),

    # todo author paths
    path('authors/<int:pk>/', views.author_detail, name='author-detail'),
    # path('authors/', views.AuthorListApiView.as_view()),
    # path('authors/create/', views.CreateAuthorApiView.as_view()),
    # path('author/<int:pk>/', views.AuthorDetailApiView.as_view(), name='detail'),

    # todo Below paths are for function based view
    # path('books/', views.book_List),
    # path('book/<int:pk>/', views.book_detail),
    # path('authors/', views.author_list),
    # path('author/<int:pk>/', views.author_detail)
]
