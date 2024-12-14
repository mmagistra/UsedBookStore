from django.contrib.auth import get_user_model
from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField, SlugRelatedField

from Store.models import (
    Profile,
    Book,
    BookInstance,
    Condition,
    Genre,
    Author,
)


UserModel = get_user_model()


class ProfileSerializer:
    user = HyperlinkedRelatedField(
        view_name='training_site_app:user-detail',
        lookup_field='pk',
        many=False,
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = Profile
        fields = ['pk', 'user']


class UserSerializer:
    class Meta:
        model = UserModel
        fields = ['pk', 'username']


class BookSerializer:
    genres = SlugRelatedField(
        many=True,
        queryset=Genre.objects.all(),
        read_only=False,
        slug_field='name',
    )
    authors = SlugRelatedField(
        many=True,
        queryset=Author.objects.all(),
        read_only=False,
        slug_field='name',
    )

    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'cover', 'publisher', 'published_year', 'genres', 'authors']


class BookInstanceSerializer:
    book = HyperlinkedRelatedField(
        view_name='store:book-detail',
        lookup_field='pk',
        many=False,
        queryset=Book.objects.all(),
    )
    condition = HyperlinkedRelatedField(
        view_name='store:condition-detail',
        lookup_field='pk',
        many=False,
        queryset=Condition.objects.all(),
    )

    class Meta:
        model = BookInstance
        fields = ['pk', 'book', 'condition', 'storage_cell', 'purchase_price', 'sale_price']


class ConditionSerializer:
    class Meta:
        model = Condition
        fields = ['pk', 'degree_of_wear', 'description']


class GenreSerializer:
    class Meta:
        model = Genre
        fields = ['pk', 'name']


class AuthorSerializer:
    class Meta:
        model = Author
        fields = ['pk', 'name']
