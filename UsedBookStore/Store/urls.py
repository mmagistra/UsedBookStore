from django.template.defaulttags import url
from django.urls import path, include
from django.views.generic import DetailView, TemplateView
from rest_framework.routers import DefaultRouter

from Store.views import (
    UserViewSet,
    ProfileViewSet,
    BookViewSet,
    BookInstanceViewSet,
    ConditionViewSet,
    GenreViewSet,
    AuthorViewSet,
    PublisherViewSet,
    CheckMediaUrl,
    CatalogView,
    CatalogDetailView,
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
router.register('publishers', PublisherViewSet, 'publisher')

urlpatterns = [
    path('', include(router.urls)),
    path('check_media_url/<int:pk>/', CheckMediaUrl.as_view(), name='check-media-url'),
    path('catalog/', CatalogView.as_view(), name='catalog'),
    path('catalog/<int:pk>/', CatalogDetailView.as_view(), name='catalog-detail'),
]
