from rest_framework import generics
from book.models import Book
from book.serializer import BookSerializer
from rest_framework.pagination import PageNumberPagination


class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination


class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.filter()
    serializer_class = BookSerializer
    pagination_class = PageNumberPagination