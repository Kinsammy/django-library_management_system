from rest_framework import serializers
from book.models import *
from djoser.serializers import UserCreateSerializer


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']
        date_of_birth = serializers.DateTimeField(read_only=True)


class BookSerializer(serializers.ModelSerializer):
    # todo relationship
    # author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description', 'genre', 'language', 'price', 'discount_price', 'author']

    # Todo The below code will make the author field be clickable hyperlink / or nested resources
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author-detail'

    )
    # todo to add new field that is not in your model
    discount_price = serializers.SerializerMethodField(method_name='discount')

    # todo to calculate discount
    def discount(self, book: Book):
        return book.price * 25 / 100

    # todo the below syntax will show the author id
    # author = AuthorSerializer
    #  todo the below syntax will bring the author name
    # author = serializers.StringRelatedField()


class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'isbn', 'description']

# # todo is used when you wanted to add something that are not inside your model
# class AuthorSerializer(serializers.Serializer):
#     first_name = serializers.CharField(max_length=55)
#     last_name = serializers.CharField(max_length=55)
#     birth_day = serializers.DateField(source='date_of_birth')


class UserCreate(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        fields = ['id', 'username', 'email', 'password', 'first_name', 'last_name']