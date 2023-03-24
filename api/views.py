from django.shortcuts import render
from rest_framework.response import Response
from book.models import *
from .serializers import *
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import generics


# todo class base view
class BookCreateApiView(generics.ListAPIView):
    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer



#
# # Create your views here.
# # class BookListView(generics.ListAPIView):
# #     queryset = Book.objects.all()
# #     serializer_class = BookSerializer
#
# @api_view(['GET', 'POST'])
# def book_List(request):
#     if request.method == "GET":
#         queryset = Book.objects.all()
#         serializer = BookSerializer(queryset, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         book = BookSerializer(data=request.data)
#         book.is_valid(raise_exception=True)
#         book.save()
#         return Response("Book saved successfully")
#
#
# @api_view(['GET', 'DELETE', 'PUT', 'PATCH'])
# def book_detail(request, pk):
#     # try:
#     #     book = Book.objects.get(pk=pk)
#     # except Book.DoesNotExist:
#     #     return Response(status=status.HTTP_404_NOT_FOUND)
#     book = Book.objects.get(pk=pk)
#     if request.method == 'GET':
#         serializer = BookDetailSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#     if request.method == 'PUT':
#         book = BookSerializer(data=request.data)
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


