from rest_framework.serializers import ModelSerializer
from book.models import Book


class BookSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title', 'author', 'description', 'create_time', 'update_time')
        model = Book