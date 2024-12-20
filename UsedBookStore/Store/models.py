from django.contrib.auth import get_user_model
from django.db import models

from UsedBookStore.settings import BASE_DIR, MEDIA_ROOT

UserModel = get_user_model()


"""
Models:
    Profile
        - user
    Book
        - title
        - description
        - cover
        - publisher
        - published_year
        - genres
        - authors
    BookInstance
        - book
        - condition
        - storage_cell
        - purchase_price
        - sale_price
    Condition
        - degree_of_wear
        - description
    Genre
        - name
    Author
        - name
    Publisher
        - name
"""


class Profile(models.Model):
    user = models.OneToOneField(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.user.username


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    class Meta:
        unique_together = ('title', 'publisher', 'published_year')

    title = models.CharField(max_length=255)
    description = models.TextField()
    cover = models.ImageField(
        upload_to='covers/',
        blank=True,
        null=True,
    )
    published_year = models.IntegerField()

    genres = models.ManyToManyField(
        to=Genre,
        related_name='books',
    )
    authors = models.ManyToManyField(
        to=Author,
        related_name='books',
    )
    publisher = models.ForeignKey(
        to='Publisher',
        on_delete=models.PROTECT,
        related_name='books',
    )

    DEFAULT_COVER_PATH = 'covers/default_cover.jpg'  # Путь к файлу обложки по умолчанию

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self._state.adding:
            # Если поле cover не установлено, устанавливаем значение по умолчанию
            if not self.cover:
                self.cover = self.DEFAULT_COVER_PATH
            print('Объект создан')
        else:
            self.cover = Book.objects.get(pk=self.pk).cover
            print('Объект обновлен', self.cover)

    def __str__(self):
        return self.title


class Status(models.TextChoices):
    IN_STOCK = 'in_stock', 'В наличии'
    RESERVED = 'reserved', 'Зарезервировано'
    SOLD = 'sold', 'Продано'
    LOST = 'lost', 'Потеряно'


class BookInstance(models.Model):
    book = models.ForeignKey(
        to=Book,
        on_delete=models.CASCADE,
        related_name='instances',
    )
    condition = models.ForeignKey(
        to='Condition',
        on_delete=models.PROTECT,
        related_name='book_instances',
    )

    status = models.CharField(
        max_length=20,
        choices=Status.choices,
        default=Status.IN_STOCK,
    )
    storage_cell = models.CharField(max_length=50, blank=True, null=True)
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    sale_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.book.title} - {self.storage_cell}"


class Condition(models.Model):
    class Meta:
        ordering = ['degree_of_wear']

    degree_of_wear = models.IntegerField(unique=True)
    description = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.degree_of_wear} - {self.description}'
