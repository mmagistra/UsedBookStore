from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import ModelViewSet

from Store.models import (
    Profile,
    Book,
    BookInstance,
    Condition,
    Genre,
    Author,
)
from Store.serializers import (
    ProfileSerializer,
    UserSerializer,
    BookSerializer,
    BookInstanceSerializer,
    ConditionSerializer,
    GenreSerializer,
    AuthorSerializer,
)


UserModel = get_user_model()


class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [DjangoModelPermissions]


class UserViewSet(ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer
    permission_classes = [DjangoModelPermissions]
    http_method_names = ['get']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [DjangoModelPermissions]


class BookInstanceViewSet(ModelViewSet):
    queryset = BookInstance.objects.all()
    serializer_class = BookInstanceSerializer
    permission_classes = [DjangoModelPermissions]


class ConditionViewSet(ModelViewSet):
    queryset = Condition.objects.all()
    serializer_class = ConditionSerializer
    permission_classes = [DjangoModelPermissions]


class GenreViewSet(ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    permission_classes = [DjangoModelPermissions]


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [DjangoModelPermissions]
