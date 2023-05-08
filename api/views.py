from django.shortcuts import render, get_object_or_404

from .pagination import DefaultPageNumberPaginaton
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from book.models import *
from .permission import IsAdminOrReadOnly
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics
from django.core.mail import send_mail

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


# todo class base view
class BookListApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


# class CreateBookApiView(generics.CreateAPIView):
#     queryset = Book.objects.select_related('author').all()
#     serializer_class = BookSerializer


class BookDetailApiView(generics.RetrieveDestroyAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer


class AuthorListApiView(generics.ListAPIView, generics.CreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# class CreateAuthorApiView(generics.CreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer


class AuthorDetailApiView(generics.RetrieveDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


# Todo function for hyperlink
@api_view()
def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    serializer = AuthorSerializer(author)
    # todo -> This is a point where we use the send_mail()
    message = 'Never give up, keep it up'
    subject = 'Motivation from Samuel'
    send_mail(subject, message, 'fanusamuel@gmail.com',
              ['michaelolamilekanjohn0@gmail.com', 'akinsanyadaniel665@gmail.com'], fail_silently=False)
    return Response(serializer.data)


# Todo View Set ---> This will do all the Http Methods such as
# todo GET, POST, PUT, DELETE
class AuthorViewSet(ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPaginaton
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class BookViewSet(ModelViewSet):
    pagination_class = DefaultPageNumberPaginaton
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['title', 'genre']
    search_fields = ['language', 'price']


class BookInstanceSet(ModelViewSet):
    # permission_classes = [IsAdminOrReadOnly]
    pagination_class = DefaultPageNumberPaginaton
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer

#
# # Create your views here.
# # class BookListView(generics.ListAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
# todo function based view
# todo function based view is used to overide a certain function
# @api_view(['GET', 'POST'])
# def book_List(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         email = BookSerializer(data=request.data)
#         email.is_valid(raise_exception=True)
#         email.save()
#         return Response("Book saved successfully")
#
#
# @api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# def book_detail(request, pk):
#     # try:
#     #     email = Book.objects.get(pk=pk)
#     # except Book.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#     email = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = BookDetailSerializer(email)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'DELETE':
#         email.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     if request.method == 'PUT':
#         email = BookSerializer(data=request.data)
#
#
# @api_view(['GET'])
# def author_list(request):
#     if request.method == 'GET':
#         author = Author.objects.all()
#         serializer = AuthorSerializer(author, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#
# @api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# def author_detail(request, pk):
#     if request.method == 'GET':
#         author = Author.objects.get(pk=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
