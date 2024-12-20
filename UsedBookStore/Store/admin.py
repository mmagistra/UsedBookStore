from django.contrib import admin

from django.contrib import admin

from .models import Profile, Book, BookInstance, Condition, Genre, Author, Publisher


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username')
    list_display_links = ('pk', 'username')
    list_filter = ('user',)

    def username(self, obj: Profile):
        return obj.user


class BookInstanceInline(admin.TabularInline):
    model = BookInstance


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'publisher', 'published_year', 'display_authors', 'display_genres')
    list_display_links = ('pk', 'title')
    list_filter = ('genres', 'authors', 'publisher', 'published_year')

    inlines = [BookInstanceInline]

    def display_authors(self, obj: Book) -> str:
        return ', '.join([author.name for author in obj.authors.all()])

    display_authors.short_description = 'Authors'

    def display_genres(self, obj: Book) -> str:
        return ', '.join([genre.name for genre in obj.genres.all()])

    display_genres.short_description = 'Genres'

    def save_model(self, request, obj, form, change):
        if not obj.cover:
            obj.cover = 'covers/default_cover.jpg'
        super().save_model(request, obj, form, change)


@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('pk', 'book', 'storage_cell', 'purchase_price', 'sale_price', 'condition')
    list_display_links = ('pk', 'book')
    list_filter = ('book', 'condition')

    def condition(self, obj: BookInstance) -> str:
        return obj.condition


@admin.register(Condition)
class ConditionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'degree_of_wear', 'description')
    list_display_links = ('pk', 'degree_of_wear')


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    list_display_links = ('pk', 'name')
