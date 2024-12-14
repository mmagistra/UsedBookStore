from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Store.views import (
    UserViewSet,
    ProfileViewSet,
    BookViewSet,
    BookInstanceViewSet,
    ConditionViewSet,
    GenreViewSet,
    AuthorViewSet,
)

app_name = 'Store'

router = DefaultRouter()
router.register('users', UserViewSet, 'user')
router.register('profiles', ProfileViewSet, 'profile')
router.register('books', BookViewSet, 'book')
router.register('book_instances', BookInstanceViewSet, 'book_instance')
router.register('conditions', ConditionViewSet, 'condition')
router.register('genres', GenreViewSet, 'genre')
router.register('authors', AuthorViewSet, 'author')


urlpatterns = [
    path('', include(router.urls)),
]
