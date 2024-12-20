from django.contrib.auth import get_user_model
from rest_framework.fields import IntegerField, CharField, DecimalField, URLField, ImageField, ListField
from rest_framework.relations import HyperlinkedRelatedField, StringRelatedField, SlugRelatedField, \
    PrimaryKeyRelatedField
from rest_framework.reverse import reverse
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer, Serializer

from Store.models import (
    Profile,
    Book,
    BookInstance,
    Condition,
    Genre,
    Author,
    Publisher,
)


# custom Fields
class AbsoluteURLField(URLField):
    def to_representation(self, value):
        request = self.context.get('request')
        url = request.build_absolute_uri(str(value))

        return url


UserModel = get_user_model()


class ProfileSerializer(HyperlinkedModelSerializer):
    user = HyperlinkedRelatedField(
        view_name='Store:user-detail',
        lookup_field='pk',
        many=False,
        queryset=UserModel.objects.all(),
    )

    class Meta:
        model = Profile
        fields = ['pk', 'user']


class UserSerializer(ModelSerializer):
    class Meta:
        model = UserModel
        fields = ['pk', 'username']


class BookSerializer(ModelSerializer):
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
    publisher = PrimaryKeyRelatedField(queryset=Publisher.objects.all())

    class Meta:
        model = Book
        fields = ['pk', 'title', 'description', 'cover', 'publisher', 'published_year', 'genres', 'authors']


class BookUpdateSerializer(BookSerializer):
    pass


class BookInstanceSerializer(HyperlinkedModelSerializer):
    book = HyperlinkedRelatedField(
        view_name='Store:book-detail',
        lookup_field='pk',
        many=False,
        queryset=Book.objects.all(),
    )
    condition = HyperlinkedRelatedField(
        view_name='Store:condition-detail',
        lookup_field='pk',
        many=False,
        queryset=Condition.objects.all(),
    )

    class Meta:
        model = BookInstance
        fields = ['pk', 'book', 'condition', 'storage_cell', 'purchase_price', 'sale_price', 'status']


class ConditionSerializer(ModelSerializer):
    class Meta:
        model = Condition
        fields = ['pk', 'degree_of_wear', 'description']


class GenreSerializer(ModelSerializer):
    class Meta:
        model = Genre
        fields = ['pk', 'name']


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['pk', 'name']


class PublisherSerializer(ModelSerializer):
    class Meta:
        model = Publisher
        fields = ['pk', 'name']


class CatalogSerializer(Serializer):
    pk = IntegerField()
    title = CharField()
    genres = ListField(child=CharField())
    authors = ListField(child=CharField())
    description = CharField()
    cover = AbsoluteURLField(source='cover.url')
    publisher = CharField()
    published_year = IntegerField()
    count = IntegerField()
    minPrice = DecimalField(max_digits=10, decimal_places=2)
    maxPrice = DecimalField(max_digits=10, decimal_places=2)

    bestCondition = CharField()
    degree_of_wear = IntegerField()


class ConditionForCatalogSerializer(ModelSerializer):
    class Meta:
        model = Condition
        fields = ['pk', 'degree_of_wear', 'description']


class BookInstanceForCatalogSerializer(ModelSerializer):
    condition = ConditionForCatalogSerializer(
        many=False,
    )

    class Meta:
        model = BookInstance
        fields = ['pk', 'condition', 'storage_cell', 'purchase_price', 'sale_price', 'status']


class CatalogDetailSerializer(Serializer):
    pk = IntegerField()
    title = CharField()
    instances = BookInstanceForCatalogSerializer(many=True)
    genres = ListField(child=CharField())
    authors = ListField(child=CharField())
    description = CharField()
    cover = AbsoluteURLField(source='cover.url')
    publisher = CharField()
    published_year = IntegerField()
    count = IntegerField()
    minPrice = DecimalField(max_digits=10, decimal_places=2)
    maxPrice = DecimalField(max_digits=10, decimal_places=2)
    bestCondition = CharField()
    degree_of_wear = IntegerField()
